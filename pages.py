#!/usr/bin/env python3
"""Page bodies for Irish Air to Water.

COPY POLICY — first draft.
Every line on this site traces to one of four sources:
  1. irishairtowater.com (his live site)
  2. Annual_Maintenance_Customer_Info.pdf
  3. Irish_Air_to_Water_Safety_Statement_v2.pdf
  4. His certificates, or his own email signature
Where his site has wording, that wording is used as-is. Nothing is invented,
no pricing or turnaround promises are made, and no claims are made about his
process that a document does not support.
"""

from build import (
    page, faq_block, faq_schema, CTA_BAND, SITE, img,
    PHONE_DISPLAY, PHONE_TEL, PHONE_WA, EMAIL,
    ICON_PHONE, ICON_MAIL, ICON_INSTA, ICON_PIN, TICK, PLUS,
    SERVICE_PAGES, svc_cards, related_services, crumbs,
    breadcrumb_schema, service_schema, sitemap, pic, FORM_ACTION,
)

SERVICES_TRAIL = [("index.html", "Home"), ("services.html", "Services")]


def svc_trail(label):
    return SERVICES_TRAIL + [(None, label)]

# His site and his Safety Statement both list these five. Grant is a training
# certificate, not a brand he advertises, so it stays on the certifications page.
BRANDS = ["MasterTherm", "Mitsubishi Electric", "Mitsubishi Heavy Industries", "Panasonic", "Samsung"]
BRANDS_ROW = "".join(f'<span class="brand-mark">{b}</span>' for b in BRANDS)

CONTACT_LIST = f"""<ul class="contact-list">
  <li>
    <div class="c-icon">{ICON_PHONE}</div>
    <div><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a><small>Phone and WhatsApp</small></div>
  </li>
  <li>
    <div class="c-icon">{ICON_MAIL}</div>
    <div><a href="mailto:{EMAIL}">{EMAIL}</a><small>Email us any time</small></div>
  </li>
  <li>
    <div class="c-icon">{ICON_INSTA}</div>
    <div><a href="https://www.instagram.com/irish_airtowater" target="_blank" rel="noopener">@irish_airtowater</a><small>Instagram and Facebook</small></div>
  </li>
  <li>
    <div class="c-icon">{ICON_PIN}</div>
    <div><a href="index.html#coverage">Sligo-based, all of Ireland</a><small>Domestic and commercial</small></div>
  </li>
</ul>"""


def form_card(heading, sub, submit_label="Send enquiry"):
    sub_html = f'\n  <p class="form-sub">{sub}</p>' if sub else ""
    action = f' action="{FORM_ACTION}" method="POST"' if FORM_ACTION else ""
    return f"""<div class="form-card reveal">
  <h3>{heading}</h3>{sub_html}
  <form data-iatw-form{action}>
    <div class="hp" aria-hidden="true"><label for="f-website">Website</label><input id="f-website" type="text" name="website" tabindex="-1" autocomplete="off"></div>
    <div class="field-row">
      <div class="field">
        <label for="f-name">Name</label>
        <input id="f-name" type="text" name="name" autocomplete="name" required>
      </div>
      <div class="field">
        <label for="f-phone">Phone</label>
        <input id="f-phone" type="tel" name="phone" autocomplete="tel" required>
      </div>
    </div>
    <div class="field">
      <label for="f-county">County</label>
      <input id="f-county" type="text" name="county">
    </div>
    <div class="field">
      <label for="f-brand">Heat pump brand / model</label>
      <input id="f-brand" type="text" name="brand">
    </div>
    <div class="field">
      <label for="f-type">What do you need?</label>
      <select id="f-type" name="type">
        <option>Commissioning</option>
        <option>Service or repair</option>
        <option>Aftersales maintenance</option>
        <option>Installation</option>
        <option>Air conditioning</option>
        <option>Something else</option>
      </select>
    </div>
    <button class="btn btn-amber" type="submit" style="width:100%; justify-content:center;">{submit_label}</button>
  </form>
</div>"""


# His site's exact five common issues, verbatim.
PROBLEMS = [
    "High electricity bills / low efficiency",
    "Heat pump cycling on/off",
    "DHW not reaching temperature",
    "Cold rooms / poor heat output",
    "Noise, alarms, or frequent defrost",
]
PROB_BLOCKS = "".join(f"<li>{TICK}{h}</li>" for h in PROBLEMS)


# Air conditioning. Scope wording is Dáire's own, relayed 2 Sep: high wall domestic
# units, and commercial systems including cassette underceiling and multi-unit VRV/VRF.
# His QQI Level 6 is in Refrigeration and Air Conditioning, so the credentials carry over.
AC_DOMESTIC = [
    "High wall units for homes",
    "Installation and service",
    "F-Gas certified refrigerant work",
]
AC_COMMERCIAL = [
    "Cassette and underceiling units",
    "Multi-unit VRV / VRF systems",
    "Installation and service",
]
AC_DOM_LI = "".join(f"<li>{TICK}{x}</li>" for x in AC_DOMESTIC)
AC_COM_LI = "".join(f"<li>{TICK}{x}</li>" for x in AC_COMMERCIAL)

COVERAGE_BLOCK = f"""<div class="coverage reveal">
  <h2>Sligo-based. Covering all of Ireland.</h2>
  <p>Air-to-water heat pump work across Ireland, for domestic and commercial systems.</p>
  <ul class="tick-list">
    <li>{TICK}Based in Sligo</li>
    <li>{TICK}Covering all of Ireland</li>
    <li>{TICK}Domestic and commercial</li>
  </ul>
</div>"""


