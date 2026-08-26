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
)

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
    return f"""<div class="form-card reveal">
  <h3>{heading}</h3>{sub_html}
  <form data-iatw-form>
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
    <div class="svc-grid svc-grid-3">
      <a class="svc reveal" href="services.html#commissioning">
        <div class="svc-watermark" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg></div>
        <h3>Commissioning</h3>
        <p>Correct setup from day one: checks, settings, optimisation, and clear handover.</p>
      </a>
      <a class="svc reveal" href="services.html#repairs">
        <div class="svc-watermark" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg></div>
        <h3>Service &amp; Repairs</h3>
        <p>Fault finding, alarms, cycling issues, DHW temperature problems and performance optimisation.</p>
      </a>
      <a class="svc reveal" href="services.html#aftersales">
        <div class="svc-watermark" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 20h9"/><path d="M16.5 3.5a2.12 2.12 0 0 1 3 3L7 19l-4 1 1-4Z"/></svg></div>
        <h3>Aftersales Maintenance</h3>
        <p>Planned servicing and callouts to keep systems running efficiently year-round.</p>
      </a>
    </div>
  </div>
</section>

<section class="bg-white">
  <div class="wrap">
    <div class="sec-head reveal">
      <h2>Services.</h2>
      <p>Air-to-water heat pumps. Domestic and commercial.</p>
    </div>
    <ul class="tick-list issues-list reveal">
      <li>{TICK}Commissioning &amp; setup (controls, temperatures, checks)</li>
      <li>{TICK}Performance optimisation &amp; troubleshooting</li>
      <li>{TICK}Routine / planned maintenance</li>
      <li>{TICK}Repairs &amp; fault finding (alarms, cycling, low performance)</li>
      <li>{TICK}Clear reporting &amp; recommendations</li>
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
      <div class="g-item g-tall"><img src="images/coverage-home-install.jpg" alt="Finished Panasonic air-to-water heat pump installation" width="750" height="1000" loading="lazy" decoding="async"></div>
      <div class="g-item"><img src="images/services-commissioning-controls.jpg" alt="Heat pump control board during commissioning" width="750" height="1000" loading="lazy" decoding="async"></div>
      <div class="g-item"><img src="images/services-aftersales-filters.jpg" alt="Air filters removed for cleaning on a service visit" width="750" height="1000" loading="lazy" decoding="async"></div>
      <div class="g-item g-tall"><img src="images/certifications-at-work.jpg" alt="Servicing pipework on a commercial heat pump installation" width="750" height="1000" loading="lazy" decoding="async"></div>
      <div class="g-item"><img src="images/services-installation.jpg" alt="Wall-mounted heat pump unit with pipework" width="562" height="1000" loading="lazy" decoding="async"></div>
      <div class="g-item"><img src="images/maintenance-clear-access.jpg" alt="Outdoor heat pump unit sited with clear space around it" width="750" height="1000" loading="lazy" decoding="async"></div>
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


# ============================================================ SERVICES
SERVICES = f"""
<section class="page-hero">
  <div class="wrap">
    <h1>Air-to-water heat pump services.</h1>
    <p>Installation, commissioning, service and repairs, and aftersales maintenance. Domestic and commercial systems, Sligo-based, covering all of Ireland.</p>
    <ul class="crumbs"><li><a href="index.html">Home</a></li><li>Services</li></ul>
  </div>
</section>

