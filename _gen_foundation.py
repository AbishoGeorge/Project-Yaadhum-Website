# -*- coding: utf-8 -*-
import _build as B

BODY = """<main class="subpage">

  <!-- ============================ HERO ============================ -->
  <section class="contact-hero">
    <div class="wrap">
      <div class="head-split head-split--top">
        <div>
          <h1 class="reveal">For the students a school will <em>never reach</em>.</h1>
          <p class="hero-sub reveal">Some students meet Yaadhum through their school. Others never will. The Foundation exists for them.</p>
          <p class="schools__lede reveal" style="color:var(--ink-2);max-width:58ch">The Foundation works with colleges, volunteers and local organisations to bring free student transition programmes closer to Tier&nbsp;2 and Tier&nbsp;3 communities, without waiting for every school to adopt a programme first.</p>
        </div>
        <figure class="heroviz reveal" data-delay="1"
                aria-label="A school reaches the students inside it. The Foundation reaches outward, to the ones it never will.">
          <svg viewBox="0 0 300 190" role="img">
            <!-- the ripples going outward -->
            <circle class="hv-ripple" cx="96" cy="95" r="80"/>
            <circle class="hv-ripple" cx="96" cy="95" r="80"/>
            <circle class="hv-ripple" cx="96" cy="95" r="80"/>
            <!-- the school itself -->
            <path class="hv-draw" d="M70 108V78l26-15 26 15v30"/>
            <path class="hv-draw hv-accent" d="M86 108V92h20v16"/>
            <path class="hv-draw" d="M60 108h72"/>
            <!-- the students it never reaches -->
            <circle class="hv-fill-accent" cx="212" cy="52" r="5"/>
            <circle class="hv-fill-accent" cx="252" cy="96" r="5"/>
            <circle class="hv-fill-accent" cx="206" cy="140" r="5"/>
            <path class="hv-draw hv-soft" d="M150 84c26-16 44-24 58-30"/>
            <path class="hv-draw hv-soft" d="M152 100c34 0 62-2 94-4"/>
            <path class="hv-draw hv-soft" d="M150 114c24 12 40 20 52 25"/>
          </svg>
          <figcaption>A school reaches the students inside it. <b>The Foundation goes to the rest.</b></figcaption>
        </figure>
      </div>
      <p class="reveal" style="margin-top:1.8em"><span class="status">Yaadhum Foundation is currently being registered as a nonprofit education and research organisation</span></p>
    </div>
  </section>

  <!-- ===================== WHY IT EXISTS ========================== -->
  <section class="section section--paper">
    <div class="wrap">
      <div class="head-split head-split--top">
        <div class="reveal">
          <h2 class="duo__statement">Information arrives unevenly.</h2>
        </div>
        <p class="standfirst reveal" data-delay="1">One student hears about an examination in Class&nbsp;9. Another discovers it after Class&nbsp;12. One family knows ten people who have gone to university. Another is making the decision for the first time. <b>Ability may be distributed widely. Access to useful information is not.</b></p>
      </div>

      <div class="split-bar reveal" aria-label="Two families making the same decision with very different information">
        <div class="sbar">
          <p class="sbar__lab">A family who has done this before</p>
          <div class="sbar__track"><span class="sbar__fill sbar__fill--full"></span></div>
          <p class="sbar__note">Hears about the examination in Class&nbsp;9. Knows ten people to ask.</p>
        </div>
        <div class="sbar">
          <p class="sbar__lab">A family doing this for the first time</p>
          <div class="sbar__track"><span class="sbar__fill sbar__fill--thin"></span></div>
          <p class="sbar__note">Finds out after Class&nbsp;12. The same child, the same ability.</p>
        </div>
      </div>
      <p class="tline__cap reveal">The Foundation exists to close that distance where a school cannot, through colleges, community organisations and local programmes.</p>
    </div>
  </section>

  <!-- =================== TRANSITION CAMPS ========================= -->
  <section class="section">
    <div class="wrap">
      <div class="head-split head-split--top">
        <div class="reveal">
          <h2 class="duo__statement">One town. Students and parents in the same conversation.</h2>
        </div>
        <p class="standfirst reveal" data-delay="1">Small community programmes for students in Classes 9 to 12 and their families. Not a psychometric destiny test, not a coaching sales event, and not a promise that a child has found the right career in a day. The purpose is the quality and timing of the next decision.</p>
      </div>

      <div class="promises">
        <div class="promise reveal"><h3>The students</h3>
          <p>A transition exercise suited to their stage, and a clear output they can take home and talk about.</p></div>
        <div class="promise reveal" data-delay="1"><h3>The parents</h3>
          <p>A separate local-language session on pathways, timing, examinations, costs and eligibility, and the questions worth asking before a decision.</p></div>
        <div class="promise reveal" data-delay="2"><h3>The volunteers</h3>
          <p>Trained college students help facilitate under supervision. They do not counsel, diagnose, or make pathway decisions for children.</p></div>
        <div class="promise reveal" data-delay="3"><h3>Afterwards</h3>
          <p>Each family keeps only its own child&rsquo;s output. Yaadhum keeps anonymised programme-level learning.</p></div>
      </div>

      <div class="ages reveal">
        <h2 class="block-title">The question changes with age</h2>
        <ul class="ages__list">
          <li><span>Class 9</span>What possibilities have I not yet explored?</li>
          <li><span>Class 10</span>How should I think about my next academic choice?</li>
          <li><span>Class 11</span>Am I adjusting well, and what should I do if I am not?</li>
          <li><span>Class 12</span>What exams, courses, colleges and pathways should I know about now?</li>
        </ul>
      </div>
    </div>
  </section>

  <!-- ====================== FOR COLLEGES ========================== -->
  <section class="section section--paper">
    <div class="wrap">
      <div class="head-split head-split--top">
        <div class="reveal">
          <h2 class="duo__statement">The people who just crossed the bridge can help those approaching it.</h2>
        </div>
        <p class="standfirst reveal" data-delay="1">College students remember what they knew in Class&nbsp;10, what they discovered too late, and what actually helped. We want to turn that recent experience into useful service for younger students.</p>
      </div>

      <div class="obs">
        <div class="obs__item reveal">
          <h3 class="obs__t">Nominate volunteers</h3>
          <p class="obs__s">Usually 5 to 10 students for one programme day, with mandatory training beforehand.</p></div>
        <div class="obs__item reveal" data-delay="1">
          <h3 class="obs__t">Nominate a faculty coordinator</h3>
          <p class="obs__s">A member of staff who can help coordinate the student group and stay our point of contact.</p></div>
        <div class="obs__item reveal" data-delay="2">
          <h3 class="obs__t">Host a camp, or open a door</h3>
          <p class="obs__s">A classroom or seminar hall for a local programme, or an introduction to schools and community groups nearby.</p></div>
      </div>

      <p class="tline__cap reveal">B.Ed and teacher-training students may find the work especially relevant, and the programme can offer real field exposure. Whether it counts toward any formal academic or community-engagement requirement is the college&rsquo;s decision, not ours.</p>
    </div>
  </section>

  <!-- ======================== SAFEGUARDS ========================== -->
  <section class="section">
    <div class="wrap">
      <div class="head-split head-split--top">
        <div class="reveal">
          <h2 class="duo__statement">Working with minors requires clear boundaries.</h2>
        </div>
        <p class="standfirst reveal" data-delay="1">These are not aspirations. They are the conditions under which a volunteer is allowed anywhere near a student, and they apply to everyone including us.</p>
      </div>

      <div class="pair" style="margin-top:clamp(30px,4.5vh,50px)">
        <div class="ask reveal">
          <h3>Before anyone meets a student</h3>
          <ul>
            <li>Parent or guardian communication and consent before a minor participates</li>
            <li>Student-facing volunteers must be 18 or older</li>
            <li>Identity verification and mandatory orientation before fieldwork</li>
            <li>No volunteer works one to one with a minor without supervision</li>
          </ul>
        </div>
        <div class="notlist reveal" data-delay="1">
          <h3>And never</h3>
          <ul>
            <li>No private contact with students through personal WhatsApp, Instagram or other channels</li>
            <li>No downloading, retaining or privately sharing student information</li>
            <li>No photographs of children published without the required permission</li>
            <li>No sponsor branding on an individual child&rsquo;s report</li>
          </ul>
        </div>
      </div>

      <p class="tline__cap reveal">In a Foundation programme, each student and their parent or guardian receives only that child&rsquo;s own output. Colleges, volunteers, sponsors and partner organisations receive none of it.</p>
    </div>
  </section>

  <!-- ========================= PARTNER ============================ -->
  <section class="section cohort" id="partner">
    <div class="wrap">
      <div class="cohort__grid">
        <div>
          <h2 class="duo__statement reveal">If this belongs in work you already do, we would rather begin with a conversation than a cheque.</h2>
          <ul class="work reveal" data-delay="1">
            <li>Host a camp</li>
            <li>Provide volunteers</li>
            <li>Introduce schools or community groups</li>
            <li>Help with community mobilisation</li>
            <li>Support a programme</li>
          </ul>
          <p class="work__note reveal">Camps are free to participating families, and are supported through host institutions, local partners and organisations that want better education access where they already work.</p>
        </div>

        <!-- see js/main.js for wiring this to a real endpoint -->
        <form class="form form--light reveal" data-delay="1" data-yaadhum action="https://api.web3forms.com/submit" method="POST">
          <!-- Web3Forms: delivered to the address registered against this key -->
          <input type="hidden" name="access_key" value="05681784-0a7f-4680-b1bc-f97bb74409a3">
          <input type="hidden" name="subject" value="Yaadhum website: partner enquiry">
          <input type="hidden" name="from_name" value="Project Yaadhum website">
          <!-- honeypot: real people never fill this in -->
          <input type="checkbox" name="botcheck" class="hp" tabindex="-1" autocomplete="off">
          <div class="field-row"><label for="f-name">Name</label>
            <input id="f-name" name="name" type="text" autocomplete="name" required></div>
          <div class="field-row"><label for="f-org">Organisation</label>
            <input id="f-org" name="org" type="text"></div>
          <div class="field-row"><label for="f-type">Organisation type</label>
            <select id="f-type" name="type">
              <option value="">Select one</option>
              <option>College</option><option>School</option>
              <option>Community organisation</option><option>Company or CSR</option>
              <option>Individual</option><option>Something else</option>
            </select></div>
          <div class="field-row"><label for="f-role">Your role</label>
            <input id="f-role" name="role" type="text"></div>
          <div class="field-row"><label for="f-place">District or town</label>
            <input id="f-place" name="place" type="text"></div>
          <div class="field-row"><label for="f-email">Email</label>
            <input id="f-email" name="email" type="email" autocomplete="email" required></div>
          <div class="field-row"><label for="f-how">How would you like to work with us</label>
            <textarea id="f-how" name="how" rows="3"></textarea></div>
          <button class="btn" type="submit">Start a conversation</button>
          <p class="form__done">Thank you. We&rsquo;ll be in touch from komala@projectyaadhum.com.</p>
          <p class="form__fail">That did not go through. Please try again, or write to <a href="mailto:komala@projectyaadhum.com">komala@projectyaadhum.com</a> and we will pick it up from there.</p>
        </form>
      </div>
    </div>
  </section>
</main>"""

B.page("foundation.html", "foundation", BODY)
print("foundation page built")
