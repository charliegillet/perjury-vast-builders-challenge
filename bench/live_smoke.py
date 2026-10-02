"""Small live check of metadata and abstention policy; not a held-out accuracy benchmark."""
from __future__ import annotations
import asyncio
import json
from bench.common import load_claims, now_iso, save_run
from bench.run_bench import predict_one
from perjury.pipeline import load_context

VERIFIED = {
    'd05': 'Team index metadata identifies Nashville; Toronto contradicts that metadata.',
    'd14': 'Temporal braking assertions are outside the verifier policy, irrespective of the footage.'
}


def select_verified(rows, index):
    selected, excluded = [], []
    for row in rows:
        reason = None
        if row['scene'] not in index.scenes():
            reason = 'Scene is absent from the live index.'
        elif row['truth_source'] == 'eyeball_pending':
            reason = 'Required independent manual ground-truth review is incomplete.'
        elif row['id'] not in VERIFIED:
            reason = 'Ground truth assumes the original full dataset, not this 300-second partial archive.'
        elif row['id'] == 'd05' and index.locations(row['scene']) != {'nashville'}:
            reason = 'Nashville metadata has not been confirmed for every segment.'
        if reason:
            excluded.append({'id': row['id'], 'scene': row['scene'], 'reason': reason})
        else:
            selected.append(row)
    return selected, excluded


async def run():
    ctx = load_context()
    if ctx.settings.mode != 'live':
        raise SystemExit('Live smoke evaluation requires PERJURY_MODE=live.')
    rows, exclusions = select_verified(load_claims(split='dev'), ctx.index)
    if not rows:
        raise SystemExit('No live dev claims have verified ground truth.')
    started = now_iso()
    results = []
    for row in rows:
        result = await predict_one(row, jury_size=ctx.settings.jury_size, variant='neutral', timeout_s=90)
        results.append(result)
        print(row['id'], result['verdict'], result['error'], flush=True)
    run = {'version':1, 'split':'dev', 'variant':'neutral', 'mode':'live', 'offline':False,
           'jury_size':ctx.settings.jury_size, 'started_at':started, 'finished_at':now_iso(),
           'evaluation_scope': 'Live smoke check of two verified metadata/policy claims; not general accuracy.',
           'ground_truth_basis':VERIFIED, 'exclusions':exclusions, 'coverage':ctx.index.coverage,
           'held_out_test_run':False, 'promotion_frozen_at':None, 'weave_url':None, 'results':results}
    print('saved', save_run(run))


if __name__ == '__main__':
    asyncio.run(run())
