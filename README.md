# Irish Air to Water

Static marketing site for irishairtowater.com. No build step. Vercel serves it as-is.

**Launch checklist and open questions: see [LAUNCH.md](LAUNCH.md).**

```
index.html            Home
services.html         Six services in detail
maintenance.html      Annual maintenance plan
certifications.html   Certs, safety statement, insurance
contact.html          Contact, coverage, pre-call FAQ
404.html              Styled not-found page
assets/styles.css     Shared stylesheet
assets/main.js        Nav, accordion, reveal, form handler
images/               Photos go here (see images/PHOTOS-NEEDED.md)
vercel.json           cleanUrls, security headers, asset caching
robots.txt
sitemap.xml
build.py / pages.py   Generator. Edit copy here, run `python3 pages.py`.
verify.py             Link, schema, SEO and a11y checks. Run after any edit.
shots.py              Screenshots desktop + mobile, tests nav/accordion/form.
```

`cleanUrls` is on, so `/services` is the live URL. Canonicals and the sitemap use that
form; internal links keep `.html` so the folder still previews by opening `index.html`
locally. Editing the HTML directly is fine, the generator only exists so six pages stay
in sync.

## Local checks

```bash
python3 pages.py    # regenerate HTML from copy
python3 verify.py   # links, anchors, JSON-LD, meta, a11y basics
python3 shots.py    # screenshots + interaction tests (needs playwright)
```

---

## Before go-live

**1. Wire up the contact form.** `assets/main.js` currently fakes the submit. Every form
carries `data-iatw-form`. Point it at Formspree, a Vercel function, or HubSpot.

**2. Swap the placeholders.** Every one is a `<div class="ph">`. Replace with `<img>`.

Photos needed from Dáire, 13 in total:

| Page | Shot |
|---|---|
| Home | Hero: Dáire on an install, or a finished outdoor unit (~1200×1000) |
| Home | Install in progress or plant room |
| Home | Portrait of Dáire, or Dáire with the van (~900×1050) |
| Home + Contact | Map of Ireland graphic, or van on the road (~1000×750) |
| Services | Outdoor unit install / pipework |
| Services | Controls or gauges during commissioning |
| Services | Service visit, filter or unit inspection |
| Services | Controller screen showing an alarm |
| Services | Flow temp readout or efficiency comparison |
| Services | Manifold with flow meters (pairs with the balancing section) |
| Maintenance | Outdoor unit with clear access, or engineer at the unit |
| Certifications | Dáire at work, or van and equipment |

Certificate scans, 6 slots on `certifications.html`. Four are already in hand:
QQI Level 6, Grant R290, Manual Handling, Safety Statement. Still needed: the F-GAS
registration document and the insurance certificate.

**3. Logo.** `.brand-logo` in the header and the favicon are placeholders.

**4. Two videos** (1156.mp4, 1167.mp4) were sent but are not used yet. Options: hero
background loop, or an embedded clip in the relevant services section.

---

## Content sources

Everything on these pages traces back to something Dáire supplied. Nothing is invented.

- **maintenance.html** — taken almost verbatim from `Annual_Maintenance_Customer_Info.pdf`.
  Inclusions, chargeable items, customer responsibilities, the 90-minute visit length, the
  written service record, the warranty point and the exclusions are all his wording, lightly
  edited for web.
- **certifications.html** — dates and numbers read off the actual certificates.
  QQI awarded 14 June 2020 with Credit, NFQ Level 6. Grant R290 attended 30 October 2025.
  Manual handling CERT603373, 11 Mar 2025 to 11 Mar 2028. Safety Statement issued
  6 Aug 2026, review 6 Aug 2027.
- **Insurance wording** — from the Safety Statement: Combined Liability, Public/Products
  Liability and Employers' Liability.
- **I.S. 10101 and safe isolation** — from the Safety Statement's control measures.
- **Hydraulic balancing section** — built from the infographic Dáire posted on LinkedIn.
- **Grant Aerona** added to the brands row. It was missing from the first draft but he is
  trained on it.

## Things to confirm with Dáire

1. **Maintenance pricing.** The page deliberately has no price. His PDF has none either.
   If he wants a figure or a "from €X" it needs to come from him.
2. **Counties listed** on the coverage sections are an assumption. Trim or extend.
3. **Facebook URL.** Instagram is `@irish_airtowater`. The Facebook link currently points
   at Instagram as a placeholder.
4. **F-GAS certificate number.** Not on any document received. Worth displaying if he has it,
   since it is checkable and that is the whole point of the page.
5. **Business address.** Schema says Sligo with no street address. Fine if he works from
   home, but a full address helps local SEO if he is happy to publish it.

## SEO

Per-page titles and descriptions within length limits. Canonicals set. OpenGraph tags in
place, though `og:image` is not set until there is a real photo to point at.

JSON-LD on every page: `HVACBusiness` with services, credentials and area served, plus a
`FAQPage` block per page. That is what puts the FAQ accordions in the running for rich
results, so keep the questions and the visible text in sync if you edit either.

## Accessibility

Skip link, single h1 per page, `aria-current` on the active nav item, `aria-expanded` and
`aria-controls` on the nav toggle and every accordion, escape key closes the mobile nav,
visible focus rings, and `prefers-reduced-motion` respected.

Reveal-on-scroll only hides content when JS is running, via a `.js` class set inline in the
head. If the script fails or is blocked, the page still renders in full.
