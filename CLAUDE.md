# Notes for Claude

- Static site, no framework. Page text lives in `build.py`; subject pages (including class slots) are generated from `subjects.py`; run `python3 build.py` after editing it, and commit `build.py` and the regenerated `site/` together.
- `site/css/styles.css`, `site/js/main.js` and `site/assets/` are hand-edited, not generated.
- Cloudflare deploys the `site/` folder from `main`. There is no build step on Cloudflare.
- Brand: fonts Libre Baskerville (display) and Almarai (body), self-hosted in `site/assets/fonts`. Colours #F6F3EC, #ECE4DA, #B9A590, #574C3F, #36302A.
- Seven subjects with equal emphasis on the classes pages: English A Language & Literature, English A Literature, History, Geography, Business Management, Maths AA, Maths AI (all SL and HL). The homepage hero still names English A as the specialism.
- History and Geography have revised IB courses (History first examined May 2028), so their assessment tables show only figures common to both versions. Verify before adding timings.
- Preview larger changes on a branch first: Cloudflare builds a preview for each branch.
