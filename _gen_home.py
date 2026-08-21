# -*- coding: utf-8 -*-
import _build as B

BODY = """<!-- ============================ HERO ============================ -->
<main>
<section class="hero" id="hero">
  <div class="hero__stage">
    <span class="hero__holder" aria-hidden="true"></span>
    <img class="hero__logo hero__logo--flow" src="assets/yaadhum-logo-cut.png" alt="Project Yaadhum, a student walking toward a lit doorway out of an open book">
    <p class="hero__tagline">Every possibility belongs to every student.</p>

    <div class="hero__partners-slot">
      <div class="hero__partners" aria-label="Where our team volunteers">
        <figure class="hpartner"><img src="assets/partner-un.png" alt="United Nations"><figcaption>United Nations</figcaption></figure>
        <figure class="hpartner"><img src="assets/partner-moe.png" alt="Ministry of Education, Government of India"><figcaption>Ministry of Education</figcaption></figure>
        <figure class="hpartner"><img src="assets/partner-tnskill.png" alt="Naan Mudhalvan, TNSkill Corporation"><figcaption>Naan Mudhalvan</figcaption></figure>
      </div>
    </div>
    <p class="hero__partners-note">Where our team volunteers as mentors</p>
  </div>
</section>
<img class="hero__logo hero__logo--fixed" src="assets/yaadhum-logo-cut.png" alt="" aria-hidden="true">

<!-- ================= THE QUESTION WE STARTED WITH =============== -->
<section class="section qband">
  <div class="wrap">
    <p class="qmark reveal">The question we started with</p>
    <div class="qband__grid">
      <h1 class="qband__q reveal">How does a fifteen-year-old in Tamil&nbsp;Nadu end up in the <em>science stream</em>?</h1>
      <p class="qband__sub reveal" data-delay="1">Sixty-six out of a hundred students here take that path. About two choose arts. Almost nobody has written down how that decision actually gets made, so we went to find out.</p>
    </div>
  </div>
</section>

<!-- the gap, lands differently -->
<section class="section gap">
  <div class="wrap">
    <div class="gap__pre reveal">
      <p><b>Learning platforms</b>ask how is this student learning.</p>
      <p><b>Assessments</b>ask what do the marks reveal.</p>
      <p><b>Guidance programmes</b>ask where is this student headed.</p>
    </div>
    <div class="head-split head-split--top">
      <div>
        <p class="gap__punch reveal" data-delay="1">Nobody asks <b>what needs to happen next for this student</b>: who is responsible, whether it happened, and whether it changed anything.</p>
        <p class="gap__sig reveal" data-delay="2">This is the reason the research exists.</p>
      </div>
      <div class="reveal" data-delay="2">
        <ul class="record">
          <li class="kept"><span class="pip" aria-hidden="true"></span>Marks and scores</li>
          <li><span class="pip" aria-hidden="true"></span>What someone noticed</li>
          <li><span class="pip" aria-hidden="true"></span>What they did about it</li>
          <li><span class="pip" aria-hidden="true"></span>Whether it happened</li>
          <li><span class="pip" aria-hidden="true"></span>Whether it changed anything</li>
          <li class="kept"><span class="pip" aria-hidden="true"></span>Final outcome</li>
        </ul>
        <p class="record__key">Filled: already recorded &nbsp;&middot;&nbsp; Hollow: nowhere to put it</p>
      </div>
    </div>
  </div>
</section>

<!-- ================= WHAT WE'RE DOING ABOUT IT ================== -->
<section class="section">
  <div class="wrap duo">
    <div class="duo__statement reveal">
      We are building the first honest record of how this decision <span class="accent">actually gets made</span> inside Tier&nbsp;2 and Tier&nbsp;3 schools.
    </div>
    <div class="duo__body reveal" data-delay="1">
      <h2 class="block-title">What we&rsquo;re doing about it</h2>
      <p>Who decides. What information reaches the family, and when it arrives. What it costs when it arrives late.</p>
      <p>Not a model. Not a survey. Fieldwork, school by school. We go and sit with principals, teachers, students and parents, and write down what is actually happening.</p>
      <p>Then we test small ways of responding to what we find, with schools and communities willing to try them while they are still being shaped.</p>
    </div>
  </div>
</section>

<!-- ============== WHAT WE BELIEVE, three beats on one screen ===== -->
<section class="section still">
  <div class="wrap">
    <div class="believe">
      <blockquote class="couplet reveal">
        <p class="couplet__ta" lang="ta">யாதும் ஊரே<br>யாவரும் கேளிர்</p>
        <p class="couplet__rom">Yaadhum oore, yaavarum kelir</p>
        <p class="couplet__en">Every town is our own.<br>Every person, our kin.</p>
        <p class="couplet__attr">Kaniyan Pungundranar &middot; Purananuru 192 &middot; Sangam era</p>
      </blockquote>

      <div class="still__passage reveal" data-delay="1">
        <h2 class="block-title">What we believe</h2>
        <p>We took the line as a premise rather than a slogan. If no accident of birth decides what belongs to whom, then the district a student was born in should not quietly decide which stream is available to them.</p>
        <p>That is a claim about the world that can be checked, school by school, and checking it is the work.</p>
      </div>

      <div class="believe__ours reveal" data-delay="2">
        <span class="believe__rule" aria-hidden="true"></span>
        <p class="believe__line">Every possibility belongs to every student.</p>
        <p class="believe__note">The same claim, narrowed to one thing we can actually go and check.</p>
      </div>
    </div>
  </div>
</section>

<!-- ======================= THE NUMBERS ========================= -->
<section class="section section--tint">
  <div class="wrap">
    <div class="head-split numbers__head">
      <h2 class="story__lead reveal" style="margin:0">A hundred students. Two chose arts.</h2>
      <p class="standfirst reveal" data-delay="1">This is the <b>public picture</b>, and it is the only part of this story already written down. Everything underneath it, how each of these students arrived where they did, is what we are in schools to find out.</p>
    </div>

    <div class="picture">
      <div class="roll reveal" aria-hidden="true"></div>
      <div class="picture__legend reveal" data-delay="1">
        <p class="mono" style="letter-spacing:.16em;color:var(--ink-3)">Of every hundred Tamil&nbsp;Nadu students</p>
        <div class="leg"><span class="leg__n">66</span><span class="leg__t">Enter science<small>the default path</small></span></div>
        <div class="leg"><span class="leg__n leg__n--art">2</span><span class="leg__t">Choose arts<small>the two marigold figures</small></span></div>
        <div class="leg"><span class="leg__n leg__n--else">32</span><span class="leg__t">Go elsewhere<small>commerce, vocational, out</small></span></div>
      </div>
    </div>
    <p class="picture__foot reveal">Nobody can tell you which of these places was chosen, and which was simply arrived at.</p>

    <!-- ============================================================
         FIELD NUMBERS, keep these true. Edit the data-count values;
         each counts up from 0 the first time it scrolls into view.
         ============================================================ -->
    <div class="field reveal">
      <div class="field__label">
        <span class="field__dot" aria-hidden="true"></span>
        <span class="mono">Our fieldwork so far &middot; in progress &middot; as of August 2026</span>
      </div>
      <div class="counters">
        <div><div class="counter__n" data-count="12">00</div><div class="counter__t">Schools mapped</div></div>
        <div><div class="counter__n" data-count="84">00</div><div class="counter__t">Interviews recorded</div></div>
        <div><div class="counter__n" data-count="5">00</div><div class="counter__t">Districts entered</div></div>
        <div><div class="counter__n" data-count="9">00</div><div class="counter__t">Researchers in field</div></div>
      </div>
    </div>
  </div>
</section>

<!-- ==================== WHERE THE RESEARCH GOES ================= -->
<section class="section">
  <div class="wrap">
    <div class="head-split head-split--top">
      <div class="reveal">
        <h2 class="duo__statement">Two ways the same findings reach a student.</h2>
      </div>
      <p class="standfirst reveal" data-delay="1">The research tells us how these decisions are really made. Both of the programmes below are small, free attempts to respond to what we find, tested with the people they are meant to help.</p>
    </div>

    <div class="routes">
      <a class="route reveal" href="schools.html">
        <span class="route__k">Yaadhum Schools</span>
        <span class="route__t">Inside one school, one class at a time</span>
        <span class="route__s">We shape a short pilot around the transition problem your school is already seeing, and share back everything we find. There is no fee.</span>
        <span class="route__go">How a pilot works</span>
      </a>
      <a class="route reveal" data-delay="1" href="foundation.html">
        <span class="route__k">Yaadhum Foundation</span>
        <span class="route__t">Beyond the schools that already say yes</span>
        <span class="route__s">Community programmes with colleges and local partners, for students and families who may never meet Yaadhum through a school at all.</span>
        <span class="route__go">About the Foundation</span>
      </a>
    </div>
  </div>
</section>

<!-- ================= WHERE ELSE WE DO THIS WORK ================= -->
<section class="section section--paper">
  <div class="wrap">
    <div class="head-split head-split--top">
      <div class="reveal">
        <h2 class="duo__statement">The same rooms, wearing someone else&rsquo;s badge.</h2>
      </div>
      <p class="standfirst reveal" data-delay="1">Long before Yaadhum, we were already mentoring students through three volunteer programmes. That work is what put us in front of the problem, and we are still doing it.</p>
    </div>

    <div class="mentors">
      <article class="mentor reveal">
        <div class="mentor__logo"><img src="assets/partner-un.png" alt="United Nations"></div>
        <h3 class="mentor__t">United Nations</h3>
        <p class="mentor__r">Education volunteer</p>
        <p class="mentor__s">Supporting students in Tier&nbsp;2 and Tier&nbsp;3 cities with career awareness, exposure to technology and consulting work, and industry readiness.</p>
      </article>
      <article class="mentor reveal" data-delay="1">
        <div class="mentor__logo"><img src="assets/partner-moe.png" alt="Ministry of Education, Government of India"></div>
        <h3 class="mentor__t">Ministry of Education</h3>
        <p class="mentor__r">Vidyanjali mentor</p>
        <p class="mentor__s">Registered under the Government of India&rsquo;s school volunteer programme, working with students on career awareness and the educational pathways open to them.</p>
      </article>
      <article class="mentor reveal" data-delay="2">
        <div class="mentor__logo"><img src="assets/partner-tnskill.png" alt="Naan Mudhalvan, TNSkill Corporation"></div>
        <h3 class="mentor__t">Naan Mudhalvan</h3>
        <p class="mentor__r">Industry mentor, TNSkill</p>
        <p class="mentor__s">Volunteering with Tamil&nbsp;Nadu&rsquo;s skills mission, giving college students a clear view of technology and consulting careers before they have to choose one.</p>
      </article>
    </div>

    <p class="mentors__foot reveal">These are the volunteer mentoring roles our own team holds. The organisations above are not affiliated with Project Yaadhum and do not endorse, certify or accredit this work.</p>
  </div>
</section>
</main>"""

B.page("index.html", "home", BODY, body_class="home")
print("home rebuilt")
