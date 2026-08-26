#!/usr/bin/env python3
"""Verify links, anchors and JSON-LD across the built site."""
import re, json, pathlib, html, sys

ROOT = pathlib.Path(__file__).parent
pages = sorted(ROOT.glob("*.html"))
names = {p.name for p in pages}
errors, warnings = [], []

anchors = {}
for p in pages:
    t = p.read_text(encoding="utf-8")
    anchors[p.name] = set(re.findall(r'id="([^"]+)"', t))

for p in pages:
    t = p.read_text(encoding="utf-8")

    # links
    for href in re.findall(r'href="([^"]+)"', t):
        if href.startswith(("http", "mailto:", "tel:", "#")):
            if href.startswith("#") and href[1:] not in anchors[p.name]:
                errors.append(f"{p.name}: dead in-page anchor {href}")
            continue
        target, _, frag = href.partition("#")
        target = target.split("?")[0]  # strip cache-bust query
        if target and not target.endswith(".html"):
            # static asset (css, js, favicon, image)
            if not (ROOT / target).exists():
                errors.append(f"{p.name}: missing asset {target}")
            continue
        if target and target not in names:
            errors.append(f"{p.name}: link to missing page {target}")
        elif frag and target in names and frag not in anchors[target]:
            errors.append(f"{p.name}: link {href} -> anchor #{frag} not found in {target}")

    # json-ld valid
    for block in re.findall(r'<script type="application/ld\+json">(.*?)</script>', t, re.S):
        try:
            json.loads(block)
        except Exception as e:
            errors.append(f"{p.name}: invalid JSON-LD ({e})")

    # required meta
    for tag in ['name="description"', 'rel="canonical"', 'property="og:title"', '<title>']:
        if tag not in t:
            errors.append(f"{p.name}: missing {tag}")

    # title length
    title = re.search(r"<title>(.*?)</title>", t, re.S)
    if title and len(title.group(1)) > 70:
        warnings.append(f"{p.name}: title {len(title.group(1))} chars (>70, may truncate in SERPs)")
    desc = re.search(r'name="description" content="(.*?)"', t, re.S)
    if desc and len(desc.group(1)) > 165:
        warnings.append(f"{p.name}: meta description {len(desc.group(1))} chars (>165)")

    # accessibility basics
    if 'class="skip-link"' not in t:
        errors.append(f"{p.name}: missing skip link")
    if t.count("<h1") != 1:
        errors.append(f"{p.name}: has {t.count('<h1')} h1 tags, expected 1")
    for btn in re.findall(r'<button[^>]*class="faq-q"[^>]*>', t):
        if "aria-expanded" not in btn or "aria-controls" not in btn:
            errors.append(f"{p.name}: faq button missing aria attributes")
    if 'aria-label="Menu"' not in t:
        errors.append(f"{p.name}: nav toggle missing aria-label")

    # unescaped stray characters in visible text
    if "&aacute;" not in t and "Dáire" not in t:
        warnings.append(f"{p.name}: no Dáire reference found")

print(f"Pages checked: {len(pages)}")
for w in warnings:
    print("WARN ", w)
for e in errors:
    print("ERROR", e)
print("\nRESULT:", "FAIL" if errors else "PASS")
sys.exit(1 if errors else 0)
