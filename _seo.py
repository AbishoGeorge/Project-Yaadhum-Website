# -*- coding: utf-8 -*-
"""
SEO / AEO / GEO configuration, in one place.

Implements the package prepared 19 August 2026. Two things are deliberate:

* URLs keep their .html extensions, because that is what this static site
  actually serves. The package explicitly allows this ("keeping .html is
  acceptable and costs nothing measurable") provided one form is canonical.
* No `sameAs`, and no `affiliation` for the UN / Ministry of Education /
  Naan Mudhalvan. Those are volunteer mentoring roles held by individuals;
  asserting organisational affiliation in schema would contradict the site's
  own disclaimer and manufacture a claim nobody can support.

Change DOMAIN here and every canonical, og:url and @id follows.
"""

DOMAIN = "https://www.projectyaadhum.com"

ORG_ID      = DOMAIN + "/#organization"
WEBSITE_ID  = DOMAIN + "/#website"
LOGO_ID     = DOMAIN + "/#logo"
KOMALA_ID   = DOMAIN + "/story.html#komala-maran"
ABISHO_ID   = DOMAIN + "/story.html#abisho-george"

# the footer sentence, repeated on every page, is the canonical short description
SHORT_DESC = ("Field research on how students in small-town Tamil Nadu arrive at their "
              "stream and pathway decisions, and the small free programmes we build "
              "from what we find.")

LONG_DESC = ("Project Yaadhum is a field research initiative studying how students in "
             "Tier 2 and Tier 3 Tamil Nadu schools arrive at their stream and pathway "
             "decisions after Class 10, and who actually makes those decisions. It runs "
             "small, free pilot programmes with schools and communities based on what "
             "the fieldwork finds.")

# ---------------------------------------------------------------- per page --
PAGES = {
    "index.html": dict(
        path="/",
        title="Project Yaadhum: How Tamil Nadu Students Choose a Stream",
        desc=("Field research in Tier 2 and Tier 3 Tamil Nadu schools. Of every 100 students, "
              "66 enter science and 2 choose arts. We went to find out why."),
        og_title="How does a fifteen-year-old in Tamil Nadu end up in the science stream?",
        og_desc=("Of every hundred Tamil Nadu students, about 66 enter science and 2 choose arts. "
                 "Nobody has written down how that decision actually gets made. We went to find out."),
        page_type="WebPage",
    ),
    "schools.html": dict(
        path="/schools.html",
        title="Free Classroom Pilot for Schools | Project Yaadhum",
        desc=("One class, about 45 minutes of one period, no fee now or later. We shape a short "
              "research pilot around the transition problem your school is already seeing."),
        og_title="Bring the research into one of your classrooms",
        og_desc=("One section, about 45 minutes of one period, and an honest conversation "
                 "afterwards. There is no fee, now or later."),
        page_type="WebPage",
    ),
    "foundation.html": dict(
        path="/foundation.html",
        title="Free Community Programmes, Tamil Nadu | Project Yaadhum",
        desc=("Free programmes for students in Classes 9 to 12 and their families, run with colleges "
              "and local partners in Tier 2 and Tier 3 Tamil Nadu. Parents included."),
        og_title="For the students a school will never reach",
        og_desc=("One family hears about an examination in Class 9. Another finds out after Class 12. "
                 "Free community programmes for students and parents together."),
        page_type="WebPage",
    ),
    "volunteer.html": dict(
        path="/volunteer.html",
        title="Volunteer: Education Fieldwork in Tamil Nadu | Yaadhum",
        desc=("For college students, B.Ed students and recent graduates, 18 or older, anywhere in "
              "Tamil Nadu. Training in interviewing, consent and safeguarding included."),
        og_title="Do the fieldwork. Help a student understand what comes next.",
        og_desc=("Sit with someone. Listen properly. Write down what was actually said. Open to "
                 "students and recent graduates anywhere in Tamil Nadu."),
        page_type="WebPage",
    ),
    "story.html": dict(
        path="/story.html",
        title="Our Story: Why Project Yaadhum Exists | Founder's Note",
        desc=("Komala Maran finished ten years of school without knowing JEE existed. One conversation "
              "changed that. The question that started Project Yaadhum, in her words."),
        og_title="A question we could not put down: why Project Yaadhum exists",
        og_desc=("Komala Maran finished ten years of school without knowing JEE existed. Abisho George "
                 "lost a seat on a date he did not know existed. Both notes, in full."),
        page_type="AboutPage",
    ),
    "contact.html": dict(
        path="/contact.html",
        title="Contact Project Yaadhum | Cuddalore, Tamil Nadu",
        desc=("Email komala@projectyaadhum.com or write to us from here. We reply to every message "
              "ourselves. No mailing list, no autoresponder. Cuddalore, Tamil Nadu."),
        og_title="Contact Project Yaadhum",
        og_desc=("We want to hear from anyone who has watched this decision get made up close. "
                 "Cuddalore, Tamil Nadu."),
        page_type="ContactPage",
    ),
    "privacy.html": dict(
        path="/privacy.html",
        title="How We Handle Student Information | Project Yaadhum",
        desc=("What we collect, why, who sees it, and how long we keep it. Parent consent before any "
              "minor takes part, and anything published is anonymised."),
        og_title="How we handle student information",
        og_desc="Written as a promise to a parent, not as terms and conditions.",
        page_type="WebPage",
    ),
}

