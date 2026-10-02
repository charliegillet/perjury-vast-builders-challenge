"""Bench layer: claims.yaml shape (§8 table), Wilson CI, choose_m, jury-size curve on synthetic votes, test-split guard,
promotion rule, and the fill_numbers fixture refusal."""
from __future__ import annotations

import collections
import json

import pytest

import bench.common as common
from bench import fill_numbers, report, run_bench
from bench.common import _choose_m_local, _wilson_local, claim_verdict, load_claims, match_atoms

ATOM_LABELS = {"SUPPORTED", "CONTRADICTED", "UNVERIFIABLE", "MOOT"}
TYPES = {"scene_identity", "road_surface", "weather", "traffic_state", "lighting", "coco_presence", "count", "towing",
         "heavy_vehicle_kind", "action", "attribute", "identity_intent", "cross_camera", "lane_position", "other"}


# ---------------------------------------------------------------- claims.yaml
def test_claim_counts_match_section_8_table():
    rows = load_claims()
    assert len(rows) == 47
    by = collections.Counter((r["split"], r["kind"]) for r in rows)
    assert sum(v for (s, _), v in by.items() if s == "dev") == 17
    assert sum(v for (s, _), v in by.items() if s == "test") == 30
    assert [by[("dev", k)] for k in ("lie", "truth", "unverifiable", "compound")] == [7, 6, 4, 0]
    assert [by[("test", k)] for k in ("lie", "truth", "unverifiable", "compound")] == [10, 10, 6, 4]


def test_claim_rows_are_well_formed():
    rows = load_claims()
    assert len({r["id"] for r in rows}) == len(rows)
    assert len({(r["text"], r["scene"]) for r in rows}) == len(rows)
    expect = {"lie": {"FALSE"}, "truth": {"TRUE"}, "unverifiable": {"UNPROVEN"}, "compound": {"TRUE", "FALSE", "UNPROVEN"}}
    for r in rows:
        assert r["scene"] in (1, 2, 3), r["id"]
        assert r["expected_claim"] in expect[r["kind"]], r["id"]
        assert r["truth_source"] in ("dataset_structure", "eyeball_pending"), r["id"]
        assert r["expected_atoms"], r["id"]
        labels = [a["expected"] for a in r["expected_atoms"]]
        for a in r["expected_atoms"]:
            assert a["span"] in r["text"], (r["id"], a["span"])
            assert a["type"] in TYPES and a["expected"] in ATOM_LABELS, (r["id"], a)
        # expected atoms must reproduce the expected claim verdict under the §4 rule
        assert claim_verdict(labels) == r["expected_claim"], r["id"]


def test_heroes_in_dev_and_warmup_compound_in_test():
    rows = {(r["text"], r["scene"]): r for r in load_claims()}
    assert rows[("A pickup is towing a trailer.", 2)]["split"] == "dev"
    assert rows[("A pickup is towing a trailer.", 2)]["expected_claim"] == "FALSE"
    assert rows[("A pickup is towing a trailer.", 1)]["split"] == "dev"
    assert rows[("A pickup is towing a trailer.", 1)]["expected_claim"] == "TRUE"
    w = rows[("Three pedestrians are crossing the highway in the snow.", 2)]
    assert (w["split"], w["kind"], w["expected_claim"]) == ("test", "compound", "FALSE")
    assert sum(r["sycophancy"] for r in load_claims()) == 1


def test_dev_supports_promotion_for_hard_types():
    """n >= 5 hard atoms and >= 1 planted lie per hard-verdict type on dev, or the type can never be promoted."""
    hard = collections.Counter()
    lies = collections.Counter()
    for r in load_claims(split="dev"):
        for a in r["expected_atoms"]:
            if a["expected"] in ("SUPPORTED", "CONTRADICTED"):
                hard[a["type"]] += 1
                lies[a["type"]] += a["expected"] == "CONTRADICTED"
    for t in ("towing", "coco_presence", "road_surface", "traffic_state", "lighting", "scene_identity"):
        assert hard[t] >= 5 and lies[t] >= 1, (t, hard[t], lies[t])


# ---------------------------------------------------------------- stats
@pytest.mark.parametrize("k,n,lo,hi", [(0, 10, 0.0, 0.2775), (5, 10, 0.2366, 0.7634), (10, 10, 0.7225, 1.0),
                                       (7, 10, 0.3968, 0.8922)])
def test_wilson_known_values(k, n, lo, hi):
    for f in (_wilson_local, common.wilson_ci):
        a, b = f(k, n)
        assert a == pytest.approx(lo, abs=1e-4) and b == pytest.approx(hi, abs=1e-4)


