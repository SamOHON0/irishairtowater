import asyncio, pathlib
from playwright.async_api import async_playwright

ROOT = pathlib.Path(__file__).parent
OUT = ROOT / "_shots"
OUT.mkdir(exist_ok=True)
PAGES = ["index", "services", "maintenance", "certifications", "contact", "404"]

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/opt/pw-browsers/chromium")
        errs = []

        # desktop full page
        ctx = await b.new_context(viewport={"width": 1440, "height": 1000})
        pg = await ctx.new_page()
        pg.on("console", lambda m: errs.append(f"{m.type}: {m.text}") if m.type == "error" else None)
        pg.on("pageerror", lambda e: errs.append(f"pageerror: {e}"))
        for name in PAGES:
            await pg.goto(f"file://{ROOT}/{name}.html")
            await pg.wait_for_timeout(700)
            h = await pg.evaluate("document.body.scrollHeight")
            y = 0
            while y < h:
                await pg.evaluate(f"window.scrollTo(0,{y})")
                await pg.wait_for_timeout(140)
                y += 700
            await pg.evaluate("window.scrollTo(0,0)")
            # force lazy images to load and reveals to settle so the
            # stitched full-page capture is truthful
            await pg.evaluate("document.querySelectorAll('img[loading=lazy]').forEach(i=>i.loading='eager')")
            try:
                await pg.wait_for_function(
                    "Array.from(document.images).every(i=>i.complete)", timeout=8000)
            except Exception:
                pass
            await pg.evaluate(
                "Promise.all(Array.from(document.images).map(i=>i.decode().catch(()=>{})))")
            # force final state so the stitched full-page capture is truthful
            await pg.evaluate("document.querySelectorAll('.reveal').forEach(e=>{e.classList.add('in');e.style.transition='none';e.style.opacity='1';e.style.transform='none'})")
            await pg.wait_for_timeout(400)
            await pg.screenshot(path=str(OUT / f"{name}-desktop.png"), full_page=True)
        await ctx.close()

        # mobile
        ctx = await b.new_context(viewport={"width": 390, "height": 844}, device_scale_factor=2)
        pg = await ctx.new_page()
        for name in PAGES:
            await pg.goto(f"file://{ROOT}/{name}.html")
            await pg.wait_for_timeout(700)
            await pg.screenshot(path=str(OUT / f"{name}-mobile.png"))
            # horizontal overflow check
            ow = await pg.evaluate("document.documentElement.scrollWidth")
            if ow > 391:
                errs.append(f"{name}: horizontal overflow, scrollWidth={ow}")

        # mobile nav open
        await pg.goto(f"file://{ROOT}/index.html")
        await pg.wait_for_timeout(500)
        await pg.click(".nav-toggle")
        await pg.wait_for_timeout(400)
        open_ok = await pg.evaluate("document.getElementById('mobile-panel').classList.contains('open')")
        if not open_ok:
            errs.append("mobile nav did not open")
        await pg.screenshot(path=str(OUT / "nav-open-mobile.png"))

        # faq accordion
        await pg.goto(f"file://{ROOT}/maintenance.html")
        await pg.wait_for_timeout(500)
        await pg.click(".faq-q")
        await pg.wait_for_timeout(400)
        faq_ok = await pg.evaluate("document.querySelector('.faq-a').classList.contains('open')")
        if not faq_ok:
            errs.append("faq accordion did not open")

        # form submit handler
        await pg.goto(f"file://{ROOT}/contact.html")
        await pg.wait_for_timeout(500)
        await pg.fill("#f-name", "Test")
        await pg.fill("#f-phone", "0871234567")
        await pg.click('form[data-iatw-form] button[type=submit]')
        await pg.wait_for_timeout(400)
        label = await pg.inner_text('form[data-iatw-form] button[type=submit]')
        if "Sent" not in label:
            errs.append(f"form handler did not fire, button says: {label}")

        await ctx.close()
        await b.close()

        print("CONSOLE/INTERACTION ISSUES:", errs if errs else "none")

asyncio.run(main())