<section>
  <div class="wrap">

    <div class="svc-detail reveal" id="installation">
      <div class="svc-detail-media">{img("services-installation.jpg", "Wall-mounted heat pump unit with pipework run down the wall", 562, 1000)}</div>
      <div>
        <h2>Installation</h2>
        <p>Installation of domestic and commercial air-to-water heat pump systems, through to commissioning and handover.</p>
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

    <div class="svc-detail flip reveal" id="commissioning">
      <div class="svc-detail-media">{img("services-commissioning-controls.jpg", "Heat pump control board and wiring inside an opened control panel", 750, 1000)}</div>
      <div>
        <h2>Commissioning</h2>
        <p>Correct setup from day one: checks, settings, optimisation, and clear handover.</p>
        <ul class="tick-list">
          <li>{TICK}System checks against manufacturer specification</li>
          <li>{TICK}Settings and controls configured</li>
          <li>{TICK}Optimisation of system performance</li>
          <li>{TICK}Clear handover so you understand your controls</li>
        </ul>
      </div>
    </div>

    <div class="svc-detail reveal" id="repairs">
      <div class="svc-detail-media">{img("services-repairs-strainer-check.jpg", "A system strainer checked in hand during a service call", 937, 1000)}</div>
      <div>
        <h2>Service &amp; repairs</h2>
        <p>Fault finding, alarms, cycling issues, DHW temperature problems and performance optimisation.</p>
        <ul class="tick-list">
          <li>{TICK}Fault finding and diagnostics</li>
          <li>{TICK}Alarms and lockouts</li>
          <li>{TICK}Cycling issues</li>
          <li>{TICK}DHW temperature problems</li>
          <li>{TICK}Performance optimisation</li>
        </ul>
        <p style="font-size:0.9rem">Work on refrigerant circuits is carried out only by F-Gas certified personnel, using certified recovery equipment. Refrigerant is never vented to atmosphere.</p>
      </div>
    </div>

    <div class="svc-detail flip reveal" id="aftersales">
      <div class="svc-detail-media">{img("services-aftersales-filters.jpg", "Air filters removed and laid out for cleaning during a service visit", 750, 1000)}</div>
      <div>
        <h2>Aftersales maintenance</h2>
        <p>Planned servicing and callouts to keep systems running efficiently year-round.</p>
        <ul class="tick-list">
          <li>{TICK}Annual maintenance visit, carried out by an F-Gas certified engineer</li>
          <li>{TICK}F-Gas leak check, recorded as required under F-Gas Regulations</li>
          <li>{TICK}Written service record of what was checked and any issues found</li>
          <li>{TICK}Callouts between scheduled visits</li>
        </ul>
        <a class="btn btn-amber btn-sm" href="maintenance.html">See what a visit includes</a>
      </div>
    </div>

    <div class="svc-detail reveal" id="balancing">
      <div class="svc-detail-media">{img("services-balancing-manifold.jpg", "Heating manifold with flow meters, from our hydraulic balancing explainer", 1000, 514, cls="frame-landscape")}</div>
      <div>
        <h2>Hydraulic balancing</h2>
        <p>Sometimes the heat source is not the problem. Short loops get too much flow and long loops get too little, so one room runs warm while another sits cool.</p>
        <ul class="tick-list">
          <li>{TICK}Uneven flow distribution identified</li>
          <li>{TICK}Flow meter adjusted by circuit</li>
          <li>{TICK}More even room temperatures</li>
        </ul>
      </div>
    </div>

  </div>
</section>

<section class="bg-white sec-tight">
  <div class="wrap">
    <div class="sec-head reveal">
      <h2>Brands we work with.</h2>
    </div>
    <div class="brands-row reveal">{BRANDS_ROW}</div>
  </div>
