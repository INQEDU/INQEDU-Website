# Notes for Claude

- Static site, no framework. Page text lives in `build.py`; subject pages (including class slots) are generated from `subjects.py`; run `python3 build.py` after editing it, and commit `build.py` and the regenerated `site/` together.
- `site/css/styles.css`, `site/js/main.js` and `site/assets/` are hand-edited, not generated.
- Cloudflare deploys the `site/` folder from `main`. There is no build step on Cloudflare.
- Brand: fonts Libre Baskerville (display) and Almarai (body), self-hosted in `site/assets/fonts`. Colours #F6F3EC, #ECE4DA, #B9A590, #574C3F, #36302A.
- Seven subjects with equal emphasis on the classes pages: English A Language & Literature, English A Literature, History, Geography, Business Management, Maths AA, Maths AI (all SL and HL). The homepage hero label reads "IB Tuition Specialists".
- History and Geography have revised IB courses (History first examined May 2028), so their assessment tables show only figures common to both versions. Verify before adding timings.
- Preview larger changes on a branch first: Cloudflare builds a preview for each branch.
- Enquiries go to WhatsApp (+65 8866 5396) via `whatsapp_link()` in `build.py`, which pre-fills a message; subject pages name the subject in it. There is no contact form.
- FAQ answers live in `FAQS` in `build.py` and appear at the bottom of the contact page (`contact.html#faq`). Do not add facts the owner has not confirmed (fees, class sizes, trial lessons, location, one-to-one lessons).
- Homepage class photos are in `site/assets/photos/`; metadata is stripped before adding. They show students, so confirm consent with the owner before adding new ones.
- The "Trusted by students from" belt (scrolls continuously in full colour, static for reduced motion) comes from `SCHOOLS` in `build.py`. A logo file in `site/assets/schools/<slug>.<ext>` replaces that school's text name automatically. Only add logos the owner supplies.