# ============================================================ HOME
# Section order and copy mirror irishairtowater.com. His wording is verbatim
# except em dashes (house rule: none) and bullet separators.
HOME = f"""
<section class="hero hero-bleed hero-light">
  <video class="bleed-video" autoplay muted loop playsinline preload="metadata" poster="media/brand-intro-poster.jpg" aria-hidden="true" tabindex="-1">
    <source src="media/brand-intro.mp4" type="video/mp4">
  </video>
  <div class="bleed-scrim" aria-hidden="true"></div>
  <div class="wrap bleed-content">
    <h1>Air-to-Water Heat Pump Specialist, Ireland-wide.</h1>
    <p class="lede">Sligo-based, providing nationwide coverage across Ireland for air-to-water heat pump commissioning, servicing, repairs, and aftersales maintenance. Domestic and commercial systems supported.</p>
    <div class="hero-ctas">
      <a class="btn btn-amber" href="tel:{PHONE_TEL}">{ICON_PHONE}Call {PHONE_DISPLAY}</a>
      <a class="btn btn-ghost" href="https://wa.me/{PHONE_WA}" target="_blank" rel="noopener">WhatsApp</a>
    </div>
  </div>
</section>

<div class="trust">
  <div class="wrap trust-row">
    <span>F-GAS Registered</span>
    <span>QQI Level 6 Refrigeration &amp; Air Conditioning</span>
    <span>R290 Heat Pump Trained</span>
    <span>Sligo-based, covering all of Ireland</span>
  </div>
</div>

<section id="services" class="sec-tight">
  <div class="wrap">
    {svc_cards()}
  </div>
</section>

<section class="bg-white">
  <div class="wrap">
    <div class="sec-head reveal">
      <h2>Services.</h2>
      <p>Air-to-water heat pumps. Domestic and commercial.</p>
    </div>
    <ul class="tick-list issues-list reveal">
      <li>{TICK}Installation of domestic and commercial systems</li>
      <li>{TICK}Commissioning &amp; setup (controls, temperatures, checks)</li>
      <li>{TICK}Performance optimisation &amp; troubleshooting</li>
      <li>{TICK}Routine / planned maintenance</li>
      <li>{TICK}Repairs &amp; fault finding (alarms, cycling, low performance)</li>
      <li>{TICK}Hydraulic balancing</li>
      <li>{TICK}Clear reporting &amp; recommendations</li>
      <li>{TICK}Air conditioning: domestic and commercial installation &amp; service</li>
    </ul>
    <div style="margin-top:30px"><a class="btn btn-ghost" href="services.html">See all services</a></div>
  </div>
</section>

<section class="bg-pine">
  <div class="wrap">
    <div class="sec-head reveal">
      <h2>Common callouts.</h2>
      <p>If you're seeing any of these, they're usually fixable with the right checks.</p>
    </div>
    <ul class="tick-list issues-list reveal">{PROB_BLOCKS}</ul>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head reveal">
      <h2>Recent work.</h2>
    </div>
    <div class="gallery-grid reveal">
      <div class="g-item g-tall">{pic("coverage-home-install.jpg", "Finished Panasonic air-to-water heat pump installation", 750, 1000)}</div>
      <div class="g-item">{pic("services-commissioning-controls.jpg", "Heat pump control board during commissioning", 750, 1000)}</div>
      <div class="g-item">{pic("services-aftersales-filters.jpg", "Air filters removed for cleaning on a service visit", 750, 1000)}</div>
      <div class="g-item g-tall">{pic("certifications-at-work.jpg", "A large system strainer removed for cleaning on a commercial installation", 750, 1000)}</div>
      <div class="g-item">{pic("services-installation.jpg", "Wall-mounted heat pump unit with pipework", 562, 1000)}</div>
      <div class="g-item">{pic("maintenance-clear-access.jpg", "Outdoor heat pump unit sited with clear space around it", 750, 1000)}</div>
    </div>
  </div>
</section>

<section class="bg-white">
  <div class="wrap">
    <div class="sec-head reveal">
      <h2>What our customers say.</h2>
      <p>From the Irish Air to Water Facebook page.</p>
    </div>
    <div class="reviews-grid">
      <div class="review review-lead reveal">
        <blockquote>&ldquo;He was absolutely fantastic from start to finish. He explained everything clearly, was very professional, and his pricing was extremely reasonable. It&rsquo;s such a relief to find someone so reliable, honest, and helpful.&rdquo;</blockquote>
        <div class="review-who">Stephanie Callaghan<small>Facebook review</small></div>
      </div>
      <div class="review reveal">
        <blockquote>&ldquo;Absolutely 10/10 service. Knew what the problem was straight away and got it sorted. I&rsquo;ve had 5 people come to look at the problem and only he knew. Recommend 100%.&rdquo;</blockquote>
        <div class="review-who">Shawana Moriarty<small>Facebook review</small></div>
      </div>
      <div class="review reveal">
        <blockquote>&ldquo;We have been having extremely high bills because of our heat pump and no knowledge as to why. Since he has looked at it, our usage on the pump has come down and our bills reduced.&rdquo;</blockquote>
        <div class="review-who">Rebecca Fabozzi<small>Facebook review</small></div>
      </div>
      <div class="review-video reveal">
        <video controls playsinline preload="none" poster="media/customer-reviews-poster.jpg" aria-label="More customer reviews from the Irish Air to Water Facebook page">
          <source src="media/customer-reviews.mp4" type="video/mp4">
        </video>
      </div>
    </div>
    <div style="margin-top:30px"><a class="btn btn-ghost" href="reviews.html">Read all reviews</a></div>
  </div>
</section>

<section id="coverage" class="coverage-band" style="padding:64px 0">
  <div class="wrap coverage-band-inner">
    <div class="reveal">
      <h2>Coverage.</h2>
      <p style="max-width:62ch">Based in Sligo and covering all of Ireland for air-to-water heat pump commissioning, servicing, repairs and aftersales maintenance. Domestic and commercial work welcome. Travel nationwide.</p>
    </div>
    <ul class="tick-list reveal">
      <li>{TICK}Sligo base</li>
      <li>{TICK}Ireland-wide</li>
      <li>{TICK}Domestic &amp; commercial</li>
    </ul>
  </div>
</section>

<section class="sec-tight" id="brands">
  <div class="wrap">
    <div class="sec-head reveal">
      <h2>Heat pump brands supported.</h2>
      <p>Experience commissioning, servicing and maintaining a wide range of domestic and commercial air-to-water systems.</p>
    </div>
    <div class="brands-row reveal">{BRANDS_ROW}</div>
  </div>
</section>

<section id="contact" class="contact">
  <div class="wrap contact-grid">
    <div class="reveal">
      <h2>Contact.</h2>
      <p class="contact-lede">Fastest way to book:</p>
      {CONTACT_LIST}
      <p style="color:rgba(244,243,238,0.7);font-size:0.92rem;margin-top:28px;max-width:48ch">Tip: include your county, system brand/model, and whether it's commissioning or service/maintenance. If there's an alarm, include the code/photo.</p>
    </div>
    {form_card("Send an enquiry", "")}
  </div>
</section>
"""


# ============================================================ SERVICES HUB
# One page per service. This page is the index; each card is its own page.
BRANDS_BAND = f"""<section class="bg-white sec-tight">
  <div class="wrap">
    <div class="sec-head reveal">
      <h2>Brands we work with.</h2>
    </div>
    <div class="brands-row reveal">{BRANDS_ROW}</div>
  </div>
</section>"""

SAFE_NOTE = ('<p style="font-size:0.9rem">Work on refrigerant circuits is carried out only by '
             'F-Gas certified personnel, using certified recovery equipment. Refrigerant is never '
             'vented to atmosphere.</p>')

ENQUIRY_TIP = f"""<section class="bg-pine sec-tight">
  <div class="wrap">
    <div class="sec-head reveal">
      <h2>Before you call.</h2>
      <p>Three things that let us tell you more on the phone.</p>
    </div>
    <ul class="tick-list issues-list reveal">
      <li>{TICK}Your county</li>
      <li>{TICK}The system brand and model</li>
      <li>{TICK}Any alarm code, or a photo of the display</li>
    </ul>
  </div>
</section>"""

ARROW = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" '
         'stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/>'
         '<path d="m12 5 7 7-7 7"/></svg>')


def more_link(href, label):
    """Keyword-anchored link from a services.html block to its own page."""
    return f'<a class="more-link" href="{href}">{label}{ARROW}</a>'


