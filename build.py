#!/usr/bin/env python3
"""Static site builder for Irish Air to Water. Emits plain HTML files."""

import os, json, pathlib, hashlib

OUT = pathlib.Path(__file__).parent
SITE = "https://irishairtowater.com"
PHONE_DISPLAY = "087 341 3114"
PHONE_TEL = "+353873413114"
PHONE_WA = "353873413114"
EMAIL = "irishairtowater@gmail.com"

NAV = [
    ("index.html", "Home"),
    ("services.html", "Services"),
    ("maintenance.html", "Maintenance Plan"),
    ("certifications.html", "Certifications"),
    ("contact.html", "Contact"),
]

ICON_PHONE = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>'

# Lucide icon paths, used as the faded watermark on service cards.
def _svg(paths):
    return ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
            'stroke-linecap="round" stroke-linejoin="round">' + paths + '</svg>')

ICON_WRENCH = _svg('<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>')
ICON_GAUGE = _svg('<path d="m12 14 4-4"/><path d="M3.34 19a10 10 0 1 1 17.32 0"/>')
ICON_SEARCH = _svg('<circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/>')
ICON_CALCHECK = _svg('<path d="M8 2v4"/><path d="M16 2v4"/><rect width="18" height="18" x="3" y="4" rx="2"/><path d="M3 10h18"/><path d="m9 16 2 2 4-4"/>')
ICON_SLIDERS = _svg('<line x1="21" x2="14" y1="4" y2="4"/><line x1="10" x2="3" y1="4" y2="4"/><line x1="21" x2="12" y1="12" y2="12"/><line x1="8" x2="3" y1="12" y2="12"/><line x1="21" x2="16" y1="20" y2="20"/><line x1="12" x2="3" y1="20" y2="20"/><line x1="14" x2="14" y1="2" y2="6"/><line x1="8" x2="8" y1="10" y2="14"/><line x1="16" x2="16" y1="18" y2="22"/>')
ICON_SNOW = _svg('<path d="m10 20-1.25-2.5L6 18"/><path d="M10 4 8.75 6.5 6 6"/><path d="m14 20 1.25-2.5L18 18"/><path d="m14 4 1.25 2.5L18 6"/><path d="m17 21-3-6h-4"/><path d="m17 3-3 6 1.5 3"/><path d="M2 12h6.5L10 9"/><path d="m20 10-1.5 2 1.5 2"/><path d="M22 12h-6.5L14 15"/><path d="m4 10 1.5 2L4 14"/><path d="m7 21 3-6-1.5-3"/><path d="m7 3 3 6h4"/>')

# One page per service. (file, nav/card label, card blurb, schema service name, icon)
SERVICE_PAGES = [
    ("installation.html", "Installation",
     "Domestic and commercial air-to-water systems, from siting and pipework through to handover.",
     "Air to water heat pump installation", ICON_WRENCH),
    ("commissioning.html", "Commissioning",
     "Correct setup from day one: checks, settings, optimisation, and clear handover.",
     "Air to water heat pump commissioning", ICON_GAUGE),
    ("repairs.html", "Service &amp; Repairs",
     "Fault finding, alarms, cycling issues, DHW temperature problems and performance optimisation.",
     "Air to water heat pump service and repairs", ICON_SEARCH),
    ("maintenance.html", "Aftersales Maintenance",
     "Planned annual servicing and callouts to keep systems running efficiently year-round.",
     "Heat pump aftersales maintenance", ICON_CALCHECK),
    ("hydraulic-balancing.html", "Hydraulic Balancing",
     "Uneven flow leaves one room warm and another cool. Balancing evens the flow out by circuit.",
     "Heating system hydraulic balancing", ICON_SLIDERS),
    ("air-conditioning.html", "Air Conditioning",
     "Domestic high wall units and commercial systems, including cassette, underceiling and multi-unit VRV/VRF.",
     "Air conditioning installation and service", ICON_SNOW),
]


def svc_cards(exclude=None, grid_cls="svc-grid"):
    """Grid of service cards. Pass a filename to leave that service out."""
    cards = ""
    for href, label, blurb, _name, icon in SERVICE_PAGES:
        if href == exclude:
            continue
        cards += (f'<a class="svc reveal" href="{href}">'
                  f'<div class="svc-watermark" aria-hidden="true">{icon}</div>'
                  f'<h3>{label}</h3><p>{blurb}</p></a>')
    return f'<div class="{grid_cls}">{cards}</div>'