def test_wilson_empty_and_rate_shape():
    assert _wilson_local(0, 0) == (0.0, 1.0)
    assert common.rate(0, 0) == {"k": 0, "n": 0, "rate": None, "ci": None}
    r = common.rate(3, 4)
    assert r["rate"] == 0.75 and len(r["ci"]) == 2


@pytest.mark.parametrize("alpha,m", [(0.05, 2), (0.10, 3), (0.20, 4), (0.27, 4), (0.40, None)])
def test_choose_m_section_7_table(alpha, m):
    assert _choose_m_local(alpha, 6) == m
    assert common.choose_m(alpha, 6) == m


# ---------------------------------------------------------------- atom matching
def test_match_atoms_by_span_and_type():
    expected = [{"span": "pedestrians", "type": "coco_presence", "expected": "CONTRADICTED"},
                {"span": "Three", "type": "count", "expected": "MOOT"},
                {"span": "in the snow", "type": "road_surface", "expected": "SUPPORTED"}]
    atoms = [{"id": "a1", "span": "Three pedestrians", "type": "count"},
             {"id": "a2", "span": "pedestrians", "type": "coco_presence"},
             {"id": "a3", "span": "the snow", "type": "road_surface"}]
    avs = [{"atom_id": "a1", "verdict": "MOOT"}, {"atom_id": "a2", "verdict": "CONTRADICTED"},
           {"atom_id": "a3", "verdict": "SUPPORTED"}]
    m = match_atoms(expected, atoms, avs)
    assert [x["atom_id"] for x in m] == ["a2", "a1", "a3"]
    assert all(x["correct"] for x in m)
    assert match_atoms([{"span": "braked", "type": "action", "expected": "UNVERIFIABLE"}], atoms, avs)[0]["got"] == "MISSING"


# ---------------------------------------------------------------- synthetic runs
def _vote(cam, vote, zoom=None, probe="P-TOW"):
    return {"camera": cam, "vote": vote, "tier": "JURY", "probe": probe, "zoom_ok": zoom}


def _towing_result(cid, kind, expected_claim, votes, *, sycophancy=False, scene=2, verdict=None):
    exp_atom = {"FALSE": "CONTRADICTED", "TRUE": "SUPPORTED"}[expected_claim]
    got = verdict or exp_atom
    return {"id": cid, "scene": scene, "text": "A pickup is towing a trailer.", "kind": kind, "split": "dev",
            "expected_claim": expected_claim, "sycophancy": sycophancy,
            "expected_atoms": [{"span": "A pickup is towing a trailer", "type": "towing", "expected": exp_atom}],
            "verdict": claim_verdict([got]), "elapsed_ms": 5000, "gpu_s": 30.0, "calls": 20,
            "atoms": [{"id": "a1", "span": "A pickup is towing a trailer", "type": "towing"}],
            "atom_verdicts": [{"atom_id": "a1", "verdict": got, "tiers": ["JURY"], "votes": votes,
                               "stats": {"Y": sum(v["vote"] == "yes" for v in votes), "k": len(votes),
                                         "t1": {"supports": 0}}}],
            "atom_matches": [{"span": "A pickup is towing a trailer", "type": "towing", "expected": exp_atom,
                              "got": got, "atom_id": "a1", "correct": got == exp_atom}]}


def _cams(n=16):
    return [f"p{1 + i // 6}c{1 + i % 6}" for i in range(n)]


def test_jury_curve_recomputes_from_stored_votes():
    lie = _towing_result("d01", "lie", "FALSE", [_vote(c, "no") for c in _cams()], sycophancy=True)
    true = _towing_result("d08", "truth", "TRUE", [_vote(c, "yes", True) for c in _cams()], scene=1)
    # a noisy truth: 8 zoom-passed yes, 8 no
    mixed = _towing_result("d09", "truth", "TRUE",
                           [_vote(c, "yes" if i % 2 else "no", True if i % 2 else None) for i, c in enumerate(_cams())],
                           scene=3)
    run = {"split": "dev", "mode": "fixture", "results": [lie, true, mixed]}
    curve = report.jury_curve([run], alpha=0.10, subsets=50, seed=0)
    assert [c["k"] for c in curve] == [1, 3, 6, 16]
    by_k = {c["k"]: c for c in curve}
    for c in curve:
        assert c["catch"] == 1.0                 # 0 yes among k valid no-votes -> CONTRADICTED at every k
        assert c["false_accusation"] <= 0.5      # the mixed truth may be falsely accused only when it draws 0 yes
        assert c["subsets"] == 50 and c["n_lie_claims"] == 1 and c["n_true_claims"] == 2
    assert by_k[1]["m"] is None and by_k[1]["support"] == 0.0   # one juror can never reach a 5% false-yes quorum
    assert by_k[16]["support"] == 1.0 and by_k[16]["false_accusation"] == 0.0
    assert report.jury_curve([run], alpha=0.10, subsets=50, seed=0) == curve   # deterministic