# Layout is the original stacked one. Each block now heads to its own page.
SERVICES = f"""
<section class="page-hero">
  <div class="wrap">
    <h1>Heat pump and air conditioning services.</h1>
    <p>Installation, commissioning, service and repairs, aftersales maintenance, hydraulic balancing and air conditioning. Domestic and commercial systems, Sligo-based, covering all of Ireland.</p>
    {crumbs([("index.html", "Home"), (None, "Services")])}
  </div>
</section>

<section>
  <div class="wrap">

    <div class="svc-detail reveal" id="installation">
      <div class="svc-detail-media"><a href="installation.html" tabindex="-1" aria-hidden="true">{img("services-installation.jpg", "Wall-mounted heat pump unit with pipework run down the wall", 562, 1000)}</a></div>
      <div>
        <h2><a href="installation.html">Installation</a></h2>
        <p>Installation of domestic and commercial air-to-water heat pump systems, through to commissioning and handover.</p>
        <ul class="tick-list">
          <li>{TICK}Siting and mounting of outdoor and indoor units</li>
          <li>{TICK}Refrigerant pipework: brazing, pressure testing, evacuation and charging</li>
          <li>{TICK}Hot water cylinder installation</li>
          <li>{TICK}First-fix and second-fix pipework and electrical connections</li>
          <li>{TICK}System handover</li>
        </ul>
        {more_link("installation.html", "Heat pump installation")}
      </div>
    </div>

    <div class="svc-detail flip reveal" id="commissioning">
      <div class="svc-detail-media"><a href="commissioning.html" tabindex="-1" aria-hidden="true">{img("services-commissioning-controls.jpg", "Heat pump control board and wiring inside an opened control panel", 750, 1000)}</a></div>
      <div>
        <h2><a href="commissioning.html">Commissioning</a></h2>
        <p>Correct setup from day one: checks, settings, optimisation, and clear handover.</p>
        <ul class="tick-list">
          <li>{TICK}System checks against manufacturer specification</li>
          <li>{TICK}Settings and controls configured</li>
          <li>{TICK}Optimisation of system performance</li>
          <li>{TICK}Clear handover so you understand your controls</li>
        </ul>
        {more_link("commissioning.html", "Heat pump commissioning")}
      </div>
    </div>

    <div class="svc-detail reveal" id="repairs">
      <div class="svc-detail-media"><a href="repairs.html" tabindex="-1" aria-hidden="true">{img("services-repairs-strainer-check.jpg", "A system strainer checked in hand during a service call", 937, 1000)}</a></div>
      <div>
        <h2><a href="repairs.html">Service &amp; repairs</a></h2>
        <p>Fault finding, alarms, cycling issues, DHW temperature problems and performance optimisation.</p>
        <ul class="tick-list">
          <li>{TICK}Fault finding and diagnostics</li>
          <li>{TICK}Alarms and lockouts</li>
          <li>{TICK}Cycling issues</li>
          <li>{TICK}DHW temperature problems</li>
          <li>{TICK}Performance optimisation</li>
        </ul>
        {SAFE_NOTE}
        {more_link("repairs.html", "Heat pump service &amp; repairs")}
      </div>
    </div>

    <div class="svc-detail flip reveal" id="aftersales">
      <div class="svc-detail-media"><a href="maintenance.html" tabindex="-1" aria-hidden="true">{img("services-aftersales-filters.jpg", "Air filters removed and laid out for cleaning during a service visit", 750, 1000)}</a></div>
      <div>
        <h2><a href="maintenance.html">Aftersales maintenance</a></h2>
        <p>Planned servicing and callouts to keep systems running efficiently year-round.</p>
        <ul class="tick-list">
          <li>{TICK}Annual maintenance visit, carried out by an F-Gas certified engineer</li>
          <li>{TICK}F-Gas leak check, recorded as required under F-Gas Regulations</li>
          <li>{TICK}Written service record of what was checked and any issues found</li>
          <li>{TICK}Callouts between scheduled visits</li>
        </ul>
        {more_link("maintenance.html", "Annual maintenance visit")}
      </div>
    </div>

    <div class="svc-detail reveal" id="balancing">
      <div class="svc-detail-media"><a href="hydraulic-balancing.html" tabindex="-1" aria-hidden="true">{img("services-balancing-manifold.jpg", "Heating manifold with flow meters, from our hydraulic balancing explainer", 1000, 514, cls="frame-landscape")}</a></div>
      <div>
        <h2><a href="hydraulic-balancing.html">Hydraulic balancing</a></h2>
        <p>Sometimes the heat source is not the problem. Short loops get too much flow and long loops get too little, so one room runs warm while another sits cool.</p>
        <ul class="tick-list">
          <li>{TICK}Uneven flow distribution identified</li>
          <li>{TICK}Flow meter adjusted by circuit</li>
          <li>{TICK}More even room temperatures</li>
        </ul>
        {more_link("hydraulic-balancing.html", "Hydraulic balancing")}
      </div>
    </div>

    <div class="svc-detail-full reveal" id="air-conditioning">
      <h2><a href="air-conditioning.html">Air conditioning</a></h2>
      <p>Installation and service of domestic and commercial air conditioning, alongside our heat pump work. Same F-GAS certified refrigerant handling, and a QQI Level 6 Advanced Certificate in Refrigeration and Air Conditioning behind it.</p>
      <div class="split-cols" style="margin-top:34px">
        <div class="panel">
          <h3>Domestic</h3>
          <ul class="tick-list">{AC_DOM_LI}</ul>
        </div>
        <div class="panel">
          <h3>Commercial</h3>
          <ul class="tick-list">{AC_COM_LI}</ul>
        </div>
      </div>
      <div style="margin-top:28px">{more_link("air-conditioning.html", "Air conditioning installation &amp; service")}</div>
    </div>

  </div>
</section>

{BRANDS_BAND}

{CTA_BAND}
"""


# ============================================================ INSTALLATION
INSTALLATION = f"""
<section class="page-hero">
  <div class="wrap">
    <h1>Air-to-water heat pump installation.</h1>
    <p>Installation of domestic and commercial air-to-water heat pump systems, through to commissioning and handover.</p>
    {crumbs(svc_trail("Installation"))}
  </div>
</section>

<section>
  <div class="wrap">
    <div class="svc-detail reveal">
      <div class="svc-detail-media">{img("services-installation.jpg", "Wall-mounted heat pump unit with pipework run down the wall", 562, 1000, eager=True)}</div>
      <div>
        <h2>What the work covers.</h2>
        <ul class="tick-list">
          <li>{TICK}Siting and mounting of outdoor and indoor units</li>
          <li>{TICK}Refrigerant pipework: brazing, pressure testing, evacuation and charging</li>
          <li>{TICK}Hot water cylinder installation</li>
          <li>{TICK}First-fix and second-fix pipework and electrical connections</li>
          <li>{TICK}System handover</li>
        </ul>
        <p style="font-size:0.9rem">Electrical installation work is carried out in accordance with the National Rules for Electrical Installations (I.S. 10101). Where the scope requires a Registered Electrical Contractor, this is arranged and coordinated accordingly.</p>
      </div>
    </div>
  </div>
</section>

<section class="bg-pine">
  <div class="wrap">
    <div class="about-grid">
      <div class="reveal">
        <h2>How we work on site.</h2>
        <p style="color:rgba(244,243,238,0.78);margin-bottom:20px">From the company Safety Statement.</p>
        <ul class="tick-list">
          <li>{TICK}Only F-Gas certified personnel work on refrigerant circuits, and certification is checked before work commences</li>
          <li>{TICK}Refrigerant is recovered using certified recovery equipment and never vented to atmosphere</li>
          <li>{TICK}Safe isolation procedure is followed before any electrical work: isolate, lock off, prove dead</li>
          <li>{TICK}Site briefing or induction is completed on arrival at multi-trade sites</li>
          <li>{TICK}Manual handling training for lifting units, cylinders, gas bottles and equipment</li>
        </ul>
        <p style="color:rgba(244,243,238,0.62);font-size:0.88rem;margin-top:22px">The Safety Statement is a general company document. It is not a job-specific or site-specific risk assessment and does not replace RAMS, method statements, permits-to-work or site inductions, which are prepared separately where required.</p>
      </div>
      <div class="about-media reveal">
        {img("about-installed-unit.jpg", "Completed air-to-water heat pump installation at a domestic property", 750, 1000)}
      </div>
    </div>
  </div>
</section>

<section class="bg-white">
  <div class="wrap">
    <div class="sec-head reveal">
      <h2>After the install.</h2>
      <p>Every system we install is commissioned and handed over, and can be taken onto annual maintenance from there.</p>
    </div>
    <div class="split-cols">
      <div class="panel reveal">
        <h3>Commissioning</h3>
        <p class="panel-sub">Checks against manufacturer specification, settings and controls configured, performance optimised, and a clear handover.</p>
        <a class="btn btn-ghost btn-sm" href="commissioning.html">Commissioning</a>
      </div>
      <div class="panel reveal">
        <h3>Annual maintenance</h3>
        <p class="panel-sub">A yearly visit by an F-Gas certified engineer, with an F-Gas leak check and a written service record.</p>
        <a class="btn btn-ghost btn-sm" href="maintenance.html">Maintenance plan</a>
      </div>
    </div>
  </div>
</section>

{BRANDS_BAND}

{related_services("installation.html")}

{CTA_BAND}
"""