def related_services(current):
    """Bottom-of-page strip linking every other service page."""
    links = "".join(
        f'<a href="{href}">{label}</a>'
        for href, label, _b, _n, _i in SERVICE_PAGES if href != current
    )
    return f"""<section class="bg-white sec-tight">
  <div class="wrap">
    <div class="sec-head reveal"><h2>Other services.</h2></div>
    <div class="related-row reveal">{links}</div>
  </div>
</section>"""


def crumbs(trail):
    """trail: list of (href|None, label). Last item is the current page."""
    items = ""
    for href, label in trail:
        items += f'<li><a href="{href}">{label}</a></li>' if href else f"<li>{label}</li>"
    return f'<ul class="crumbs">{items}</ul>'


def breadcrumb_schema(trail):
    out = []
    for i, (href, label) in enumerate(trail, 1):
        entry = {"@type": "ListItem", "position": i, "name": label}
        if href:
            url = f"{SITE}/" if href == "index.html" else f"{SITE}/{href[:-5]}"
            entry["item"] = url
        out.append(entry)
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": out}


def service_schema(name, description, filename, service_type=None):
    return {
        "@context": "https://schema.org",
        "@type": "Service",
        "name": name,
        "description": description,
        "serviceType": service_type or name,
        "url": f"{SITE}/{filename[:-5]}",
        "provider": {"@id": f"{SITE}/#business"},
        "areaServed": {"@type": "Country", "name": "Ireland"},
        "audience": {"@type": "Audience", "audienceType": "Domestic and commercial"},
    }
ICON_MAIL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/></svg>'
ICON_INSTA = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="20" height="20" x="2" y="2" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="0.5" fill="currentColor"/></svg>'
ICON_PIN = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 10c0 4.993-5.539 10.193-7.399 11.799a1 1 0 0 1-1.202 0C9.539 20.193 4 14.993 4 10a8 8 0 0 1 16 0"/><circle cx="12" cy="10" r="3"/></svg>'
TICK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg>'
PLUS = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14M5 12h14"/></svg>'
ICON_WA = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51a12.8 12.8 0 0 0-.57-.01c-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884a9.82 9.82 0 0 1 6.988 2.896 9.82 9.82 0 0 1 2.893 6.994c-.003 5.45-4.437 9.885-9.885 9.885M20.52 3.449C18.24 1.245 15.24 0 12.045 0 5.463 0 .104 5.334.101 11.893c0 2.096.549 4.142 1.595 5.945L0 24l6.335-1.652a12 12 0 0 0 5.71 1.447h.006c6.585 0 11.946-5.335 11.949-11.896 0-3.176-1.24-6.165-3.495-8.411"/></svg>'


# Where the enquiry forms post. None keeps the in-page placeholder handler.
# Set to a Formspree endpoint ("https://formspree.io/f/xxxxxxxx") to go live.
FORM_ACTION = None


def pic(src, alt, w, h, eager=False, img_cls=""):
    """<picture> with a WebP source and the original JPEG as fallback.
    A .webp sibling is emitted by the image pass; if none exists, plain <img>."""
    load = 'loading="eager" fetchpriority="high"' if eager else 'loading="lazy"'
    cls = f' class="{img_cls}"' if img_cls else ""
    fallback = (f'<img{cls} src="images/{src}" alt="{alt}" '
                f'width="{w}" height="{h}" {load} decoding="async">')
    webp = pathlib.Path(src).with_suffix(".webp")
    if not (OUT / "images" / webp).exists():
        return fallback
    return f'<picture><source srcset="images/{webp}" type="image/webp">{fallback}</picture>'


def img(src, alt, w, h, eager=False, cls=""):
    """Photo in a cropping frame. All supplied photos are 3:4 portrait."""
    extra = f" {cls}" if cls else ""
    return f'<div class="media-frame{extra}">{pic(src, alt, w, h, eager, "media-img")}</div>'


CURRENT_ATTR = ' aria-current="page"' 


