# -*- coding: utf-8 -*-
"""
Keeps the shared chrome (head, nav, footer) identical across every page.

There is no build step for this site: the HTML files are the site. This script
just rewrites the shared blocks in place, so the six pages cannot drift apart.
Run it after changing NAV, FOOTER or the <head> block:

    python _build.py
"""
import re, glob, time, io, os
import _seo

VERSION = time.strftime("%Y%m%d%H%M%S")

PAGES = [
    ("index.html",      "home",       "Home"),
    ("schools.html",    "schools",    "Schools"),
    ("foundation.html", "foundation", "Foundation"),
    ("volunteer.html",  "volunteer",  "Volunteer"),
    ("story.html",      "story",      "Our Story"),
    ("contact.html",    "contact",    "Contact"),
    ("privacy.html",    "privacy",    None),          # footer link only
]

def head(fname):
    """The whole <head> for a page, from the SEO config."""
    return _seo.head_tags(fname, _seo.PAGES[fname], VERSION)


def schema_block(fname, extra=None):
    """One <script type=application/ld+json> holding the page's whole @graph."""
    return ('<script type="application/ld+json">\n'
            + _seo.graph_for(fname, _seo.PAGES[fname], extra)
            + '\n</script>')


def nav(current):
    links = []
    for f, key, label in PAGES:
        if not label:
            continue
        cur = ' aria-current="page"' if key == current else ""
        links.append(f'      <a href="{f}"{cur}>{label}</a>')
    return ("""<header class="nav" role="banner">
  <a class="nav__brand" href="index.html">
    <img class="nav__logo" src="assets/yaadhum-logo-cut.png" alt="">
    <span class="nav__wordmark">Project Yaadhum</span>
  </a>
  <div class="nav__right">
    <button class="nav__toggle" type="button" aria-expanded="false" aria-controls="nav-links"
            aria-label="Open menu">
      <span class="nav__bars" aria-hidden="true"></span>
      <span class="nav__togglelab">Menu</span>
    </button>
    <nav class="nav__links" id="nav-links" aria-label="Primary">
"""
            + "\n".join(links)
            + """
    </nav>
  </div>
</header>""")

SOCIALS = """<div class="socials" aria-label="Social links">
          <a href="https://www.linkedin.com/company/projectyaadhum/" target="_blank" rel="noopener" aria-label="Project Yaadhum on LinkedIn"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5zM3 9h4v12H3V9zm7 0h3.8v1.7h.05c.53-1 1.83-2.05 3.77-2.05 4.03 0 4.78 2.65 4.78 6.1V21h-4v-5.5c0-1.3-.03-3-1.83-3-1.83 0-2.11 1.43-2.11 2.9V21h-4V9z"/></svg></a>
          <a href="https://www.instagram.com/projectyaadhum/" target="_blank" rel="noopener" aria-label="Project Yaadhum on Instagram"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.2c3.2 0 3.6 0 4.85.07 1.17.05 1.8.25 2.23.41.56.22.96.48 1.38.9.42.42.68.82.9 1.38.16.42.36 1.06.41 2.23.06 1.25.07 1.62.07 4.82s0 3.57-.07 4.82c-.05 1.17-.25 1.8-.41 2.23-.22.56-.48.96-.9 1.38-.42.42-.82.68-1.38.9-.42.16-1.06.36-2.23.41-1.25.06-1.62.07-4.85.07s-3.6 0-4.85-.07c-1.17-.05-1.8-.25-2.23-.41a3.7 3.7 0 0 1-1.38-.9 3.7 3.7 0 0 1-.9-1.38c-.16-.42-.36-1.06-.41-2.23C2.2 15.6 2.2 15.2 2.2 12s0-3.57.07-4.82c.05-1.17.25-1.8.41-2.23.22-.56.48-.96.9-1.38.42-.42.82-.68 1.38-.9.42-.16 1.06-.36 2.23-.41C8.4 2.2 8.8 2.2 12 2.2zm0 1.8c-3.15 0-3.5 0-4.74.07-.9.04-1.38.19-1.7.32-.43.16-.73.36-1.05.68-.32.32-.52.62-.68 1.05-.13.32-.28.8-.32 1.7C3.24 8.5 3.24 8.85 3.24 12s0 3.5.07 4.74c.04.9.19 1.38.32 1.7.16.43.36.73.68 1.05.32.32.62.52 1.05.68.32.13.8.28 1.7.32 1.24.07 1.59.07 4.74.07s3.5 0 4.74-.07c.9-.04 1.38-.19 1.7-.32.43-.16.73-.36 1.05-.68.32-.32.52-.62.68-1.05.13-.32.28-.8.32-1.7.07-1.24.07-1.59.07-4.74s0-3.5-.07-4.74c-.04-.9-.19-1.38-.32-1.7a2.8 2.8 0 0 0-.68-1.05 2.8 2.8 0 0 0-1.05-.68c-.32-.13-.8-.28-1.7-.32C15.5 4 15.15 4 12 4zm0 3.06A4.94 4.94 0 1 1 12 17a4.94 4.94 0 0 1 0-9.88zm0 1.8a3.14 3.14 0 1 0 0 6.28 3.14 3.14 0 0 0 0-6.28zM17.34 6a1.15 1.15 0 1 1 0 2.3 1.15 1.15 0 0 1 0-2.3z"/></svg></a>
          <a href="https://www.facebook.com/share/1XpGHpxK6S/" target="_blank" rel="noopener" aria-label="Project Yaadhum on Facebook"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M13.5 21v-8h2.7l.4-3.1h-3.1V7.9c0-.9.25-1.5 1.55-1.5H17V3.6c-.3-.04-1.3-.13-2.46-.13-2.43 0-4.1 1.48-4.1 4.21v2.35H7.7V13h2.74v8h3.06z"/></svg></a>
          <!-- WhatsApp: add back here once there is a number, e.g. https://wa.me/91XXXXXXXXXX -->
        </div>"""