# --------------------------------------------------------------- JSON-LD ----
import json

def _org():
    return {
        "@type": "NGO",
        "@id": ORG_ID,
        "name": "Project Yaadhum",
        "legalName": "Yaadhum Foundation",
        "alternateName": ["Yaadhum", "Yaadhum Foundation"],
        "url": DOMAIN + "/",
        "logo": {"@type": "ImageObject", "@id": LOGO_ID,
                 "url": DOMAIN + "/assets/logo-square.png",
                 "width": 512, "height": 512, "caption": "Project Yaadhum"},
        "image": {"@id": LOGO_ID},
        "slogan": "Every possibility belongs to every student.",
        "description": LONG_DESC,
        "foundingDate": "2025",
        "founder": {"@id": KOMALA_ID},
        "member": [{"@id": KOMALA_ID}, {"@id": ABISHO_ID}],
        "email": "komala@projectyaadhum.com",
        "address": {"@type": "PostalAddress", "addressLocality": "Cuddalore",
                    "addressRegion": "Tamil Nadu", "addressCountry": "IN"},
        "areaServed": {"@type": "AdministrativeArea", "name": "Tamil Nadu, India"},
        "knowsAbout": ["Academic stream selection after Class 10",
                       "Education access in Tier 2 and Tier 3 India",
                       "School-to-higher-education transition",
                       "Field research in schools",
                       "Student career awareness"],
        "contactPoint": {"@type": "ContactPoint", "@id": DOMAIN + "/#contact-point",
                         "email": "komala@projectyaadhum.com",
                         "contactType": "General enquiries",
                         "areaServed": "IN", "availableLanguage": ["en", "ta"]},
        # only profiles that actually resolve; an unresolving sameAs is worse than none
        "sameAs": ["https://www.linkedin.com/company/projectyaadhum/",
                   "https://www.instagram.com/projectyaadhum/",
                   "https://www.facebook.com/share/1XpGHpxK6S/"],
    }

def _website():
    return {"@type": "WebSite", "@id": WEBSITE_ID, "url": DOMAIN + "/",
            "name": "Project Yaadhum", "description": SHORT_DESC,
            "publisher": {"@id": ORG_ID}, "inLanguage": "en-IN"}