def header(current, title_lines=None):
    links = "".join(
        '<li><a href="%s"%s>%s</a></li>' % (href, CURRENT_ATTR if href == current else "", label)
        for href, label in NAV[1:]
    )
    mob = "".join(
        '<li><a href="%s"%s>%s</a></li>' % (href, CURRENT_ATTR if href == current else "", label)
        for href, label in NAV
    )
    return f"""<a class="skip-link" href="#main">Skip to content</a>
<header>
  <div class="wrap nav">
    <a class="brand" href="index.html">
      <img class="brand-logo-img" src="images/logo-mark.png" alt="" width="44" height="44">
      <div class="brand-name">Irish Air to Water<small>Heat Pump Services</small></div>
    </a>
    <ul class="nav-links">{links}</ul>
    <div class="nav-cta">
      <a class="btn btn-ghost" href="contact.html">Request a callback</a>
      <a class="btn btn-amber nav-call" href="tel:{PHONE_TEL}" aria-label="Call {PHONE_DISPLAY}">{ICON_PHONE}<span>{PHONE_DISPLAY}</span></a>
      <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="mobile-panel" aria-label="Menu">
        <span></span><span></span><span></span>
      </button>
    </div>
  </div>
  <div class="mobile-panel" id="mobile-panel">
    <ul>{mob}</ul>
    <div class="mobile-actions">
      <a class="btn btn-amber" href="tel:{PHONE_TEL}">{ICON_PHONE}Call {PHONE_DISPLAY}</a>
      <a class="btn btn-ghost" href="contact.html">Request a callback</a>
    </div>
  </div>
</header>"""


FOOTER = f"""<footer>
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <div class="foot-logo"><img src="images/logo.png" alt="Irish Air to Water, Heat Pump Services" width="729" height="674" loading="lazy" decoding="async"></div>
        <p>Heat pump installation, commissioning, service and aftersales maintenance. F-GAS registered, Sligo-based, covering all of Ireland.</p>
      </div>
      <div>
        <h4>Services</h4>
        <ul>
          <li><a href="installation.html">Installation</a></li>
          <li><a href="commissioning.html">Commissioning</a></li>
          <li><a href="repairs.html">Service &amp; repairs</a></li>
          <li><a href="maintenance.html">Aftersales maintenance</a></li>
          <li><a href="hydraulic-balancing.html">Hydraulic balancing</a></li>
          <li><a href="air-conditioning.html">Air conditioning</a></li>
        </ul>
      </div>
      <div>
        <h4>Company</h4>
        <ul>
          <li><a href="services.html">All services</a></li>
          <li><a href="certifications.html">Certifications</a></li>
          <li><a href="reviews.html">Reviews</a></li>
          <li><a href="faq.html">FAQ</a></li>
          <li><a href="index.html#coverage">Coverage</a></li>
          <li><a href="contact.html">Contact</a></li>
        </ul>
      </div>
      <div>
        <h4>Get in touch</h4>
        <ul>
          <li><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li><a href="https://wa.me/{PHONE_WA}" target="_blank" rel="noopener">WhatsApp</a></li>
          <li><a href="https://www.instagram.com/irish_airtowater" target="_blank" rel="noopener">Instagram</a></li>
        </ul>
      </div>
    </div>
    <div class="foot-bottom">
      <div>&copy; 2026 Irish Air to Water. Proprietor: D&aacute;ire Cullinane. Sligo, Ireland. <a href="privacy.html">Privacy</a></div>
      <div>Site by <a href="https://squaretwo.ie" target="_blank" rel="noopener" style="text-decoration:none">SquareTwo</a></div>
    </div>
  </div>
</footer>
<a class="wa-float" href="https://wa.me/{PHONE_WA}" target="_blank" rel="noopener" aria-label="Message us on WhatsApp">{ICON_WA}</a>
<nav class="call-bar" aria-label="Call or message">
  <a href="tel:{PHONE_TEL}">{ICON_PHONE}Call {PHONE_DISPLAY}</a>
  <a class="call-bar-wa" href="https://wa.me/{PHONE_WA}" target="_blank" rel="noopener">{ICON_WA}WhatsApp</a>
</nav>
<script src="assets/main.js?v=__MAINJS_V__"></script>"""


CTA_BAND = f"""<section class="cta-band">
  <div class="wrap cta-inner">
    <div>
      <h2>Talk to us about your system.</h2>
      <p>Call, WhatsApp, email or send the form.</p>
    </div>
    <div class="cta-actions">
      <a class="btn btn-amber" href="tel:{PHONE_TEL}">{ICON_PHONE}{PHONE_DISPLAY}</a>
      <a class="btn btn-ghost-light" href="contact.html">Request a callback</a>
    </div>
  </div>
</section>"""