FOOTER = """<footer class="footer" role="contentinfo">
  <div class="wrap">
    <div class="footer__top">
      <div>
        <div class="footer__brand">
          <span class="footer__logo-tile"><img src="assets/logo-square.png" alt="Project Yaadhum"></span>
          <span>Project Yaadhum</span>
        </div>
        <p class="footer__tag">Field research on how students in small-town Tamil&nbsp;Nadu arrive at their stream and pathway decisions, and the small free programmes we build from what we find.</p>
      </div>
      <div>
        <h4>The work</h4>
        <ul class="footer__links">
          <li><a href="index.html">Home</a></li>
          <li><a href="schools.html">Yaadhum Schools</a></li>
          <li><a href="foundation.html">Yaadhum Foundation</a></li>
          <li><a href="volunteer.html">Volunteer</a></li>
        </ul>
      </div>
      <div>
        <h4>About</h4>
        <ul class="footer__links">
          <li><a href="story.html">Our Story</a></li>
          <li><a href="contact.html">Contact</a></li>
          <li><a href="mailto:komala@projectyaadhum.com">komala@projectyaadhum.com</a></li>
        </ul>
        """ + SOCIALS + """
      </div>
    </div>
    <div class="footer__bottom">
      <span class="footer__meta">Project Yaadhum · Cuddalore, Tamil Nadu · est. 2025</span>
      <a href="privacy.html">How we handle student information</a>
    </div>
  </div>
</footer>"""

def page(fname, current, body, body_class="", schema_extra=None):
    cls = f' class="{body_class}"' if body_class else ""
    html = f"""<!doctype html>
<html lang="en-IN">
<head>
{head(fname)}
{schema_block(fname, schema_extra)}
</head>
<body{cls}>

{nav(current)}

{body}

{FOOTER}

<script src="js/main.js?v={VERSION}"></script>
</body>
</html>
"""
    open(fname, "w", encoding="utf-8").write(html)
    return fname


def restamp(fname):
    """Refresh the shared chrome + head + schema inside an existing page."""
    s = open(fname, encoding="utf-8").read()
    key = dict((f, k) for f, k, _ in PAGES)[os.path.basename(fname)]

    # <head>: replace wholesale, but keep any page-specific schema already there
    extra = None
    m = re.search(r'<script type="application/ld\+json" data-extra>(.*?)</script>', s, re.S)
    if m:
        extra = m.group(0)
    new_head = head(fname) + "\n" + schema_block(fname)
    if extra:
        new_head += "\n" + extra
    s = re.sub(r'<head>.*?</head>',
               lambda _m: "<head>\n" + new_head + "\n</head>", s, flags=re.S)

    s = re.sub(r'<html[^>]*>', '<html lang="en-IN">', s, count=1)
    s = re.sub(r'<header class="nav".*?</header>', nav(key), s, flags=re.S)
    s = re.sub(r'<footer class="footer".*?</footer>', FOOTER, s, flags=re.S)
    s = re.sub(r'src="js/main\.js(\?v=[\d]+)?"', f'src="js/main.js?v={VERSION}"', s)
    open(fname, "w", encoding="utf-8").write(s)


if __name__ == "__main__":
    for f, _, _ in PAGES:
        if os.path.exists(f):
            restamp(f)
            print("restamped", f)
    print("version", VERSION)
