# Launch checklist — irishairtowater.com

Repo: https://github.com/SamOHON0/irishairtowater

Static site, no build step. Vercel serves it as-is. `cleanUrls` is on, so `/services`
is the live URL and `/services.html` 308s to it. Canonicals and the sitemap use the
clean form. Internal links keep `.html` so the folder still previews by double-clicking
`index.html` locally.

---

## Blockers before go-live

### 1. Contact form is a stub
`assets/main.js` fakes the submit. Every form carries `data-iatw-form`, three of them
across index, maintenance and contact. Create a Formspree form, then set the `action`
and `method` on each and delete the fake handler at the bottom of `main.js`.

### 2. Photos and video — done, zero placeholders
The hero is a full-bleed background video (`media/hero-reel.mp4`, 21s, 1.1MB), a slow
pan-and-crossfade reel built with ffmpeg from five of Dáire's own install photos, graded
dark under a pine scrim so the headline stays readable. It autoplays muted and looped,
falls back to a poster frame, and pauses under prefers-reduced-motion. The 45-second
Facebook reviews carousel (1167.mp4) sits in the reviews section with a poster and
controls. The balancing section uses the manifold from his own LinkedIn explainer
graphic. There are no placeholder tiles anywhere on the site.

The 7-second brand animation (1156.mp4 → `media/brand-intro.mp4`) was the hero briefly
but cannot work as a bleed (white background, text-unsafe); it stays in `media/` unused,
ready for social posts or a loading treatment if ever wanted.

Still worth chasing for a v2: **a photo of Dáire himself**, and the van. The About
section says "One name on the van" and currently shows a finished install instead of
a person.

### 3. Certificates — 4 of 6 shown as real documents
QQI, Grant R290, manual handling and the Safety Statement cover are rendered from the
actual documents on `certifications.html`. F-GAS and insurance have deliberate icon
tiles instead of images, because those documents have not been supplied; when they
arrive, render page 1 to `images/cert-fgas.jpg` / `images/cert-insurance.jpg` and swap
the `doc-tile` div for a `doc-frame` img in `pages.py`. No fake or stock documents are
used anywhere.

### 4. Logo — done
The original logo file arrived and replaced the video-frame extract. `images/logo-mark.png`
(the flame/snowflake mark, 360px) is the header mark and the favicon; `images/logo.png`
(the full lockup) sits in the footer on a white tile. The header tagline now reads
"Heat Pump Services" to match the logo's own wording.

The raw 1024px source in the repo root (`logo.png`) can be deleted; the processed copies
in `images/` are what the site uses. `favicon.svg` (my drawn stand-in) is unreferenced
and can also be deleted.

### 5. og:image — done
`images/og-image.jpg` is a 1200x630 crop of the hero photo, wired into every page.
Swap it if a better shot arrives.

---

## Questions for Dáire

1. **Maintenance pricing.** His own PDF carries no price, so neither does the page.
   Does he want a figure, or "from €X"?
2. **F-GAS certificate number.** Not on anything he sent. The certifications page argues
   "qualifications you can check" and a registration number is the one genuinely
   checkable thing on it.
3. **Facebook URL.** Instagram is `@irish_airtowater`. The Facebook link currently points
   at Instagram as a placeholder.
4. **Grant — his own photos answer this.** Three of the photos he just sent show Grant
   Aerona outdoor units he has worked on, and he holds the Grant R290 certificate. His
   website still lists only five brands and does not include Grant, so it is left out of
   the brands row for now. Worth one line to him: "do you want Grant added to the brands
   list?" It is a one-word change.
5. **Street address** for the LocalBusiness schema. Sligo only at present, which is fine
   if he works from home, but a full address helps local SEO.
6. ~~Two videos unused~~ — used. The videos contained his logo and five real Facebook
   reviews. The logo is now in the header and favicon; three of the reviews are on the
   home page. The original logo file has since arrived and is in use.

---

## Copy policy

This is a first draft written to be safe to send. Every line traces to one of four
sources and nothing is invented:

1. **irishairtowater.com** — his live site. Where he has wording, that wording is used
   verbatim. The three service descriptions, the five common issues, the brands list, the
   hero eyebrow and the coverage lines are all his.
2. **Annual_Maintenance_Customer_Info.pdf** — the whole maintenance page.
3. **Irish_Air_to_Water_Safety_Statement_v2.pdf** — the installation scope, the on-site
   control measures, the insurance wording and the RAMS disclaimer.
4. **His certificates and email signature** — the certifications page and the trust strip.

Two additions beyond those four sources, both still his own material: the hydraulic
balancing section comes from the "Hydraulic Balancing Matters" graphic he posted on
LinkedIn, and the "What our customers say" section on the home page carries three real
Facebook reviews (Stephanie Callaghan, Shawana Moriarty, Rebecca Fabozzi) transcribed
from the promo video he supplied, trimmed for length with the customers' own wording
kept. Two more legible reviews from the same video (Roisin Mc Gloin, Niamh Clancy) are
transcribed in the project notes if more are wanted.

Deliberately **not** on the site, because no document supports it: pricing of any kind,
response-time or turnaround promises, call-out charge policy, a county-by-county coverage
list, invented process steps, and any claim about how he diagnoses or configures systems
beyond what his own site and documents say.

Two judgement calls worth flagging to Dáire:

- **Grant is not in the brands row.** His site and his Safety Statement both list the same
  five brands, and Grant is not among them. The R290 course is a training certificate, so
  it sits on the certifications page instead. If he does install Grant, add it.
- **Installation is on the site but not on his current site.** It comes from his email
  signature and from the Safety Statement, which describes installation work in detail.

## Already done

Home page layout (26 Aug pass): the hero is a layered two-photo composition of his real
installs, six photos sit in a "Recent work" gallery under the common-issues band, coverage
is a slim pine band instead of a third split-section, and the brands strip moved to just
above contact. The hero F-GAS badge was removed because the trust strip directly below it
says the same thing.

Six pages plus a styled 404. Mobile nav and FAQ accordions. Per-page titles, descriptions,
canonicals and OG tags. `HVACBusiness` JSON-LD on every page with services, credentials and
area served, plus a `FAQPage` block on the maintenance page. robots.txt, sitemap.xml,
security headers and a one-year immutable cache on `/assets`. Skip link, single h1 per page,
`aria-current` on the active nav item, `aria-expanded`/`aria-controls` throughout, escape
closes the mobile nav, visible focus rings, `prefers-reduced-motion` honoured.
Reveal-on-scroll only hides content when JS is running, so a blocked script never blanks
the page.

Two corrections to the first draft: the domain is **.com**, not .ie, and the QQI award is a
**Level 6 Advanced Certificate in Refrigeration and Air Conditioning, with Credit**, not a
generic "QQI Certified".

## Regenerating

`build.py` holds the header, footer, shared contact block and page shell. `pages.py`
holds the copy. Run `python3 pages.py` to rewrite the HTML. Editing the HTML directly is
fine too, the generator only exists so six pages stay in sync.

`verify.py` checks every internal link and anchor, JSON-LD validity, meta tag presence,
title and description lengths, and the accessibility basics. Run it after any edit.