</section>

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
    <ul class="crumbs"><li><a href="index.html">Home</a></li><li>Maintenance Plan</li></ul>
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
        "media": '<div class="doc-frame"><img src="images/cert-qqi.jpg" alt="QQI Level 6 Advanced Certificate awarded to Daire Cullinane" width="525" height="700" loading="lazy" decoding="async"></div>',
        "meta": [("Awarded", "14 June 2020, with Credit"), ("Level", "NFQ Level 6 / EQF Level 5")],
    },
    {
        "title": "Grant Aerona R290 Course",
        "desc": "One-day workshop on product knowledge and best practice for installing Grant R290 air source heat pumps and their associated system components.",
        "media": '<div class="doc-frame"><img src="images/cert-r290.jpg" alt="Grant Aerona R290 course certificate" width="700" height="496" loading="lazy" decoding="async"></div>',
        "meta": [("Attended", "30 October 2025"), ("Provider", "Grant, grant.ie")],
    },
    {
        "title": "Manual Handling",
        "desc": "Manual handling training, as referenced in the company Safety Statement's control measures for lifting heat pump units, cylinders, gas bottles and equipment.",
        "media": '<div class="doc-frame"><img src="images/cert-manual-handling.jpg" alt="Manual handling certificate" width="660" height="510" loading="lazy" decoding="async"></div>',
        "meta": [("Issued", "11 March 2025"), ("Valid to", "11 March 2028"), ("Certificate no.", "CERT603373")],
    },
    {
        "title": "Company Safety Statement",
        "desc": "Prepared under Section 20 of the Safety, Health and Welfare at Work Act 2005. Sets out the company's general safety policy, responsibilities, hazard identification, control measures, emergency procedures, training and competency arrangements and insurance-related safety controls.",
        "media": '<div class="doc-frame"><img src="images/cert-safety-statement.jpg" alt="Irish Air to Water Safety Statement cover page" width="496" height="700" loading="lazy" decoding="async"></div>',
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
    <ul class="crumbs"><li><a href="index.html">Home</a></li><li>Certifications</li></ul>
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
        {img("certifications-at-work.jpg", "Servicing pipework on a commercial heat pump installation", 750, 1000)}
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
    <ul class="crumbs"><li><a href="index.html">Home</a></li><li>Contact</li></ul>
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
    <div class="sec-head reveal"><h2>Useful links.</h2></div>
    <div class="svc-grid">
      <a class="svc reveal" href="services.html">
        <div class="svc-watermark" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg></div>
        <h3>Services</h3><p>Installation, commissioning, service and repairs, aftersales maintenance.</p>
      </a>
      <a class="svc reveal" href="maintenance.html">
        <div class="svc-watermark" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 20h9"/><path d="M16.5 3.5a2.12 2.12 0 0 1 3 3L7 19l-4 1 1-4Z"/></svg></div>
        <h3>Annual maintenance</h3><p>What your yearly visit includes and what's chargeable.</p>
      </a>
      <a class="svc reveal" href="certifications.html">
        <div class="svc-watermark" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg></div>
        <h3>Certifications</h3><p>F-GAS, QQI Level 6, R290 training, Safety Statement and insurance.</p>
      </a>
      <a class="svc reveal" href="contact.html">
        <div class="svc-watermark" aria-hidden="true">{ICON_PHONE}</div>
        <h3>Contact</h3><p>Phone, WhatsApp, email and a callback form.</p>
      </a>
    </div>
  </div>
</section>
"""


# ============================================================ BUILD
if __name__ == "__main__":
    page("index.html",
         "Heat Pump Installation & Service, Sligo | Irish Air to Water",
         "Air-to-water heat pump specialist. Installation, commissioning, service and aftersales maintenance. F-GAS registered, Sligo-based, covering all of Ireland.",
         HOME)

    page("services.html",
         "Heat Pump Services, Sligo & Nationwide | Irish Air to Water",
         "Air-to-water heat pump installation, commissioning, service and repairs, and aftersales maintenance. Domestic and commercial, Sligo-based, all of Ireland.",
         SERVICES)

    page("maintenance.html",
         "Annual Heat Pump Maintenance Visit | Irish Air to Water",
         "What's included in your annual air-to-water heat pump maintenance visit and what's chargeable. F-Gas certified engineer, written service record.",
         MAINTENANCE, extra_schema=[faq_schema(MAINT_FAQS)])

    page("certifications.html",
         "Certifications & Insurance | Irish Air to Water",
         "F-GAS registered, QQI Level 6 in Refrigeration and Air Conditioning, Grant R290 trained, Safety Statement and Combined Liability insurance.",
         CERTIFICATIONS)

    page("404.html",
         "Page not found | Irish Air to Water",
         "That page doesn't exist. Head back to the homepage or call 087 341 3114.",
         NOT_FOUND)

    page("contact.html",
         "Contact | Irish Air to Water Heat Pump Specialists, Sligo",
         "Call 087 341 3114, WhatsApp or email. Air-to-water heat pump installation, commissioning, service and repairs. Sligo-based, covering all of Ireland.",
         CONTACT)
