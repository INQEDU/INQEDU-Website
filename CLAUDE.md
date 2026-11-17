# Notes for Claude

- Static site, no framework. Page text lives in `build.py`; run `python3 build.py` after editing it, and commit `build.py` and the regenerated `site/` together.
- `site/css/styles.css`, `site/js/main.js` and `site/assets/` are hand-edited, not generated.
- Cloudflare deploys the `site/` folder from `main`. There is no build step on Cloudflare.
- Brand: fonts Libre Baskerville (display) and Almarai (body), self-hosted in `site/assets/fonts`. Colours #F6F3EC, #ECE4DA, #B9A590, #574C3F, #36302A.
- English A (Language & Literature, Literature) is the specialism; History, Geography, Business Management and both Maths courses are also taught.
