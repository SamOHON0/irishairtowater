#!/usr/bin/env python3
"""Static site builder for Irish Air to Water. Emits plain HTML files."""

import os, json, pathlib

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
ICON_MAIL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/></svg>'
ICON_INSTA = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="20" height="20" x="2" y="2" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="0.5" fill="currentColor"/></svg>'
ICON_PIN = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 10c0 4.993-5.539 10.193-7.399 11.799a1 1 0 0 1-1.202 0C9.539 20.193 4 14.993 4 10a8 8 0 0 1 16 0"/><circle cx="12" cy="10" r="3"/></svg>'
TICK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg>'
PLUS = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14M5 12h14"/></svg>'
ICON_WA = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51a12.8 12.8 0 0 0-.57-.01c-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884a9.82 9.82 0 0 1 6.988 2.896 9.82 9.82 0 0 1 2.893 6.994c-.003 5.45-4.437 9.885-9.885 9.885M20.52 3.449C18.24 1.245 15.24 0 12.045 0 5.463 0 .104 5.334.101 11.893c0 2.096.549 4.142 1.595 5.945L0 24l6.335-1.652a12 12 0 0 0 5.71 1.447h.006c6.585 0 11.946-5.335 11.949-11.896 0-3.176-1.24-6.165-3.495-8.411"/></svg>'


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
      <div class="brand-logo">LOGO</div>
      <div class="brand-name">Irish Air to Water<small>Heat Pump Specialists</small></div>
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
        <div class="foot-brand">Irish Air to Water</div>
        <p>Heat pump installation, commissioning, service and aftersales maintenance. F-GAS registered, Sligo-based, covering all of Ireland.</p>
      </div>
      <div>
        <h4>Services</h4>
        <ul>
          <li><a href="services.html#installation">Installation</a></li>
          <li><a href="services.html#commissioning">Commissioning</a></li>
          <li><a href="services.html#repairs">Service &amp; repairs</a></li>
          <li><a href="services.html#aftersales">Aftersales maintenance</a></li>
          <li><a href="services.html#balancing">Hydraulic balancing</a></li>
        </ul>
      </div>
      <div>
        <h4>Company</h4>
        <ul>
          <li><a href="maintenance.html">Annual maintenance plan</a></li>
          <li><a href="certifications.html">Certifications</a></li>
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
      <div>&copy; 2026 Irish Air to Water. Proprietor: D&aacute;ire Cullinane. Sligo, Ireland.</div>
      <div>Site by <a href="https://squaretwo.ie" target="_blank" rel="noopener" style="text-decoration:none">SquareTwo</a></div>
    </div>
  </div>
</footer>
<a class="wa-float" href="https://wa.me/{PHONE_WA}" target="_blank" rel="noopener" aria-label="Message us on WhatsApp">{ICON_WA}</a>
<script src="assets/main.js"></script>"""


CTA_BAND = f"""<section class="cta-band">
  <div class="wrap cta-inner">
    <div>
      <h2>Talk to us about your heat pump.</h2>
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
    "description": "Air-to-water heat pump specialist. Installation, commissioning, service and repairs, and aftersales maintenance. F-GAS registered, Sligo-based, covering all of Ireland.",
    "url": SITE,
    "telephone": "+353 87 341 3114",
    "email": EMAIL,
    "founder": {"@type": "Person", "name": "Dáire Cullinane", "jobTitle": "Proprietor"},
    "address": {"@type": "PostalAddress", "addressLocality": "Sligo", "addressRegion": "County Sligo", "addressCountry": "IE"},
    "areaServed": {"@type": "Country", "name": "Ireland"},
    "sameAs": ["https://www.instagram.com/irish_airtowater"],
    "knowsAbout": ["Air to water heat pumps", "F-Gas refrigerant handling", "Heat pump commissioning", "Hydraulic balancing", "R290 propane heat pumps"],
    "makesOffer": [
        {"@type": "Offer", "itemOffered": {"@type": "Service", "name": n}}
        for n in ["Heat pump installation", "Heat pump commissioning", "Heat pump service and repairs", "Aftersales maintenance", "Annual maintenance visit", "Hydraulic balancing"]
    ],
    "hasCredential": [
        {"@type": "EducationalOccupationalCredential", "name": "F-Gas Registered"},
        {"@type": "EducationalOccupationalCredential", "name": "QQI Level 6 Advanced Certificate, Craft - Refrigeration and Air Conditioning"},
        {"@type": "EducationalOccupationalCredential", "name": "Grant Aerona R290 Air Source Heat Pump Course"},
    ],
}


def page(filename, title, description, body, extra_schema=None, og_type="website"):
    schema = [LOCAL_BUSINESS]
    if extra_schema:
        schema.extend(extra_schema if isinstance(extra_schema, list) else [extra_schema])
    schema_tags = "\n".join(
        f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>' for s in schema
    )
    # Vercel cleanUrls is on, so the served URL has no .html extension.
    canonical = f"{SITE}/" if filename == "index.html" else f"{SITE}/{filename[:-5]}"
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
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0d2620">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@400;500;600;700&family=Outfit:wght@300;400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/styles.css">
{schema_tags}
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
    (OUT / filename).write_text(html, encoding="utf-8")
    print("wrote", filename)


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