# ============================================================ COMMISSIONING
COMMISSIONING = f"""
<section class="page-hero">
  <div class="wrap">
    <h1>Heat pump commissioning.</h1>
    <p>Correct setup from day one: checks, settings, optimisation, and clear handover. Domestic and commercial air-to-water systems, all of Ireland.</p>
    {crumbs(svc_trail("Commissioning"))}
  </div>
</section>

<section>
  <div class="wrap">
    <div class="svc-detail reveal">
      <div class="svc-detail-media">{img("services-commissioning-controls.jpg", "Heat pump control board and wiring inside an opened control panel", 750, 1000, eager=True)}</div>
      <div>
        <h2>What commissioning covers.</h2>
        <ul class="tick-list">
          <li>{TICK}System checks against manufacturer specification</li>
          <li>{TICK}Settings and controls configured</li>
          <li>{TICK}Optimisation of system performance</li>
          <li>{TICK}Clear handover so you understand your controls</li>
        </ul>
        {SAFE_NOTE}
      </div>
    </div>
  </div>
</section>

<section class="bg-white">
  <div class="wrap">
    <div class="sec-head reveal">
      <h2>Already installed and not performing as expected?</h2>
      <p>That is service and repairs rather than commissioning. Either way, get in touch and we will tell you which one you need.</p>
    </div>
    <ul class="tick-list issues-list reveal">{PROB_BLOCKS}</ul>
    <div style="margin-top:30px"><a class="btn btn-ghost" href="repairs.html">Service &amp; repairs</a></div>
  </div>
</section>

{BRANDS_BAND}

{related_services("commissioning.html")}

{CTA_BAND}
"""


# ============================================================ SERVICE & REPAIRS
REPAIRS = f"""
<section class="page-hero">
  <div class="wrap">
    <h1>Heat pump service and repairs.</h1>
    <p>Fault finding, alarms, cycling issues, DHW temperature problems and performance optimisation. Sligo-based, covering all of Ireland.</p>
    {crumbs(svc_trail("Service &amp; repairs"))}
  </div>
</section>

<section>
  <div class="wrap">
    <div class="svc-detail reveal">
      <div class="svc-detail-media">{img("services-repairs-strainer-check.jpg", "A system strainer checked in hand during a service call", 937, 1000, eager=True)}</div>
      <div>
        <h2>What we look at.</h2>
        <ul class="tick-list">
          <li>{TICK}Fault finding and diagnostics</li>
          <li>{TICK}Alarms and lockouts</li>
          <li>{TICK}Cycling issues</li>
          <li>{TICK}DHW temperature problems</li>
          <li>{TICK}Performance optimisation</li>
        </ul>
        {SAFE_NOTE}
      </div>
    </div>
  </div>
</section>

<section class="bg-pine">
  <div class="wrap">
    <div class="sec-head reveal">
      <h2>Common callouts.</h2>
      <p>If you're seeing any of these, they're usually fixable with the right checks.</p>
    </div>
    <ul class="tick-list issues-list reveal">{PROB_BLOCKS}</ul>
  </div>
</section>

<section class="bg-white">
  <div class="wrap">
    <div class="sec-head reveal">
      <h2>Cold rooms are not always the heat pump.</h2>
      <p>Where flow is unevenly distributed, one room runs warm while another sits cool. That is a balancing job, not a repair.</p>
    </div>
    <div style="margin-top:6px"><a class="btn btn-ghost" href="hydraulic-balancing.html">Hydraulic balancing</a></div>
  </div>
</section>

{ENQUIRY_TIP}

{related_services("repairs.html")}

{CTA_BAND}
"""


# ============================================================ HYDRAULIC BALANCING
BALANCING = f"""
<section class="page-hero">
  <div class="wrap">
    <h1>Hydraulic balancing.</h1>
    <p>Sometimes the heat source is not the problem. Short loops get too much flow and long loops get too little, so one room runs warm while another sits cool.</p>
    {crumbs(svc_trail("Hydraulic balancing"))}
  </div>
</section>

<section>
  <div class="wrap">
    <div class="svc-detail reveal">
      <div class="svc-detail-media">{img("services-balancing-manifold.jpg", "Heating manifold with flow meters, from our hydraulic balancing explainer", 1000, 514, eager=True, cls="frame-landscape")}</div>
      <div>
        <h2>What balancing does.</h2>
        <ul class="tick-list">
          <li>{TICK}Uneven flow distribution identified</li>
          <li>{TICK}Flow meter adjusted by circuit</li>
          <li>{TICK}More even room temperatures</li>
        </ul>
        <p style="font-size:0.9rem">Balancing is carried out at the manifold, circuit by circuit, using the flow meters on the system.</p>
      </div>
    </div>
  </div>
</section>

<section class="bg-white">
  <div class="wrap">
    <div class="sec-head reveal">
      <h2>When it's worth looking at.</h2>
      <p>Two of the five issues we get called out for most often can come back to flow rather than the heat pump itself.</p>
    </div>
    <ul class="tick-list issues-list reveal">
      <li>{TICK}Cold rooms / poor heat output</li>
      <li>{TICK}High electricity bills / low efficiency</li>
    </ul>
    <div style="margin-top:30px"><a class="btn btn-ghost" href="repairs.html">Service &amp; repairs</a></div>
  </div>
</section>

{related_services("hydraulic-balancing.html")}

{CTA_BAND}
"""


# ============================================================ AIR CONDITIONING
AIR_CON = f"""
<section class="page-hero">
  <div class="wrap">
    <h1>Air conditioning installation and service.</h1>
    <p>Domestic and commercial air conditioning, alongside our heat pump work. F-GAS certified refrigerant handling, and a QQI Level 6 Advanced Certificate in Refrigeration and Air Conditioning behind it.</p>
    {crumbs(svc_trail("Air conditioning"))}
  </div>
</section>

<section>
  <div class="wrap">
    <div class="split-cols">
      <div class="panel reveal">
        <h3>Domestic</h3>
        <p class="panel-sub">High wall units for homes.</p>
        <ul class="tick-list">{AC_DOM_LI}</ul>
      </div>
      <div class="panel reveal">
        <h3>Commercial</h3>
        <p class="panel-sub">Offices, retail and light industrial.</p>
        <ul class="tick-list">{AC_COM_LI}</ul>
      </div>
    </div>
  </div>
</section>

<section class="bg-pine">
  <div class="wrap">
    <div class="sec-head reveal">
      <h2>The same certification as the heat pump work.</h2>
      <p>Air conditioning and air-to-water heat pumps are both refrigerant systems, and the same qualifications and rules apply to both.</p>
    </div>
    <ul class="tick-list issues-list reveal">
      <li>{TICK}F-GAS registered. Only F-Gas certified personnel work on refrigerant circuits</li>
      <li>{TICK}QQI Level 6 Advanced Certificate, Craft - Refrigeration and Air Conditioning, awarded with Credit</li>
      <li>{TICK}Refrigerant recovered using certified recovery equipment, never vented to atmosphere</li>
      <li>{TICK}Covered under Combined Liability insurance: Public/Products and Employers' Liability</li>
    </ul>
    <div style="margin-top:30px"><a class="btn btn-amber" href="certifications.html">See the certificates</a></div>
  </div>
</section>

{ENQUIRY_TIP}

{related_services("air-conditioning.html")}

{CTA_BAND}
"""


# ============================================================ MAINTENANCE
MAINT_FAQS = [
    ("How long does an annual visit take?", ["A standard visit takes up to around 90 minutes. If it genuinely takes a little longer to complete the standard checks, that is covered, at no extra charge."]),
    ("What happens if you find something that needs fixing?", ["We will always explain it and agree a price with you before doing the work. The only exception is an immediate safety issue, for example an electrical or refrigerant hazard, where we will make the system safe first and explain afterwards."]),
    ("Does maintenance affect my manufacturer warranty?", ["Most manufacturers require proof of regular professional servicing to keep an extended warranty valid, so having us service your system each year helps you stay eligible for your brand's full extended warranty cover."]),
    ("You did not install my system. Can you still maintain it?", ["Yes. If the system was not originally installed by Irish Air to Water, an initial inspection is required before it can be taken on for ongoing maintenance. That initial inspection is chargeable and separate to the annual visit."]),
    ("What do you need from me on the day?", ["Safe, reasonable access to the indoor and outdoor units, and the outdoor unit kept clear of obstructions such as planting, snow and stored items, so we can access it and it can operate properly."]),
    ("Are you insured?", ["Our work is covered under our Combined Liability insurance, which includes Public and Products Liability and Employers' Liability."]),
]