LOCAL_BUSINESS = {
    "@context": "https://schema.org",
    "@type": "HVACBusiness",
    "@id": f"{SITE}/#business",
    "name": "Irish Air to Water",
    "description": "Air-to-water heat pump specialist and air conditioning installer. Commissioning, service and repairs, aftersales maintenance, and domestic and commercial air conditioning. F-GAS registered, Sligo-based, covering all of Ireland.",
    "url": SITE,
    "telephone": "+353 87 341 3114",
    "email": EMAIL,
    "founder": {"@type": "Person", "name": "Dáire Cullinane", "jobTitle": "Proprietor"},
    "address": {"@type": "PostalAddress", "addressLocality": "Sligo", "addressRegion": "County Sligo", "addressCountry": "IE"},
    "areaServed": {"@type": "Country", "name": "Ireland"},
    "sameAs": ["https://www.instagram.com/irish_airtowater"],
    "knowsAbout": ["Air to water heat pumps", "F-Gas refrigerant handling", "Heat pump commissioning",
                   "Hydraulic balancing", "R290 propane heat pumps", "Air conditioning installation",
                   "Cassette and underceiling air conditioning", "VRV and VRF systems"],
    "makesOffer": [
        {"@type": "Offer", "itemOffered": {"@type": "Service", "name": n}}
        for n in ["Heat pump installation", "Heat pump commissioning", "Heat pump service and repairs",
                  "Aftersales maintenance", "Annual maintenance visit", "Hydraulic balancing",
                  "Domestic air conditioning installation and service",
                  "Commercial air conditioning installation and service",
                  "VRV and VRF multi-unit air conditioning systems"]
    ],
    "hasCredential": [
        {"@type": "EducationalOccupationalCredential", "name": "F-Gas Registered"},
        {"@type": "EducationalOccupationalCredential", "name": "QQI Level 6 Advanced Certificate, Craft - Refrigeration and Air Conditioning"},
        {"@type": "EducationalOccupationalCredential", "name": "Grant Aerona R290 Air Source Heat Pump Course"},
    ],
}


def _asset_v(relpath):
    """Short content hash so long-cached assets bust on change."""
    return hashlib.md5((OUT / relpath).read_bytes()).hexdigest()[:8]


def page(filename, title, description, body, extra_schema=None, og_type="website", head_extra=""):
    schema = [LOCAL_BUSINESS]
    if extra_schema:
        schema.extend(extra_schema if isinstance(extra_schema, list) else [extra_schema])
    schema_tags = "\n".join(
        f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>' for s in schema
    )
    # Vercel cleanUrls is on, so the served URL has no .html extension.
    canonical = f"{SITE}/" if filename == "index.html" else f"{SITE}/{filename[:-5]}"
    html_footer_v = _asset_v("assets/main.js")
    html = f"""<!DOCTYPE html>
<html lang="en-IE">
<head>
<script>document.documentElement.className+=' js';</script>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="Irish Air to Water">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical}">
<meta property="og:locale" content="en_IE">
<meta property="og:image" content="{SITE}/images/og-image.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Air-to-water heat pump outdoor unit installed by Irish Air to Water">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0d2620">
<link rel="icon" href="images/logo-mark.png" type="image/png">
<link rel="apple-touch-icon" href="images/logo-mark.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@400;500;600;700&family=Outfit:wght@300;400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/styles.css?v={_asset_v('assets/styles.css')}">
{head_extra}{schema_tags}
</head>
<body>
{header(filename)}
<main id="main">
{body}
</main>
{FOOTER}
</body>
</html>
"""
    html = html.replace("__MAINJS_V__", html_footer_v)
    (OUT / filename).write_text(html, encoding="utf-8")
    print("wrote", filename)


def sitemap(entries):
    """entries: list of (filename, priority). Written to match cleanUrls output."""
    import datetime
    today = datetime.date.today().isoformat()
    rows = ""
    for filename, priority in entries:
        loc = f"{SITE}/" if filename == "index.html" else f"{SITE}/{filename[:-5]}"
        rows += (f"  <url>\n    <loc>{loc}</loc>\n"
                 f"    <lastmod>{today}</lastmod>\n"
                 f"    <priority>{priority}</priority>\n  </url>\n")
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
           f"{rows}</urlset>\n")
    (OUT / "sitemap.xml").write_text(xml, encoding="utf-8")
    print("wrote sitemap.xml")


def faq_block(items, start=1):
    out = ['<div class="faq">']
    for i, (q, a) in enumerate(items, start):
        answers = "".join(f"<p>{p}</p>" for p in a)
        out.append(f"""<div class="faq-item">
  <h3><button class="faq-q" type="button" aria-expanded="false" aria-controls="faq-a-{i}" id="faq-q-{i}">{q}</button></h3>
  <div class="faq-a" id="faq-a-{i}" role="region" aria-labelledby="faq-q-{i}">{answers}</div>
</div>""")
    out.append("</div>")
    return "\n".join(out)


def faq_schema(items):
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": " ".join(a)}}
            for q, a in items
        ],
    }
