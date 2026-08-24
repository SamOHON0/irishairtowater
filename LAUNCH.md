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

### 2. Photos
13 image placeholders, all `<div class="ph">`. See `images/PHOTOS-NEEDED.md` for the
list and suggested filenames. Dáire has sent nothing usable yet beyond certificates.

### 3. Certificates
6 slots on `certifications.html`. Four are in hand (QQI, Grant R290, manual handling,
safety statement) and sit in `Downloads/Air`. Still missing: **F-GAS registration** and
the **insurance certificate**.

### 4. Logo
`.brand-logo` in the header is a dashed placeholder.

`favicon.svg` is a stand-in I drew, an amber droplet over a bone waterline on pine.
It works and it is on-brand, but replace it when the real logo arrives. One file, both
the `icon` and `apple-touch-icon` link tags point at it.

### 5. og:image
Meta tags are in place but `og:image` is deliberately **not set**, because there is no
photo to point at and a broken image URL is worse than none. Link previews on WhatsApp
and Facebook will be plain until this is added. Once the hero shot lands, drop a
1200x630 crop at `images/og-image.jpg` and add to the `page()` head block in `build.py`:

```html
<meta property="og:image" content="https://irishairtowater.com/images/og-image.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
```

---

## Questions for Dáire

1. **Maintenance pricing.** His own PDF carries no price, so neither does the page.
   Does he want a figure, or "from €X"?
2. **F-GAS certificate number.** Not on anything he sent. The certifications page argues
   "qualifications you can check" and a registration number is the one genuinely
   checkable thing on it.
3. **Facebook URL.** Instagram is `@irish_airtowater`. The Facebook link currently points
   at Instagram as a placeholder.
4. **Does he install Grant?** Not in the brands row for now, see the copy policy below.
5. **Street address** for the LocalBusiness schema. Sligo only at present, which is fine
   if he works from home, but a full address helps local SEO.
6. **Two videos** (1156.mp4, 1167.mp4) were supplied and are unused. Hero loop, or drop them.

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

The one exception is the hydraulic balancing section, which comes from the "Hydraulic
Balancing Matters" graphic he posted on LinkedIn, using that graphic's own labels.

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