INCLUDED = [
    "Visual inspection of the outdoor and indoor unit(s), casings, and mounting for signs of damage, corrosion, or wear",
    "Check of refrigerant system pressures and general operation against manufacturer specification",
    "F-Gas leak check, with results recorded as required under F-Gas Regulations",
    "Inspection and cleaning of accessible air filters, or advice if replacement is needed",
    "Check of electrical connections, isolators, and wiring for security and signs of wear",
    "Check of the condensate drain for blockages and correct flow",
    "Check of system controls, programming, and settings, with adjustments made if agreed with you",
    "Check of flow and return temperatures and overall system performance",
    "Visual check of exposed pipework insulation and pipe supports/brackets",
    "A written service record, so you have a note of what was checked and any issues found",
]

CHARGEABLE = [
    "Replacement parts or materials of any kind, for example filters needing replacement, fans, pumps, valves, sensors, controllers",
    "Pipework insulation repairs. The standard visit includes a visual check of insulation, but any repair, replacement, or reinstatement of damaged, missing, or degraded insulation is chargeable",
    "Refrigerant top-up or recharge, and any diagnostic work to trace a leak beyond the routine check",
    "Any repair work identified during the visit, and the labour involved",
    "Emergency or out-of-hours call-outs, and breakdown visits outside your scheduled annual visit",
    "Extra labour where it is needed for fault-finding or repair, rather than the standard checks",
    "Access equipment beyond what is normally carried on the van, for example scaffolding, tower access, extended ladder work",
    "An initial inspection if the system was not originally installed by Irish Air to Water, before it can be taken on for ongoing maintenance",
    "Gas boiler or gas appliance work. This is separate to heat pump maintenance and outside scope regardless",
    "A call-out charge if we attend and cannot gain access, or the visit is cancelled with less than 24 hours' notice",
    "Call-outs resulting from misuse, unauthorised modification, or work carried out on the system by someone else since the last visit",
]

NEEDED = [
    "Safe, reasonable access to the indoor and outdoor units on the day of your appointment",
    "The outdoor unit kept clear of obstructions (planting, snow, stored items) so we can access it and it can operate properly",
    "Let us know as soon as possible about any fault, unusual noise, or performance issue, rather than waiting for the next annual visit",
    "Please avoid having the system opened or worked on by anyone other than a qualified engineer between visits, as this can affect both performance and warranty",
]

INC_LI = "".join(f"<li>{TICK}<span>{t}</span></li>" for t in INCLUDED)
CHG_LI = "".join(f"<li>{PLUS}<span>{t}</span></li>" for t in CHARGEABLE)
NEED_LI = "".join(f"<li>{TICK}{t}</li>" for t in NEEDED)

MAINTENANCE = f"""
<section class="page-hero">
  <div class="wrap">
    <h1>Your annual maintenance visit.</h1>
    <p>What's included, and what's chargeable. We share this with all customers ahead of their visit so there are no surprises.</p>
    {crumbs(svc_trail("Aftersales maintenance"))}
  </div>
</section>

<section class="sec-tight">
  <div class="wrap">
    <div class="stat-row">
      <div class="stat reveal"><strong>~90 min</strong><span>A standard visit takes up to around 90 minutes.</span></div>
      <div class="stat reveal"><strong>F-Gas certified</strong><span>Every visit is carried out by an F-Gas certified engineer.</span></div>
      <div class="stat reveal"><strong>Written record</strong><span>A note of what was checked and any issues found.</span></div>
    </div>
  </div>
</section>

<section style="padding-top:24px">
  <div class="wrap">
    <div class="sec-head reveal">
      <h2>What's included, and what's chargeable.</h2>
      <p>If anything chargeable comes up during the visit, we'll always explain it and agree a price with you before doing the work.</p>
    </div>
    <div class="split-cols">
      <div class="panel panel-included reveal">
        <h3>Included in your annual visit</h3>
        <p class="panel-sub">Every annual maintenance visit is carried out by an F-Gas certified engineer and includes:</p>
        <ul>{INC_LI}</ul>
      </div>
      <div class="panel panel-chargeable reveal">
        <h3>Chargeable, not included</h3>
        <p class="panel-sub">The items below aren't part of the standard annual check.</p>
        <ul>{CHG_LI}</ul>
      </div>
    </div>
    <div class="callout reveal">
      <h3>One exception on agreeing a price first</h3>
      <p>Where there's an immediate safety issue, for example an electrical or refrigerant hazard, we'll make the system safe first and explain afterwards.</p>
    </div>
  </div>
</section>

<section class="bg-pine">
  <div class="wrap">
    <div class="about-grid">
      <div class="reveal">
        <h2>What we need from you.</h2>
        <ul class="tick-list" style="margin-top:22px">{NEED_LI}</ul>
      </div>
      <div class="about-media reveal">
        {img("maintenance-clear-access.jpg", "Outdoor heat pump unit with clear space around it", 750, 1000)}
      </div>
    </div>
  </div>
</section>

<section class="bg-white">
  <div class="wrap">
    <div class="sec-head reveal">
      <h2>A few other things to know.</h2>
    </div>
    <div class="split-cols">
      <div class="reveal">
        <h3 style="font-size:1.15rem;margin-bottom:10px">Extended warranty</h3>
        <p style="color:#5c6b64;margin-bottom:24px">Keeping up with annual maintenance actually helps you, not hinders you. Most manufacturers require proof of regular professional servicing to keep an extended warranty valid, so having us service your system each year helps you stay eligible for your brand's full extended warranty cover.</p>
        <h3 style="font-size:1.15rem;margin-bottom:10px">Insurance</h3>
        <p style="color:#5c6b64">Our work is covered under our Combined Liability insurance, which includes Public/Products Liability and Employers' Liability.</p>
      </div>
      <div class="reveal">
        <h3 style="font-size:1.15rem;margin-bottom:10px">What maintenance doesn't cover</h3>
        <p style="color:#5c6b64;margin-bottom:24px">Maintenance doesn't cover damage from misuse, unauthorised modification, power surges, frost damage from the system being left switched off, or storm, flood or lightning damage. These would be treated as chargeable repair work.</p>
        <h3 style="font-size:1.15rem;margin-bottom:10px">Any questions?</h3>
        <p style="color:#5c6b64">If you have any questions about what's included or what something might cost, just ask. We're happy to talk it through before, during, or after your visit.</p>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap-narrow">
    <div class="sec-head reveal" style="margin-bottom:34px">
      <h2>Maintenance questions.</h2>
    </div>
    <div class="reveal">{faq_block(MAINT_FAQS)}</div>
  </div>
</section>

{related_services("maintenance.html")}

<section class="contact">
  <div class="wrap contact-grid">
    <div class="reveal">
      <h2>Book your annual maintenance visit.</h2>
      <p class="contact-lede">Call, WhatsApp, email or send the form.</p>
      {CONTACT_LIST}
    </div>
    {form_card("Book a maintenance visit", "We share this information sheet with all customers ahead of their visit.", "Send enquiry")}
  </div>
</section>
"""