def test_jury_curve_skips_k_larger_than_stored_jury():
    lie = _towing_result("d01", "lie", "FALSE", [_vote(c, "no") for c in _cams(6)])
    curve = report.jury_curve([{"split": "dev", "results": [lie]}], alpha=0.1, subsets=5)
    assert [c["k"] for c in curve] == [1, 3, 6]


def test_sycophancy_neutral_vs_lead():
    neutral = _towing_result("d01", "lie", "FALSE",
                             [_vote(c, "yes" if i < 2 else "no", i == 0) for i, c in enumerate(_cams())], sycophancy=True)
    lead = _towing_result("d01", "lie", "FALSE",
                          [_vote(c, "yes" if i < 10 else "no", probe="P-LEAD") for i, c in enumerate(_cams())],
                          sycophancy=True)
    s = report.sycophancy([{"results": [neutral]}], [{"results": [lead]}])
    assert s["neutral"] == {"yes": 2, "yes_after_zoom": 1, "n": 16}
    assert s["lead"] == {"yes": 10, "n": 16}


def test_promotion_rule_on_dev_run():
    res = [_towing_result(f"l{i}", "lie", "FALSE", [_vote(c, "no") for c in _cams(6)]) for i in range(3)]
    res += [_towing_result(f"t{i}", "truth", "TRUE", [_vote(c, "yes", True) for c in _cams(6)]) for i in range(2)]
    doc = report.promotion_from_run({"mode": "fixture", "results": res, "_path": "x"}, jury_size=6)
    t = doc["types"]["towing"]
    assert t["promoted"] and t["n"] == 5 and t["catch"] == 1.0 and t["false_accusation"] == 0.0
    assert doc["alpha"]["towing"] == 0.0 and doc["m"]["towing"] == 1
    # one lie missed -> catch 2/3 < 80% -> demoted; n < 5 -> demoted
    res[0] = _towing_result("l0", "lie", "FALSE", [_vote(c, "no") for c in _cams(6)], verdict="UNVERIFIABLE")
    assert not report.promotion_from_run({"results": res}, jury_size=6)["types"]["towing"]["promoted"]
    assert not report.promotion_from_run({"results": res[1:4]}, jury_size=6)["types"]["towing"]["promoted"]


def test_split_metrics_and_report_build(tmp_path, monkeypatch):
    monkeypatch.setattr(common, "CACHE", tmp_path)
    runs = tmp_path / "bench_runs"
    lie = _towing_result("d01", "lie", "FALSE", [_vote(c, "no") for c in _cams()], sycophancy=True)
    truth = _towing_result("d08", "truth", "TRUE", [_vote(c, "yes", True) for c in _cams()], scene=1)
    unv = {**_towing_result("d14", "truth", "TRUE", [], scene=1), "kind": "unverifiable",
           "expected_claim": "UNPROVEN", "verdict": "UNPROVEN"}
    common.save_run({"split": "dev", "variant": "neutral", "mode": "fixture", "started_at": "1", "finished_at": "2",
                     "results": [lie, truth, unv]}, runs / "dev_1.json")
    rep = report.build_report(runs_dir=runs, cache=tmp_path, subsets=10)
    d = rep["splits"]["dev"]
    assert rep["fixture"] and rep["mode"] == "fixture" and rep["splits"]["test"] is None
    assert d["catch"]["k"] == 1 and d["catch"]["n"] == 1
    assert d["support"]["rate"] == 1.0 and d["correct_decline"]["rate"] == 1.0
    assert rep["numbers"]["X"] is None          # no test run -> the headline number is unmeasured
    assert rep["numbers"]["j"] == 0 and rep["numbers"]["syco_n"] == 16
    assert {"generated_at", "splits", "jury_curve", "sycophancy", "stock", "promotion", "witness", "numbers",
            "weave_url"} <= set(rep)
    json.dumps(rep)


