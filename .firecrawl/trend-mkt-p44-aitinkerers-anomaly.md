cookie\_policy.sh

$cat /etc/cookies.conf

We use cookies to understand how people use this site.

Analytics cookies help us improve your experience.

They are off by default. Nothing tracks you until you say so.

$select cookie\_preferences

\[1\] Accept All\[2\] Necessary Only

[cat privacy\_policy.md](https://nyc.aitinkerers.org/privacy-policy) Esc to dismiss

[Back to Showcase](https://nyc.aitinkerers.org/hackathons/h_zvqhzy3dMEY/showcase)

[Hackathon Home](https://nyc.aitinkerers.org/hackathons/h_zvqhzy3dMEY) [Team Page](https://nyc.aitinkerers.org/hackathons/h_zvqhzy3dMEY/teams/ht_1uMztk9jtjw)

Hackathon Showcase

# Anomaly Congestion in NYC

Team led by Frank Yu, Co-founder of BlackChamber.ai, a Harvard grad and former MSFT Research game developer with expertise in agentic AI and local LLMs.

![](https://images.aitinkerers.org/cdn-cgi/image/width=96,height=96/blog_images/img-8137-jpeg-Dudi.jpg)

1 member
[Watch Demo](https://www.youtube.com/watch?v=rOrXtsc6LdM)

## Project Videos

[YouTube VideoSubmitted with the project](https://www.youtube.com/watch?v=rOrXtsc6LdM)

## Project Description

This app solves situational awareness at city scale.

New York has thousands of public traffic cameras, but no one watches them continuously. The agent turns that passive feed into an active anomaly detector: it learns what each block normally looks like, then flags the cameras that suddenly deviate — congestion spikes, empty streets that should be busy, unusual pedestrian or vehicle patterns — and explains why in plain English.

Who would use it:

NYC DOT / traffic operations centers — spot incidents before 311 calls come in

Emergency dispatch — validate and triage field reports against live camera evidence

Urban planners / civic data teams — see patterns across boroughs and time windows

Journalists and researchers — monitor public infrastructure conditions in real time

Hackathon judges — it demos a concrete, public-interest AI application on real city data

## Team

[![](https://images.aitinkerers.org/cdn-cgi/image/width=96,height=96/blog_images/img-8137-jpeg-Dudi.jpg)Frank Yu](https://nyc.aitinkerers.org/connect/client/client_WtLwJY2akAI "Frank Yu")

## Products & Tools

AI TinkerersClaudeGoogle CloudLovableeleven labs

## Additional Links

[![](https://www.google.com/s2/favicons?sz=16&domain_url=happy-cloud-path-128216437342.us-east1.run.app)https://happy-cloud-path-128216437342.us-east1.run.app](https://happy-cloud-path-128216437342.us-east1.run.app/)

Live Demo

Summarizing URL...

Anomaly - YouTube

Tap to unmute

[Anomaly](https://www.youtube.com/watch?v=rOrXtsc6LdM) [Frank Yu](https://www.youtube.com/channel/UCQKBeBQxvIZkgI4a00lbApg)

![thumbnail-image](https://yt3.ggpht.com/ytc/AIdro_kuzqKn1YBQNiVHzhGmvKmGrm9d_zzEPSEU48Si8QnigF0=s68-c-k-c0x00ffffff-no-rj)

Frank Yu5 subscribers

[Watch on](https://www.youtube.com/watch?v=rOrXtsc6LdM)

[![](https://www.google.com/s2/favicons?sz=16&domain_url=youtu.be)https://youtu.be/rOrXtsc6LdM](https://youtu.be/rOrXtsc6LdM?si=BZR3G-ZnM1bAh-if)

Video

## Project video

[Open video in a new tab](https://nyc.aitinkerers.org/hackathons/h_zvqhzy3dMEY/entries/ht_1uMztk9jtjw#)

<\\/svg>';
 var scope = root && root.querySelectorAll ? root : document;

 scope.querySelectorAll("div.code-toolbar .copy-to-clipboard-button").forEach(function(button) {
 if (!button \|\| button.dataset.sjPrismCopyEnhanced === "true") {
 return;
 }

 var label = button.querySelector("span");
 if (!label) {
 return;
 }

 label.classList.add("prism-copy-button\_\_label");

 var icon = document.createElement("span");
 icon.className = "prism-copy-button\_\_icon";
 icon.setAttribute("aria-hidden", "true");
 icon.innerHTML = copyIconHtml;
 button.insertBefore(icon, label);

 var successIcon = document.createElement("span");
 successIcon.className = "prism-copy-button\_\_success-icon";
 successIcon.setAttribute("aria-hidden", "true");
 successIcon.textContent = "✓";
 button.appendChild(successIcon);

 button.classList.add("prism-copy-button--enhanced");
 button.dataset.sjPrismCopyEnhanced = "true";
 });
 };

 window.observePrismCopyButtons = window.observePrismCopyButtons \|\| function() {
 if (!window.MutationObserver \|\| document.body.dataset.sjPrismCopyObserver === "true") {
 return;
 }

 var observer = new MutationObserver(function(mutations) {
 mutations.forEach(function(mutation) {
 mutation.addedNodes.forEach(function(node) {
 if (!(node instanceof HTMLElement)) {
 return;
 }

 if (node.matches && node.matches(".copy-to-clipboard-button")) {
 window.enhancePrismCopyButtons(node.parentNode \|\| document);
 } else {
 window.enhancePrismCopyButtons(node);
 }
 });
 });
 });

 observer.observe(document.body, { childList: true, subtree: true });
 document.body.dataset.sjPrismCopyObserver = "true";
 };

 // console.log("loaded \[\[url\]\]") when the page is loaded
 $(document).ready(function() {
 var current\_url = window.location.href;

 document.querySelectorAll('.show-page-body pre, .show-page-body--legacy pre').forEach(function(pre) {
 if (!pre.hasAttribute('data-prismjs-copy-timeout')) {
 pre.setAttribute('data-prismjs-copy-timeout', '1000');
 }
 });

 // Initialize Universal Alert Bar
 if (typeof UniversalAlertBar !== 'undefined') {
 UniversalAlertBar.init();
 }

 // Initialize Prism syntax highlighting
 if (typeof Prism !== 'undefined') {
 Prism.highlightAll();
 }

 // Initialize Mermaid diagrams (loaded via CDN on docs pages)
 if (typeof mermaid !== 'undefined') {
 mermaid.initialize({ startOnLoad: false, theme: 'neutral' });
 mermaid.run();
 }

 window.enhancePrismCopyButtons(document);
 window.observePrismCopyButtons();
 });

 // Do not change the table if there is only one row
 function smart\_article\_table\_styles() {
 var tables = $(".show-page-body table");
 for (var i = 0; i < tables.length; i++) {
 var table = tables\[i\];
 // Check if table has more than one row
 if ($(table).find("tr").length > 1) {
 if ($(table).find("thead").length == 0) {
 var firstRow = $(table).find("tr")\[0\];
 $(table).prepend("");
 // Change the td to th in that row
 var tds = $(firstRow).find("td");
 for (var j = 0; j < tds.length; j++) {
 var td = tds\[j\];
 $(td).replaceWith(" " \+ $(td).html() + " |");
 }
 $(table).find("thead").append(firstRow);
 }
 }
 }
 }

 // total hack. I'm sorry.
 // inside of article.story, show-page-body, look for any tables
 // if the table is missing a thead elemnent, create one using the first row of the table as the thead row.
 $(document).ready(function() {
 //smart\_article\_table\_styles();
 });

 // PostHog tracking (only if cookie consent granted)
 if (window.\_aitAnalyticsConsented && window.posthog && typeof window.posthog.identify === 'function' && "phc\_O22rohygrHUsNDpWnaUqvRWverxN133wf8mAQQhGl2a".length > 0) {
 var posthogPersonProperties = {};

 if ("".length > 0) {
 posthog.identify("", posthogPersonProperties);
 }
 }
-->