# ============================================================ CERTIFICATIONS
CERTS = [
    {
        "title": "F-GAS Registered",
        "desc": "Certification for work on refrigerant circuits. Under F-Gas Regulations, only personnel holding a valid F-Gas personal certificate may work on a refrigerant circuit, and leak checks must be recorded.",
        "media": '<div class="doc-tile"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/><path d="m9 12 2 2 4-4"/></svg></div>',
        "meta": [("Scope", "Refrigerant circuit work and recorded leak checks")],
    },
    {
        "title": "QQI Level 6 Advanced Certificate",
        "desc": "Craft - Refrigeration and Air Conditioning, awarded with Credit by Quality and Qualifications Ireland.",
        "media": f'<div class="doc-frame">{pic("cert-qqi.jpg", "QQI Level 6 Advanced Certificate awarded to Daire Cullinane", 525, 700)}</div>',
        "meta": [("Awarded", "14 June 2020, with Credit"), ("Level", "NFQ Level 6 / EQF Level 5")],
    },
    {
        "title": "Grant Aerona R290 Course",
        "desc": "One-day workshop on product knowledge and best practice for installing Grant R290 air source heat pumps and their associated system components.",
        "media": f'<div class="doc-frame">{pic("cert-r290.jpg", "Grant Aerona R290 course certificate", 700, 496)}</div>',
        "meta": [("Attended", "30 October 2025"), ("Provider", "Grant, grant.ie")],
    },
    {
        "title": "Manual Handling",
        "desc": "Manual handling training, as referenced in the company Safety Statement's control measures for lifting heat pump units, cylinders, gas bottles and equipment.",
        "media": f'<div class="doc-frame">{pic("cert-manual-handling.jpg", "Manual handling certificate", 660, 510)}</div>',
        "meta": [("Issued", "11 March 2025"), ("Valid to", "11 March 2028"), ("Certificate no.", "CERT603373")],
    },
    {
        "title": "Company Safety Statement",
        "desc": "Prepared under Section 20 of the Safety, Health and Welfare at Work Act 2005. Sets out the company's general safety policy, responsibilities, hazard identification, control measures, emergency procedures, training and competency arrangements and insurance-related safety controls.",
        "media": f'<div class="doc-frame">{pic("cert-safety-statement.jpg", "Irish Air to Water Safety Statement cover page", 496, 700)}</div>',
        "meta": [("Issued", "6 August 2026"), ("Review date", "6 August 2027"), ("Provided to", "Main contractors, mechanical contractors and other parties on request")],
    },
    {
        "title": "Combined Liability Insurance",
        "desc": "Public/Products Liability and Employers' Liability cover, appropriate to the work undertaken.",
        "media": '<div class="doc-tile"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7z"/><path d="M14 2v4a2 2 0 0 0 2 2h4"/><path d="M10 9H8"/><path d="M16 13H8"/><path d="M16 17H8"/></svg></div>',
        "meta": [("Cover", "Public / Products Liability"), ("Cover", "Employers' Liability")],
    },
]

CERT_CARDS = ""
for c in CERTS:
    meta = "".join(f"<li><strong>{k}:</strong> {v}</li>" for k, v in c["meta"])
    CERT_CARDS += f"""<div class="cert reveal">
  {c['media']}
  <h3>{c['title']}</h3>
  <p>{c['desc']}</p>
  <ul class="cert-meta">{meta}</ul>
</div>"""

CERTIFICATIONS = f"""
<section class="page-hero">
  <div class="wrap">
    <h1>Certified, registered and insured.</h1>
    <p>Documentation is available to homeowners, main contractors and mechanical contractors on request.</p>
    {crumbs([("index.html", "Home"), (None, "Certifications")])}
  </div>
</section>

<section>
  <div class="wrap">
    <div class="cert-grid">{CERT_CARDS}</div>
  </div>
</section>

<section class="bg-pine">
  <div class="wrap">
    <div class="about-grid">
      <div class="about-media reveal">
        {img("certifications-at-work.jpg", "A large system strainer removed for cleaning on a commercial installation", 750, 1000)}
      </div>
      <div class="reveal">
        <h2>How we work on site.</h2>
        <p style="color:rgba(244,243,238,0.78);margin-bottom:20px">From the company Safety Statement.</p>
        <ul class="tick-list">
          <li>{TICK}Only F-Gas certified personnel work on refrigerant circuits, and certification is checked before work commences</li>
          <li>{TICK}Refrigerant is recovered using certified recovery equipment and never vented to atmosphere</li>
          <li>{TICK}Safe isolation procedure is followed before any electrical work: isolate, lock off, prove dead</li>
          <li>{TICK}Electrical installation work is carried out in accordance with the National Rules for Electrical Installations (I.S. 10101)</li>
          <li>{TICK}Site briefing or induction is completed on arrival at multi-trade sites</li>
        </ul>
        <p style="color:rgba(244,243,238,0.62);font-size:0.88rem;margin-top:22px">The Safety Statement is a general company document. It is not a job-specific or site-specific risk assessment and does not replace RAMS, method statements, permits-to-work or site inductions, which are prepared separately where required.</p>
      </div>
    </div>
  </div>
</section>

{CTA_BAND}
"""


# ============================================================ CONTACT
CONTACT = f"""
<section class="page-hero">
  <div class="wrap">
    <h1>Get in touch.</h1>
    <p>Call, WhatsApp, email or send the form. Sligo-based, covering all of Ireland, domestic and commercial.</p>
    {crumbs([("index.html", "Home"), (None, "Contact")])}
  </div>
</section>

<section class="contact" style="padding-top:72px">
  <div class="wrap contact-grid">
    <div class="reveal">
      <h2>Fastest way to book.</h2>
      {CONTACT_LIST}
      <p style="color:rgba(244,243,238,0.7);font-size:0.92rem;margin-top:28px;max-width:48ch">Tip: include your county, system brand/model, and whether it's commissioning or service/maintenance. If there's an alarm, include the code/photo.</p>
    </div>
    {form_card("Send an enquiry", "")}
  </div>
</section>

<section id="coverage">
  <div class="wrap coverage-grid">
    {COVERAGE_BLOCK}
    <div class="coverage-media reveal">
      {img("contact-coverage-grant-unit.jpg", "Grant air-to-water heat pump outdoor unit at a domestic property", 750, 1000)}
    </div>
  </div>
</section>
"""


# ============================================================ REVIEWS
# All five are real Facebook recommendations transcribed from the promo video
# Dáire supplied. Customers' own wording; the three on the home page are trimmed,
# these are the fuller versions. No review schema: self-serving reviews on a
# LocalBusiness are against Google's guidelines, so they stay visual only.
REVIEWS = [
    ("Stephanie Callaghan",
     "He was absolutely fantastic from start to finish. He explained everything clearly, was very professional, and his pricing was extremely reasonable. It&rsquo;s such a relief to find someone so reliable, honest, and helpful."),
    ("R&oacute;is&iacute;n Mc Gloin",
     "I would highly recommend D&aacute;ire! I contacted him about servicing my heat pump system, and he got back to me straight away, arranging a service visit for the very next day. From start to finish, he was professional, reliable, and incredibly helpful. I had issues with my SATs, and he took the time to resolve the problem, explain everything clearly, and give me a better understanding of how the system works. Great service and excellent communication. I wouldn&rsquo;t hesitate to recommend him to anyone."),
    ("Shawana Moriarty",
     "Absolutely 10/10 service. Knew what the problem was straight away and got it sorted. I&rsquo;ve had 5 people come to look at the problem and only he knew. Recommend 100%."),
    ("Niamh Clancy",
     "I would highly recommend Daire! He took the time out of his evening to check everything was working properly for me in my home and also showed me how to use the system correctly as I was never shown previously. Genuine person, great price and very very helpful!!"),
    ("Rebecca Fabozzi",
     "We have been having extremely high bills because of our heat pump and no knowledge as to why. Since he has looked at it, our usage on the pump has come down and our bills reduced."),
]