def _people():
    komala = {
        "@type": "Person", "@id": KOMALA_ID, "name": "Komala Maran",
        "givenName": "Komala", "familyName": "Maran", "jobTitle": "Founder",
        "worksFor": {"@id": ORG_ID}, "founderOf": {"@id": ORG_ID},
        "alumniOf": {"@type": "CollegeOrUniversity",
                     "name": "Indian Institute of Information Technology, Allahabad",
                     "sameAs": "https://iiita.ac.in/"},
        "description": ("Founder of Project Yaadhum. Studied at IIIT Allahabad and spent seven years "
                        "in strategy consulting. Mentors school and college students as a volunteer "
                        "through Naan Mudhalvan (TNSkill Corporation) and the Ministry of Education's "
                        "Vidyanjali programme."),
        "knowsAbout": ["Academic stream selection after Class 10",
                       "Education access in Tier 2 and Tier 3 India",
                       "Strategy consulting", "Student mentoring"],
        "knowsLanguage": ["en", "ta"],
        "email": "komala@projectyaadhum.com",
        "image": DOMAIN + "/assets/founder-komala.jpg",
        "url": DOMAIN + "/story.html",
    }
    abisho = {
        "@type": "Person", "@id": ABISHO_ID, "name": "Abisho George",
        "givenName": "Abisho", "familyName": "George", "jobTitle": "Founding Member",
        "worksFor": {"@id": ORG_ID}, "memberOf": {"@id": ORG_ID},
        "description": ("Founding member of Project Yaadhum. Mentors school and college students as a "
                        "volunteer through Naan Mudhalvan and the Ministry of Education's Vidyanjali "
                        "programme."),
        "knowsAbout": ["Academic stream selection after Class 10",
                       "Education access in Tier 2 and Tier 3 India", "Student mentoring"],
        "knowsLanguage": ["en", "ta"],
        "image": DOMAIN + "/assets/founding-abisho.jpg?v=2",
        "url": DOMAIN + "/story.html",
    }
    return [komala, abisho]

def _webpage(fname, cfg):
    url = DOMAIN + cfg["path"]
    node = {"@type": cfg["page_type"], "@id": url + "#webpage", "url": url,
            "name": cfg["title"], "description": cfg["desc"],
            "isPartOf": {"@id": WEBSITE_ID},
            "about": {"@id": ORG_ID},
            "publisher": {"@id": ORG_ID},
            "inLanguage": "en-IN"}
    if fname == "index.html":
        node["primaryImageOfPage"] = {"@id": LOGO_ID}
    if fname == "story.html":
        node["mainEntity"] = [{"@id": KOMALA_ID}, {"@id": ABISHO_ID}]
    return node

def graph_for(fname, cfg, extra=None):
    """The whole page's structured data as one @graph, so every node is linked."""
    nodes = [_org(), _website(), _webpage(fname, cfg)]
    if fname == "story.html":
        nodes += _people()
    if extra:
        nodes += extra
    return json.dumps({"@context": "https://schema.org", "@graph": nodes},
                      indent=2, ensure_ascii=False)

def head_tags(fname, cfg, version):
    """Everything that belongs in <head> for this page."""
    url = DOMAIN + cfg["path"]
    og_img = DOMAIN + "/assets/og-image.png"
    return f"""<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{cfg['title']}</title>
<meta name="description" content="{cfg['desc']}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">

<meta property="og:type" content="website">
<meta property="og:site_name" content="Project Yaadhum">
<meta property="og:locale" content="en_IN">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{cfg['og_title']}">
<meta property="og:description" content="{cfg['og_desc']}">
<meta property="og:image" content="{og_img}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Project Yaadhum. Every possibility belongs to every student.">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{cfg['og_title']}">
<meta name="twitter:description" content="{cfg['og_desc']}">
<meta name="twitter:image" content="{og_img}">

<link rel="icon" href="assets/favicon-32.png" sizes="32x32">
<link rel="apple-touch-icon" href="assets/favicon-180.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300..600;1,9..144,300..600&family=IBM+Plex+Mono:wght@400;500&family=Inter:wght@300;400;500;600&family=Noto+Serif+Tamil:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/main.css?v={version}">"""