def test_witness_summary_is_shape_tolerant():
    w = {"mode": "live", "parents": [{"source": "s2_p1c1", "sentences": [
        {"text": "a", "verdict": "FALSE", "human_label": "FALSE", "witness": "videos/synthesize"},
        {"text": "b", "verdict": "UNPROVEN", "human_label": "TRUE"}, {"text": "c", "verdict": "TRUE"}]}]}
    s = report.witness_summary(w)
    assert (s["sentences"], s["contradicted"], s["unverifiable"], s["supported"]) == (3, 1, 1, 1)
    assert s["agreement"]["k"] == 1 and s["agreement"]["n"] == 2


# ---------------------------------------------------------------- test-split guard
def test_test_split_guard(tmp_path, monkeypatch):
    monkeypatch.setattr(common, "CACHE", tmp_path)
    run_bench.check_test_guard("dev", "neutral", "live", False)      # dev is never guarded
    with pytest.raises(run_bench.GuardError, match="frozen"):
        run_bench.check_test_guard("test", "neutral", "live", False)
    (tmp_path / "promotion.json").write_text("{}")
    run_bench.check_test_guard("test", "neutral", "live", False)
    run_bench.write_test_lock("neutral", "live", {"started_at": "t0"})
    with pytest.raises(run_bench.GuardError, match="ONCE"):
        run_bench.check_test_guard("test", "neutral", "live", False)
    run_bench.check_test_guard("test", "neutral", "live", True)      # --i-know
    run_bench.check_test_guard("test", "lead", "live", False)        # separate variant
    # fixture runs never touch the live promotion file or lock
    with pytest.raises(run_bench.GuardError):
        run_bench.check_test_guard("test", "neutral", "fixture", False)


def test_main_refuses_test_without_freeze(tmp_path, monkeypatch, capsys):
    monkeypatch.setattr(common, "CACHE", tmp_path)
    monkeypatch.setenv("PERJURY_MODE", "fixture")   # main(--offline) writes these; monkeypatch restores them
    monkeypatch.setenv("PERJURY_WEAVE", "0")
    assert run_bench.main(["--split", "test", "--offline"]) == 3
    assert "REFUSED" in capsys.readouterr().err
    assert not (tmp_path / "fixture_test_run.lock").exists()


# ---------------------------------------------------------------- fill_numbers
def _slides(tmp_path):
    src = tmp_path / "slides"
    src.mkdir()
    (src / "05-validation.md").write_text('Caught {X}/{L} lies; JSON stays {"a": 1}; {Missing} stays.')
    return src


def test_fill_numbers_refuses_fixture(tmp_path):
    src = _slides(tmp_path)
    rep = {"fixture": True, "mode": "fixture", "numbers": {"X": 9, "L": 10}}
    with pytest.raises(fill_numbers.FixtureRefused):
        fill_numbers.fill(rep, src, tmp_path / "out", allow_fixture=False)
    assert not (tmp_path / "out").exists()
    missing = fill_numbers.fill(rep, src, tmp_path / "out", allow_fixture=True)
    text = (tmp_path / "out" / "05-validation.md").read_text()
    assert "9 [FIXTURE]/10 [FIXTURE]" in text and "FIXTURE PREVIEW" in text
    assert missing == {"05-validation.md": {"Missing"}}


def test_fill_numbers_live_leaves_unmeasured_visible(tmp_path):
    src = _slides(tmp_path)
    rep = {"fixture": False, "mode": "live", "numbers": {"X": 9, "L": None}}
    missing = fill_numbers.fill(rep, src, tmp_path / "out", allow_fixture=False)
    text = (tmp_path / "out" / "05-validation.md").read_text()
    assert text.startswith("Caught 9/{L} lies") and '{"a": 1}' in text and "FIXTURE" not in text
    assert missing == {"05-validation.md": {"L", "Missing"}}
    # a report with no mode is treated as unproven -> refused
    with pytest.raises(fill_numbers.FixtureRefused):
        fill_numbers.fill({"numbers": {"X": 1}}, src, tmp_path / "o2", allow_fixture=False)


def test_stock_g2_decision():
    from bench.stock_ab import g2_decision, g2_rows
    assert len(g2_rows()) == 10 and all(r["kind"] == "lie" for r in g2_rows())
    d = g2_decision([{"verdict": "FALSE"}] * 8 + [{"verdict": "TRUE"}, {"verdict": None}])
    assert d["false"] == 8 and d["unclassified"] == 1 and "evidence audit" in d["pitch"]
    assert "believes the lie" in g2_decision([{"verdict": "TRUE"}] * 10)["pitch"]