REVIEW_CARDS = "".join(
    f'<div class="review reveal"><blockquote>&ldquo;{text}&rdquo;</blockquote>'
    f'<div class="review-who">{name}<small>Facebook review</small></div></div>'
    for name, text in REVIEWS
)

REVIEWS_PAGE = f"""
<section class="page-hero">
  <div class="wrap">
    <h1>What our customers say.</h1>
    <p>Recommendations from the Irish Air to Water Facebook page, in the customers' own words.</p>
    {crumbs([("index.html", "Home"), (None, "Reviews")])}
  </div>
</section>

<section>
  <div class="wrap reviews-page">
    <div class="reviews-list">{REVIEW_CARDS}</div>
    <div class="reviews-side">
      <div class="review-video reveal">
        <video controls playsinline preload="none" poster="media/customer-reviews-poster.jpg" aria-label="Customer reviews from the Irish Air to Water Facebook page">
          <source src="media/customer-reviews.mp4" type="video/mp4">
        </video>
      </div>
      <p class="reviews-side-note">Follow us on Instagram at <a href="https://www.instagram.com/irish_airtowater" target="_blank" rel="noopener">@irish_airtowater</a>.</p>
    </div>
  </div>
</section>

{CTA_BAND}
"""


# ============================================================ FAQ
# Every answer traces to his site, the maintenance PDF, the Safety Statement,
# his LinkedIn balancing graphic, or his relayed air conditioning scope.
GENERAL_FAQS = [
    ("What areas do you cover?",
     ["We are based in Sligo and cover all of Ireland, for both domestic and commercial systems."]),
    ("Which heat pump brands do you work on?",
     ["MasterTherm, Mitsubishi Electric, Mitsubishi Heavy Industries, Panasonic and Samsung. We have experience commissioning, servicing and maintaining a wide range of domestic and commercial air-to-water systems."]),
    ("Do you install heat pumps, or only service them?",
     ["Both. We install domestic and commercial air-to-water heat pump systems through to commissioning and handover: siting and mounting of outdoor and indoor units, refrigerant pipework, hot water cylinder installation, first-fix and second-fix pipework and electrical connections, and system handover."]),
    ("Do you do air conditioning?",
     ["Yes. Installation and service of high wall domestic air conditioners, and of commercial systems including cassette and underceiling units and multi-unit VRV/VRF systems."]),
    ("Are you F-Gas registered?",
     ["Yes. Under F-Gas Regulations, only personnel holding a valid F-Gas personal certificate may work on a refrigerant circuit. Refrigerant is recovered using certified recovery equipment and is never vented to atmosphere."]),
    ("Do you work on gas boilers?",
     ["No. Gas boiler and gas appliance work is separate to heat pump maintenance and outside our scope."]),
]

CALLING_FAQS = [
    ("What should I include when I get in touch?",
     ["Your county, the system brand and model, and whether it's commissioning or service and maintenance. If there's an alarm, include the code or a photo of the display."]),
    ("What are the most common problems you get called out for?",
     ["High electricity bills or low efficiency, the heat pump cycling on and off, hot water not reaching temperature, cold rooms or poor heat output, and noise, alarms or frequent defrost. If you're seeing any of these, they're usually fixable with the right checks."]),
    ("One room is warm and another is cold. Is the heat pump faulty?",
     ["Not necessarily. Sometimes the heat source is not the problem. Short loops get too much flow and long loops get too little, so one room runs warm while another sits cool. Hydraulic balancing identifies the uneven flow distribution and adjusts the flow meter circuit by circuit for more even room temperatures."]),
]

MAINT_MORE_FAQS = [
    ("What isn't covered by maintenance?",
     ["Maintenance doesn't cover damage from misuse, unauthorised modification, power surges, frost damage from the system being left switched off, or storm, flood or lightning damage. These would be treated as chargeable repair work."]),
    ("What if I need to cancel a visit?",
     ["Please give at least 24 hours' notice. A call-out charge applies if we attend and cannot gain access, or if the visit is cancelled with less than 24 hours' notice."]),
]

CONTRACTOR_FAQS = [
    ("Can you provide a Safety Statement or RAMS?",
     ["Our company Safety Statement, prepared under Section 20 of the Safety, Health and Welfare at Work Act 2005, is provided to main contractors, mechanical contractors and other parties on request. It is a general company document and does not replace RAMS, method statements, permits-to-work or site inductions, which are prepared separately where required."]),
    ("How do you work on multi-trade sites?",
     ["A site briefing or induction is completed on arrival. F-Gas certification is checked before work commences, and safe isolation (isolate, lock off, prove dead) is followed before any electrical work. Electrical installation work is carried out in accordance with the National Rules for Electrical Installations (I.S. 10101); where the scope requires a Registered Electrical Contractor, this is arranged and coordinated."]),
]

FAQ_GROUPS = [
    ("General", GENERAL_FAQS),
    ("Getting in touch", CALLING_FAQS),
    ("Annual maintenance", MAINT_FAQS + MAINT_MORE_FAQS),
    ("For contractors", CONTRACTOR_FAQS),
]

_faq_html = ""
_n = 1
for _title, _items in FAQ_GROUPS:
    _faq_html += f'<div class="faq-group reveal"><h2>{_title}</h2>{faq_block(_items, start=_n)}</div>'
    _n += len(_items)
ALL_FAQS = [q for _t, items in FAQ_GROUPS for q in items]

FAQ_PAGE = f"""
<section class="page-hero">
  <div class="wrap">
    <h1>Frequently asked questions.</h1>
    <p>Coverage, brands, what to send us, what a maintenance visit covers, and what contractors need to know.</p>
    {crumbs([("index.html", "Home"), (None, "FAQ")])}
  </div>
</section>

<section>
  <div class="wrap-narrow">
    {_faq_html}
    <p class="faq-more">Something else? <a href="contact.html">Get in touch</a> or call <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>.</p>
  </div>
</section>

{CTA_BAND}
"""


# ============================================================ PRIVACY
# Plain statement of what the site actually collects. To be checked by Dáire.
PRIVACY = f"""
<section class="page-hero">
  <div class="wrap">
    <h1>Privacy.</h1>
    <p>What this website collects, why, and how to contact us about it.</p>
    {crumbs([("index.html", "Home"), (None, "Privacy")])}
  </div>
</section>

<section>
  <div class="wrap-narrow prose">
    <h2>Who we are</h2>
    <p>Irish Air to Water is a heat pump and air conditioning business based in Sligo, Ireland. The proprietor is D&aacute;ire Cullinane. You can reach us at <a href="mailto:{EMAIL}">{EMAIL}</a> or <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>.</p>

    <h2>What we collect</h2>
    <p>If you send an enquiry through the form on this site, we receive what you type: your name, phone number, county, heat pump brand or model, and the type of work you need. We use it to respond to your enquiry and, if you become a customer, to arrange and carry out the work. We do not use it for marketing and we do not sell or share it with anyone else.</p>
    <p>If you call, WhatsApp or email us, we hold your contact details and the content of your message for the same purpose.</p>

    <h2>Cookies and analytics</h2>
    <p>This site does not set cookies and does not run analytics or advertising scripts.</p>

    <h2>Third parties</h2>
    <p>The site is hosted on Vercel. Fonts are loaded from Google Fonts, which means your browser requests the font files from Google's servers when you visit. Form submissions are delivered to us by email. WhatsApp links open WhatsApp, which has its own privacy policy.</p>

    <h2>How long we keep it</h2>
    <p>Enquiry details are kept for as long as needed to respond and, for customers, for as long as we maintain the system and as required for tax and legal records.</p>

    <h2>Your rights</h2>
    <p>Under the GDPR you can ask what personal data we hold about you, ask for it to be corrected or deleted, or object to our use of it. Email <a href="mailto:{EMAIL}">{EMAIL}</a>. If you are not satisfied with our response you can contact the Data Protection Commission at <a href="https://www.dataprotection.ie" target="_blank" rel="noopener">dataprotection.ie</a>.</p>

    <p class="prose-note">Last updated September 2026.</p>
  </div>
</section>
"""


