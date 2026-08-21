# -*- coding: utf-8 -*-
import _build as B

MOVED = open("_parts/story.html", encoding="utf-8").read()
MOVED = MOVED.replace('</main>', '')

HEAD = """<main class="subpage">

  <!-- ============================ HERO ============================ -->
  <section class="contact-hero">
    <div class="wrap">
      <div class="head-split head-split--top">
        <div>
          <h1 class="reveal">A question we could not put down. <em class="h1__beat">Why Project&nbsp;Yaadhum exists.</em></h1>
          <p class="schools__lede reveal" style="color:var(--ink-2);max-width:56ch">Project Yaadhum began with something we kept watching happen and could not explain: two equally capable students, the same school, entirely different futures. Nobody could tell us why. So we went to find out properly.</p>
        </div>
        <figure class="calviz reveal" data-delay="1"
                aria-label="A term of ordinary days, with the one deadline that decided everything circled late.">
          <svg viewBox="0 0 332 236" role="img">
            <path class="cal-rule" d="M24 32h284"/>
            <path class="cal-tick" d="M40 20v7"/>
            <path class="cal-tick" d="M82 20v7"/>
            <path class="cal-tick" d="M124 20v7"/>
            <path class="cal-tick" d="M166 20v7"/>
            <path class="cal-tick" d="M208 20v7"/>
            <path class="cal-tick" d="M250 20v7"/>
            <path class="cal-tick" d="M292 20v7"/>
            <rect class="cal-day" x="24" y="44" width="32" height="26" rx="5" style="transition-delay:0ms"/>
            <rect class="cal-day" x="66" y="44" width="32" height="26" rx="5" style="transition-delay:16ms"/>
            <rect class="cal-day" x="108" y="44" width="32" height="26" rx="5" style="transition-delay:32ms"/>
            <rect class="cal-day" x="150" y="44" width="32" height="26" rx="5" style="transition-delay:48ms"/>
            <rect class="cal-day" x="192" y="44" width="32" height="26" rx="5" style="transition-delay:64ms"/>
            <rect class="cal-day" x="234" y="44" width="32" height="26" rx="5" style="transition-delay:80ms"/>
            <rect class="cal-day" x="276" y="44" width="32" height="26" rx="5" style="transition-delay:96ms"/>
            <rect class="cal-day" x="24" y="79" width="32" height="26" rx="5" style="transition-delay:112ms"/>
            <rect class="cal-day" x="66" y="79" width="32" height="26" rx="5" style="transition-delay:128ms"/>
            <rect class="cal-day" x="108" y="79" width="32" height="26" rx="5" style="transition-delay:144ms"/>
            <rect class="cal-day" x="150" y="79" width="32" height="26" rx="5" style="transition-delay:160ms"/>
            <rect class="cal-day" x="192" y="79" width="32" height="26" rx="5" style="transition-delay:176ms"/>
            <rect class="cal-day" x="234" y="79" width="32" height="26" rx="5" style="transition-delay:192ms"/>
            <rect class="cal-day" x="276" y="79" width="32" height="26" rx="5" style="transition-delay:208ms"/>
            <rect class="cal-day" x="24" y="114" width="32" height="26" rx="5" style="transition-delay:224ms"/>
            <rect class="cal-day" x="66" y="114" width="32" height="26" rx="5" style="transition-delay:240ms"/>
            <rect class="cal-day" x="108" y="114" width="32" height="26" rx="5" style="transition-delay:256ms"/>
            <rect class="cal-day" x="150" y="114" width="32" height="26" rx="5" style="transition-delay:272ms"/>
            <rect class="cal-day cal-day--the" x="192" y="114" width="32" height="26" rx="5" style="transition-delay:288ms"/>
            <rect class="cal-day" x="234" y="114" width="32" height="26" rx="5" style="transition-delay:304ms"/>
            <rect class="cal-day" x="276" y="114" width="32" height="26" rx="5" style="transition-delay:320ms"/>
            <rect class="cal-day" x="24" y="149" width="32" height="26" rx="5" style="transition-delay:336ms"/>
            <rect class="cal-day" x="66" y="149" width="32" height="26" rx="5" style="transition-delay:352ms"/>
            <rect class="cal-day" x="108" y="149" width="32" height="26" rx="5" style="transition-delay:368ms"/>
            <rect class="cal-day" x="150" y="149" width="32" height="26" rx="5" style="transition-delay:384ms"/>
            <rect class="cal-day" x="192" y="149" width="32" height="26" rx="5" style="transition-delay:400ms"/>
            <rect class="cal-day" x="234" y="149" width="32" height="26" rx="5" style="transition-delay:416ms"/>
            <rect class="cal-day" x="276" y="149" width="32" height="26" rx="5" style="transition-delay:432ms"/>
            <rect class="cal-day" x="24" y="184" width="32" height="26" rx="5" style="transition-delay:448ms"/>
            <rect class="cal-day" x="66" y="184" width="32" height="26" rx="5" style="transition-delay:464ms"/>
            <rect class="cal-day" x="108" y="184" width="32" height="26" rx="5" style="transition-delay:480ms"/>
            <rect class="cal-day" x="150" y="184" width="32" height="26" rx="5" style="transition-delay:496ms"/>
            <rect class="cal-day" x="192" y="184" width="32" height="26" rx="5" style="transition-delay:512ms"/>
            <rect class="cal-day" x="234" y="184" width="32" height="26" rx="5" style="transition-delay:528ms"/>
            <rect class="cal-day" x="276" y="184" width="32" height="26" rx="5" style="transition-delay:544ms"/>
            <ellipse class="cal-ring" cx="208" cy="127" rx="27" ry="21"
                     transform="rotate(-8 208 127)"/>
          </svg>
          <figcaption>A term of ordinary days. <b>One of them was a deadline.</b> Nobody in the room knew which.</figcaption>
        </figure>
      </div>
    </div>
  </section>

  <!-- ===================== MISSION & VISION ======================= -->
  <section class="section section--paper">
    <div class="wrap">
      <div class="mv">
        <article class="mv__card reveal">
          <div class="mv__ico" aria-hidden="true">
            <svg viewBox="0 0 48 48">
              <circle cx="24" cy="24" r="16"/>
              <circle cx="24" cy="24" r="9"/>
              <circle class="fill" cx="24" cy="24" r="3"/>
              <path class="hi" d="M24 3v7M24 38v7M3 24h7M38 24h7"/>
            </svg>
          </div>
          <p class="mv__k">Our mission</p>
          <h2 class="mv__t">To write down how this decision is really made, and to hand it back to the people making it.</h2>
          <p class="mv__s">Every year, families choose a stream in a matter of weeks, on marks, hope and whatever information happened to reach them. We are building the first honest record of that process, school by school, and using it to make the next decision a little better informed than the last.</p>
        </article>

        <article class="mv__card reveal" data-delay="1">
          <div class="mv__ico" aria-hidden="true">
            <svg viewBox="0 0 48 48">
              <path d="M4 26c6-11 14-16 20-16s14 5 20 16"/>
              <path d="M4 26c6 11 14 16 20 16s14-5 20-16"/>
              <circle cx="24" cy="26" r="7"/>
              <circle class="fill" cx="24" cy="26" r="2.6"/>
              <path class="hi" d="M33 12l6-6M39 6h-5M39 6v5"/>
            </svg>
          </div>
          <p class="mv__k">Our vision</p>
          <h2 class="mv__t">A student&rsquo;s possibilities decided by what they are capable of, not by where they were born.</h2>
          <p class="mv__s">A Tamil line two thousand years old says every town is our own and every person our kin. We took it as a premise rather than a slogan. If that is true, then the district a child grows up in should not quietly decide which doors are open to them, and that is a claim you can go and check.</p>
        </article>
      </div>
    </div>
  </section>

"""

TAIL = "</main>"

B.page("story.html", "story", HEAD + MOVED + TAIL)
print("story page rebuilt with mission and vision")
