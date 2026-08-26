# Photos

## In use

11 of Dáire's photos are live on the site, resized to max 1000px (hero 1200px),
re-encoded at quality 78-80, EXIF stripped. Total weight ~1.4MB, all lazy-loaded
except the hero.

| File | Where |
|---|---|
| hero-outdoor-unit.jpg | Home hero (eager, high priority) |
| installation-outdoor-unit.jpg | Home, Installation feature card |
| about-installed-unit.jpg | Home, About (Grant Aerona install) |
| coverage-home-install.jpg | Home, Coverage |
| services-installation.jpg | Services, Installation |
| services-commissioning-controls.jpg | Services, Commissioning (control board) |
| services-repairs-strainer-check.jpg | Services, Service & repairs (strainer check) |
| services-aftersales-filters.jpg | Services, Aftersales (filters out for cleaning) |
| maintenance-clear-access.jpg | Maintenance, "What we need from you" |
| certifications-at-work.jpg | Certifications, commercial plant-room work |
| contact-coverage-grant-unit.jpg | Contact, Coverage |
| og-image.jpg | Social share card, 1200x630 crop of the hero |

## Video and documents (now in use)

`media/brand-intro.mp4` (his 1156.mp4, 7s logo animation) is the hero, autoplay muted
loop with a poster; it pauses under prefers-reduced-motion. `media/customer-reviews.mp4`
(his 1167.mp4, 45s Facebook reviews carousel) sits in the reviews section, click to play.
Cert thumbnails in `images/cert-*.jpg` are rendered from the real documents. The
balancing image is cropped from his own LinkedIn explainer graphic.

## Still needed

1. **A photo of Dáire.** There isn't one in the batch. The About section says "One name
   on the van. One person responsible for your system" and currently sits beside a photo
   of a cleaned strainer in his hand. It works, but a face or a shot of him at the van
   would be much stronger. Same for the Certifications page.
2. **The van.** Nothing in the batch shows it.
3. **F-GAS registration and insurance certificate** scans, to replace the two icon
   tiles on the certifications page with real documents.
4. **A real manifold photo** eventually; the current image is from his explainer graphic.

## Image rules used on this site

Clean, finished installs carry the brand slots (hero, About, coverage). Work-in-progress
and diagnostic shots appear only beside copy about service work. Photos showing neglect
(algae-covered fans, dirty filters against a wall, the dirty strainer) are OFF the site:
out of context they read as poor workmanship, not expertise. They would only return
inside an explicitly labelled before/after block.

## Not used

Photos from the batch left unused and still sit in the repo root as `WhatsApp Image*`
files. They are gitignored, so they are not in the repo, but they are on disk:

- Two more sets of dirty filters (one on a driveway, one on gravel)
- The dirty strainer and the algae-covered fan unit. Paired with after shots these would
  make a strong labelled before/after block on the maintenance page.
- Two more Grant Aerona outdoor units
- A weathered twin-fan unit with algae on the casing
- A unit with a fitted cover, and one wrapped/frosted

Move or delete the raw `WhatsApp Image*` and `WhatsApp Video*` files from the repo root
whenever. Two videos are there too (`*.mp4`), also gitignored and unused.

## Adding one

Drop the file in this folder, then in `pages.py` replace the placeholder with:

```python
{img("filename.jpg", "Plain description of what is in the photo", WIDTH, HEIGHT)}
```

and run `python3 pages.py`. The `img()` helper in `build.py` adds lazy loading,
async decoding and the width/height attributes that stop layout shift.