# ============================================================ 404
NOT_FOUND = f"""
<section class="page-hero" style="padding:96px 0 100px">
  <div class="wrap">
    <h1>That page doesn't exist.</h1>
    <p>It may have moved, or the link may be wrong. Everything is one click away below.</p>
    <div class="hero-ctas" style="margin-top:32px">
      <a class="btn btn-amber" href="index.html">Back to the homepage</a>
      <a class="btn btn-ghost-light" href="tel:{PHONE_TEL}">{ICON_PHONE}{PHONE_DISPLAY}</a>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head reveal"><h2>Our services.</h2></div>
    {svc_cards()}
  </div>
</section>

<section class="bg-white sec-tight">
  <div class="wrap">
    <div class="sec-head reveal"><h2>Elsewhere on the site.</h2></div>
    <div class="related-row reveal">
      <a href="services.html">All services</a>
      <a href="certifications.html">Certifications</a>
      <a href="index.html#coverage">Coverage</a>
      <a href="contact.html">Contact</a>
    </div>
  </div>
</section>
"""


# ============================================================ BUILD
if __name__ == "__main__":
    page("index.html",
         "Heat Pump & Air Conditioning Specialist, Sligo | Irish Air to Water",
         "Air-to-water heat pump commissioning, service and maintenance, plus domestic and commercial air conditioning. F-GAS registered, Sligo-based, all of Ireland.",
         HOME,
         head_extra='<link rel="preload" as="image" href="media/brand-intro-poster.jpg" fetchpriority="high">\n')

    page("services.html",
         "Heat Pump & Air Conditioning Services, Sligo | Irish Air to Water",
         "Heat pump installation, commissioning, service and repairs, maintenance, hydraulic balancing and air conditioning. Domestic and commercial, all of Ireland.",
         SERVICES,
         extra_schema=[breadcrumb_schema([("index.html", "Home"), (None, "Services")])])

    page("installation.html",
         "Heat Pump Installation, Sligo & Nationwide | Irish Air to Water",
         "Installation of domestic and commercial air-to-water heat pump systems, from siting and refrigerant pipework through to commissioning and handover.",
         INSTALLATION,
         extra_schema=[
             service_schema("Air-to-water heat pump installation",
                            "Installation of domestic and commercial air-to-water heat pump systems, through to commissioning and handover.",
                            "installation.html"),
             breadcrumb_schema(svc_trail("Installation")),
         ])

    page("commissioning.html",
         "Heat Pump Commissioning, Ireland | Irish Air to Water",
         "Air-to-water heat pump commissioning: checks against manufacturer specification, settings and controls configured, performance optimised, clear handover.",
         COMMISSIONING,
         extra_schema=[
             service_schema("Air-to-water heat pump commissioning",
                            "Correct setup from day one: checks against manufacturer specification, settings and controls configured, optimisation, and clear handover.",
                            "commissioning.html"),
             breadcrumb_schema(svc_trail("Commissioning")),
         ])

    page("repairs.html",
         "Heat Pump Service & Repairs, Sligo | Irish Air to Water",
         "Air-to-water heat pump fault finding and repairs: alarms and lockouts, cycling issues, DHW temperature problems and performance optimisation.",
         REPAIRS,
         extra_schema=[
             service_schema("Air-to-water heat pump service and repairs",
                            "Fault finding, alarms and lockouts, cycling issues, DHW temperature problems and performance optimisation.",
                            "repairs.html"),
             breadcrumb_schema(svc_trail("Service &amp; repairs")),
         ])

    page("maintenance.html",
         "Annual Heat Pump Maintenance Visit | Irish Air to Water",
         "What's included in your annual air-to-water heat pump maintenance visit and what's chargeable. F-Gas certified engineer, written service record.",
         MAINTENANCE,
         extra_schema=[
             service_schema("Heat pump aftersales maintenance",
                            "Annual maintenance visit by an F-Gas certified engineer, including a recorded F-Gas leak check and a written service record, plus callouts between visits.",
                            "maintenance.html"),
             breadcrumb_schema(svc_trail("Aftersales maintenance")),
             faq_schema(MAINT_FAQS),
         ])

    page("hydraulic-balancing.html",
         "Hydraulic Balancing for Heat Pumps | Irish Air to Water",
         "Short loops get too much flow and long loops too little, so one room runs warm and another cool. Balancing evens the flow out circuit by circuit at the manifold.",
         BALANCING,
         extra_schema=[
             service_schema("Hydraulic balancing",
                            "Identifying uneven flow distribution and adjusting flow meters circuit by circuit for more even room temperatures.",
                            "hydraulic-balancing.html"),
             breadcrumb_schema(svc_trail("Hydraulic balancing")),
         ])

    page("air-conditioning.html",
         "Air Conditioning Installation & Service | Irish Air to Water",
         "Domestic high wall air conditioning and commercial systems including cassette, underceiling and multi-unit VRV/VRF. F-GAS certified, Sligo-based, all of Ireland.",
         AIR_CON,
         extra_schema=[
             service_schema("Air conditioning installation and service",
                            "Installation and service of domestic high wall air conditioning units, and commercial systems including cassette, underceiling and multi-unit VRV/VRF.",
                            "air-conditioning.html"),
             breadcrumb_schema(svc_trail("Air conditioning")),
         ])

    page("certifications.html",
         "Certifications & Insurance | Irish Air to Water",
         "F-GAS registered, QQI Level 6 in Refrigeration and Air Conditioning, Grant R290 trained, Safety Statement and Combined Liability insurance.",
         CERTIFICATIONS,
         extra_schema=[breadcrumb_schema([("index.html", "Home"), (None, "Certifications")])])

    page("reviews.html",
         "Customer Reviews | Irish Air to Water",
         "Real recommendations from the Irish Air to Water Facebook page: heat pump servicing, repairs and clear explanations, in the customers' own words.",
         REVIEWS_PAGE,
         extra_schema=[breadcrumb_schema([("index.html", "Home"), (None, "Reviews")])])

    page("faq.html",
         "Heat Pump FAQ | Irish Air to Water, Sligo",
         "Coverage, brands, what to send when you get in touch, what an annual maintenance visit covers, and what contractors need. Straight answers from Irish Air to Water.",
         FAQ_PAGE,
         extra_schema=[faq_schema(ALL_FAQS),
                       breadcrumb_schema([("index.html", "Home"), (None, "FAQ")])])

    page("privacy.html",
         "Privacy | Irish Air to Water",
         "What the Irish Air to Water website collects when you send an enquiry, why, and how to contact us about your data.",
         PRIVACY,
         extra_schema=[breadcrumb_schema([("index.html", "Home"), (None, "Privacy")])])

    page("404.html",
         "Page not found | Irish Air to Water",
         "That page doesn't exist. Head back to the homepage or call 087 341 3114.",
         NOT_FOUND)

    page("contact.html",
         "Contact | Irish Air to Water Heat Pump Specialists, Sligo",
         "Call 087 341 3114, WhatsApp or email. Air-to-water heat pump installation, commissioning, service and repairs. Sligo-based, covering all of Ireland.",
         CONTACT,
         extra_schema=[breadcrumb_schema([("index.html", "Home"), (None, "Contact")])])

    sitemap([
        ("index.html", "1.0"),
        ("services.html", "0.9"),
        ("installation.html", "0.8"),
        ("commissioning.html", "0.8"),
        ("repairs.html", "0.8"),
        ("maintenance.html", "0.8"),
        ("hydraulic-balancing.html", "0.7"),
        ("air-conditioning.html", "0.8"),
        ("reviews.html", "0.7"),
        ("faq.html", "0.7"),
        ("certifications.html", "0.7"),
        ("contact.html", "0.8"),
        ("privacy.html", "0.3"),
    ])
