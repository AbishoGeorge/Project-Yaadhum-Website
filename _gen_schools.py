# -*- coding: utf-8 -*-
import _build as B

# the "Working with schools" block moved off the home page, kept whole
MOVED = open("_parts/schools.html", encoding="utf-8").read()
# strip its outer <section> wrapper so it can sit inside this page's flow
MOVED = MOVED.replace('<!-- ===================== FOR SCHOOLS =========================== -->\n', '')
MOVED = MOVED.replace('<section class="section schools" id="schools">',
                      '<section class="section schools" id="noticing">')
# the block was lifted from the end of the home page, so it carries the
# closing </main> with it. Drop it: this page closes its own main.
MOVED = MOVED.replace('</main>', '')

BODY = """<main class="subpage">

  <!-- ============================ HERO ============================ -->
  <section class="contact-hero">
    <div class="wrap">
      <div class="head-split head-split--top">
        <div>
          <h1 class="reveal">Bring the research into <em>one of your classrooms</em>.</h1>
          <p class="hero-sub reveal">One class. One period. No fee, now or later.</p>
          <p class="schools__lede reveal" style="color:var(--ink-2);max-width:56ch">Project Yaadhum is a field research initiative. We are building the first working version of a student transition programme, and we are looking for a small number of schools willing to try it while it is still being shaped.</p>
        </div>
        <figure class="heroviz reveal" data-delay="1"
                aria-label="A pilot is one section of students and about forty-five minutes of one period.">
          <svg viewBox="0 0 300 130" role="img">
            <!-- 45 minutes out of one period -->
            <circle class="hv-ring" cx="60" cy="60" r="54"/>
            <circle class="hv-arc" cx="60" cy="60" r="54"/>
            <text x="60" y="56" text-anchor="middle" class="hv-num">45</text>
            <text x="60" y="76" text-anchor="middle" class="hv-unit">MINUTES</text>
            <!-- one section of a class -->
            <circle class="hv-seat" cx="176" cy="30" r="4" style="transition-delay:0ms"/>
              <circle class="hv-seat" cx="193" cy="30" r="4" style="transition-delay:22ms"/>
              <circle class="hv-seat" cx="210" cy="30" r="4" style="transition-delay:44ms"/>
              <circle class="hv-seat" cx="227" cy="30" r="4" style="transition-delay:66ms"/>
              <circle class="hv-seat" cx="244" cy="30" r="4" style="transition-delay:88ms"/>
              <circle class="hv-seat" cx="261" cy="30" r="4" style="transition-delay:110ms"/>
              <circle class="hv-seat" cx="176" cy="47" r="4" style="transition-delay:132ms"/>
              <circle class="hv-seat" cx="193" cy="47" r="4" style="transition-delay:154ms"/>
              <circle class="hv-seat" cx="210" cy="47" r="4" style="transition-delay:176ms"/>
              <circle class="hv-seat" cx="227" cy="47" r="4" style="transition-delay:198ms"/>
              <circle class="hv-seat" cx="244" cy="47" r="4" style="transition-delay:220ms"/>
              <circle class="hv-seat" cx="261" cy="47" r="4" style="transition-delay:242ms"/>
              <circle class="hv-seat hv-seat--on" cx="176" cy="64" r="4" style="transition-delay:264ms"/>
              <circle class="hv-seat hv-seat--on" cx="193" cy="64" r="4" style="transition-delay:286ms"/>
              <circle class="hv-seat hv-seat--on" cx="210" cy="64" r="4" style="transition-delay:308ms"/>
              <circle class="hv-seat hv-seat--on" cx="227" cy="64" r="4" style="transition-delay:330ms"/>
              <circle class="hv-seat hv-seat--on" cx="244" cy="64" r="4" style="transition-delay:352ms"/>
              <circle class="hv-seat hv-seat--on" cx="261" cy="64" r="4" style="transition-delay:374ms"/>
              <circle class="hv-seat" cx="176" cy="81" r="4" style="transition-delay:396ms"/>
              <circle class="hv-seat" cx="193" cy="81" r="4" style="transition-delay:418ms"/>
              <circle class="hv-seat" cx="210" cy="81" r="4" style="transition-delay:440ms"/>
              <circle class="hv-seat" cx="227" cy="81" r="4" style="transition-delay:462ms"/>
              <circle class="hv-seat" cx="244" cy="81" r="4" style="transition-delay:484ms"/>
              <circle class="hv-seat" cx="261" cy="81" r="4" style="transition-delay:506ms"/>
              <circle class="hv-seat" cx="176" cy="98" r="4" style="transition-delay:528ms"/>
              <circle class="hv-seat" cx="193" cy="98" r="4" style="transition-delay:550ms"/>
              <circle class="hv-seat" cx="210" cy="98" r="4" style="transition-delay:572ms"/>
              <circle class="hv-seat" cx="227" cy="98" r="4" style="transition-delay:594ms"/>
              <circle class="hv-seat" cx="244" cy="98" r="4" style="transition-delay:616ms"/>
              <circle class="hv-seat" cx="261" cy="98" r="4" style="transition-delay:638ms"/>
          </svg>
          <figcaption>One section, about <b>45 minutes</b> of one period. That is the whole ask.</figcaption>
        </figure>
      </div>
      <p class="reveal" style="margin-top:1.8em"><span class="status">We do not arrive with a fixed programme, or a fixed answer. We begin with the problem your school is seeing</span></p>
    </div>
  </section>

  <!-- ================= WHICH CLASS, four questions ================= -->
  <section class="section section--paper">
    <div class="wrap">
      <div class="head-split head-split--top">
        <div class="reveal">
          <h2 class="duo__statement">Four classes. Four different transition questions.</h2>
        </div>
        <p class="standfirst reveal" data-delay="1">Across Classes 9 to 12, where do your students or parents struggle most with what comes next? We do not ask a school to fit our programme. We shape the first pilot around the problem it is already living with.</p>
      </div>

      <div class="classes">
        <article class="klass reveal">
          <div class="klass__ico" aria-hidden="true">
            <svg viewBox="0 0 40 40"><circle cx="20" cy="20" r="13"/><path class="hi" d="M20 7v6M20 27v6M7 20h6M27 20h6"/></svg>
          </div>
          <p class="klass__n">Class 9</p>
          <h3 class="klass__t">Explore before choices narrow</h3>
          <p class="klass__s">What students have been exposed to, what they are curious about, and what deserves exploring before the major decisions begin.</p>
        </article>
        <article class="klass reveal" data-delay="1">
          <div class="klass__ico" aria-hidden="true">
            <svg viewBox="0 0 40 40"><path d="M20 32V15"/><path class="hi" d="M20 15 8 8"/><path d="M20 15l12-7"/><circle cx="20" cy="15" r="2.5" class="fill"/></svg>
          </div>
          <p class="klass__n">Class 10</p>
          <h3 class="klass__t">Choose with better information</h3>
          <p class="klass__s">How stream and pathway decisions are actually being made, what the family knows, what is influencing it, and what is missing.</p>
        </article>
        <article class="klass reveal" data-delay="2">
          <div class="klass__ico" aria-hidden="true">
            <svg viewBox="0 0 40 40"><path d="M7 27c6 0 6-12 13-12s7 12 13 12"/><path class="hi" d="M7 33h26"/></svg>
          </div>
          <p class="klass__n">Class 11</p>
          <h3 class="klass__t">Adjust and stay on track</h3>
          <p class="klass__s">Who is struggling with the transition, what sits behind a drop in performance or confidence, and where support may matter.</p>
        </article>
        <article class="klass reveal" data-delay="3">
          <div class="klass__ico" aria-hidden="true">
            <svg viewBox="0 0 40 40"><path d="M8 30V13l12-6 12 6v17"/><path class="hi" d="M15 30v-8h10v8"/></svg>
          </div>
          <p class="klass__n">Class 12</p>
          <h3 class="klass__t">Navigate exams, courses and colleges</h3>
          <p class="klass__s">Whether students know the pathways open to them, the examinations and eligibility involved, and what they need to do next.</p>
        </article>
      </div>
    </div>
  </section>

  <!-- =================== WHAT WE KEEP NOTICING ==================== -->
""" + MOVED + """
  <!-- ===================== HOW A PILOT WORKS ====================== -->
  <section class="section section--paper">
    <div class="wrap">
      <div class="head-split head-split--top">
        <div class="reveal">
          <h2 class="duo__statement">Small enough to learn properly.</h2>
        </div>
        <p class="standfirst reveal" data-delay="1">Six steps, start to finish. The first pilots are design partnerships rather than finished products, which is exactly why they are free.</p>
      </div>
      <aside class="aside-card reveal" data-delay="1">
        <h3>What a school gives us</h3>
        <ul>
          <li>One section, around 30 to 50 students</li>
          <li>About 45 minutes of one period</li>
          <li>One coordinator we can work with</li>
          <li>The permissions the pilot requires</li>
          <li>An honest conversation afterwards</li>
        </ul>
      </aside>

      <ol class="flow">
        <li class="flow__step reveal"><span class="flow__n">01</span>
          <h3 class="flow__t">Choose one problem</h3>
          <p class="flow__s">A short conversation with the school to identify one transition question worth investigating.</p></li>
        <li class="flow__step reveal"><span class="flow__n">02</span>
          <h3 class="flow__t">Choose one cohort</h3>
          <p class="flow__s">Usually one section, around 30 to 50 students.</p></li>
        <li class="flow__step reveal"><span class="flow__n">03</span>
          <h3 class="flow__t">Run one focused session</h3>
          <p class="flow__s">Around 45 minutes of student time, adapted to the question we chose together. It is not an aptitude test.</p></li>
        <li class="flow__step reveal"><span class="flow__n">04</span>
          <h3 class="flow__t">Make sense of what we find</h3>
          <p class="flow__s">We look for patterns, exceptions, and information that deserves someone&rsquo;s attention.</p></li>
        <li class="flow__step reveal"><span class="flow__n">05</span>
          <h3 class="flow__t">Share it back</h3>
          <p class="flow__s">The school receives a cohort summary and the agreed findings, with a clear read of what appears to matter.</p></li>
        <li class="flow__step reveal"><span class="flow__n">06</span>
          <h3 class="flow__t">Recheck where useful</h3>
          <p class="flow__s">A few weeks later, where the design calls for it, we revisit what was flagged and tell you what changed.</p></li>
      </ol>
    </div>
  </section>

  <!-- ================== STUDENT INFORMATION ======================= -->
  <section class="section">
    <div class="wrap">
      <div class="head-split head-split--top">
        <div class="reveal">
          <h2 class="duo__statement">Written as a promise to a parent, not as terms and conditions.</h2>
        </div>
        <p class="standfirst reveal" data-delay="1">For a school pilot, the agreed individual findings go to the school. We do not distribute individual reports to volunteers, sponsors, other schools or the public.</p>
      </div>

      <div class="promises">
        <div class="promise reveal"><h3>Collect only what we need</h3>
          <p>Every field a programme asks for has to have a reason. We do not collect student information simply because we can.</p></div>
        <div class="promise reveal" data-delay="1"><h3>Parents know beforehand</h3>
          <p>The programme, what is collected and how it will be used are explained before a minor takes part, and consent is obtained where required.</p></div>
        <div class="promise reveal" data-delay="2"><h3>No ranking, no labels</h3>
          <p>A student&rsquo;s responses are never used to rank them against others or to predict what they will become.</p></div>
        <div class="promise reveal" data-delay="3"><h3>Research is anonymised</h3>
          <p>Anything used for research or publication is anonymised unless separate, explicit permission has been given.</p></div>
      </div>
      <p class="reveal" style="margin-top:clamp(26px,4vh,40px)">
        <a class="quietlink" href="privacy.html">Read how we handle student information</a>
      </p>
    </div>
  </section>

  <!-- ======================== WHY FREE ============================ -->
  <section class="section section--paper">
    <div class="wrap duo">
      <div class="duo__statement reveal">Why are the first pilots free? <span class="accent">Because we are still learning too.</span></div>
      <div class="duo__body reveal" data-delay="1">
        <h2 class="block-title">No fee, no obligation</h2>
        <p>Project Yaadhum is studying how students in Tier&nbsp;2 and Tier&nbsp;3 communities actually navigate school transitions. We would rather learn from real schools than build around assumptions.</p>
        <p>The first pilots are therefore free, with no obligation to purchase anything afterwards. If this ever becomes a paid school programme, we will say so plainly rather than quietly.</p>
      </div>
    </div>
  </section>

  <!-- ========================= CLOSING ============================ -->
  <section class="section cohort" id="talk">
    <div class="wrap">
      <div class="cohort__grid">
        <div>
          <h2 class="duo__statement reveal">Tell us what your school is seeing.</h2>
          <p class="work__note reveal" data-delay="1" style="margin-top:1.4em;font-size:1rem">You do not need to know whether Yaadhum is the answer. Tell us about the problem. We will call you back, and we are not going to add you to a mailing list.</p>
        </div>

        <!-- see js/main.js for wiring this to a real endpoint -->
        <form class="form form--light reveal" data-delay="1" data-yaadhum action="https://api.web3forms.com/submit" method="POST">
          <!-- Web3Forms: delivered to the address registered against this key -->
          <input type="hidden" name="access_key" value="05681784-0a7f-4680-b1bc-f97bb74409a3">
          <input type="hidden" name="subject" value="Yaadhum website: school enquiry">
          <input type="hidden" name="from_name" value="Project Yaadhum website">
          <!-- honeypot: real people never fill this in -->
          <input type="checkbox" name="botcheck" class="hp" tabindex="-1" autocomplete="off">
          <div class="field-row"><label for="s-school">School name</label>
            <input id="s-school" name="school" type="text" required></div>
          <div class="field-row"><label for="s-name">Your name</label>
            <input id="s-name" name="name" type="text" autocomplete="name" required></div>
          <div class="field-row"><label for="s-role">Your role</label>
            <input id="s-role" name="role" type="text"></div>
          <div class="field-row"><label for="s-phone">Phone</label>
            <input id="s-phone" name="phone" type="tel" autocomplete="tel"></div>
          <div class="field-row"><label for="s-email">Email</label>
            <input id="s-email" name="email" type="email" autocomplete="email" required></div>
          <div class="field-row"><label for="s-place">District or town</label>
            <input id="s-place" name="place" type="text"></div>
          <div class="field-row"><label for="s-class">Which class are you thinking of</label>
            <select id="s-class" name="klass">
              <option value="">Select one</option>
              <option>Class 9</option><option>Class 10</option>
              <option>Class 11</option><option>Class 12</option>
              <option>Not sure yet</option>
            </select></div>
          <div class="field-row"><label for="s-problem">One problem you are seeing among students or parents</label>
            <textarea id="s-problem" name="problem" rows="3"></textarea></div>
          <button class="btn" type="submit">Start a conversation</button>
          <p class="form__done">Thank you. We&rsquo;ve got it, and we&rsquo;ll call you back from komala@projectyaadhum.com.</p>
          <p class="form__fail">That did not go through. Please try again, or write to <a href="mailto:komala@projectyaadhum.com">komala@projectyaadhum.com</a> and we will pick it up from there.</p>
        </form>
      </div>
    </div>
  </section>
</main>"""

B.page("schools.html", "schools", BODY)
print("schools page built")
