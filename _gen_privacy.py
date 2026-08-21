# -*- coding: utf-8 -*-
"""
The student-information page, from the supplied policy draft.

Everything here is either already true of how the site works (verified in the
code: no analytics, no cookies, Web3Forms handles the forms) or is a practice
the site already commits to elsewhere. Four things the draft marked [CONFIRM]
are stated as principles rather than invented specifics, and are listed back to
the client: the retention periods, the parent-verification method, the named
safeguarding lead, and the postal address.
"""
import _build as B

BODY = """<main class="subpage">
  <article class="doc">

    <h1>How we handle student information</h1>
    <p class="doc__lede">Written as a promise to a parent, not as terms and conditions.</p>

    <p>This page explains what information we collect from students, families, schools and volunteers,
    why we collect it, who sees it, how long we keep it, and what you can ask us to do with it. It is
    written to be read by a parent or a principal, not by a lawyer.</p>

    <p>If anything here is unclear, or if you want something removed, write to
    <a href="mailto:komala@projectyaadhum.com">komala@projectyaadhum.com</a> and a person will reply.</p>

    <!-- ------------------------- the short version ------------------------- -->
    <div class="doc__summary">
      <h2>The short version</h2>
      <ul>
        <li>We are a research organisation. We go into schools and write down how students and families
        make decisions about what to study after Class&nbsp;10.</li>
        <li>We ask before we involve any child. A parent or guardian is told what we are doing and gives
        permission first.</li>
        <li>We do not score, rank, predict, label or profile any student. We never have, and Indian law
        prohibits it for children in any case.</li>
        <li>A school receives findings about its own students. A family receives its own child&rsquo;s
        output. Volunteers, sponsors, other schools and the public receive none of it.</li>
        <li>Anything we publish is anonymised. No child is identifiable in our research output.</li>
        <li>We do not sell information to anyone, and we do not share it with sponsors or funders.</li>
        <li>You can ask us what we hold about you, ask us to correct it, and ask us to delete it.</li>
      </ul>
    </div>

    <h2>Who we are</h2>
    <p>Project Yaadhum is a field research initiative based in Cuddalore, Tamil&nbsp;Nadu, studying how
    students in Tier&nbsp;2 and Tier&nbsp;3 schools arrive at their stream and pathway decisions after
    Class&nbsp;10. Project Yaadhum began work in 2025. Yaadhum Foundation is currently in the process of
    being registered as a nonprofit education and research organisation.</p>
    <p>Until that registration completes, Project Yaadhum is the organisation that decides why and how
    personal data is processed, and it carries the obligations that go with that. When registration
    completes we will name Yaadhum Foundation here, with its registration number.</p>
    <p>Contact for anything on this page:
    <a href="mailto:komala@projectyaadhum.com">komala@projectyaadhum.com</a>. That address is read by a
    person, not a system, and they answer it themselves.</p>

    <h2>Whose information we handle</h2>
    <ul>
      <li><strong>Students in Classes 9 to 12</strong> at partner schools and community programmes.
      Every one of them is a child under Indian law, which defines a child as anyone under 18.</li>
      <li><strong>Parents and guardians</strong>, who give permission for their child to take part, and
      who attend parent sessions at community programmes.</li>
      <li><strong>Teachers, principals and school staff</strong>, whom we interview about how decisions
      are made in their school.</li>
      <li><strong>Volunteers</strong>, who apply to do fieldwork with us.</li>
      <li><strong>People who write to us</strong> through a form on this website or by email.</li>
    </ul>

    <h2>What we collect, and why</h2>
    <p>We collect only what a specific piece of work actually requires. Every field on every form has to
    have a reason attached to it before it goes on the form. We do not collect student information
    simply because we can.</p>

    <h3>From students taking part in a programme</h3>
    <p>What we collect depends on the exercise, and it is explained to the parent beforehand. It
    ordinarily includes the student&rsquo;s name or an assigned code, class and section, school, and
    their responses to the transition exercise: what they have been exposed to, what they are curious
    about, what they know about the pathways open to them, and how they are thinking about what comes
    next.</p>
    <p>We collect this to understand how the decision is being made and what information has or has not
    reached the student. Where the school has agreed to receive individual findings, we also use it to
    prepare those.</p>

    <h3>From parents and guardians</h3>
    <p>Name, relationship to the student, a contact number or email, and the record of the permission
    given. At a community programme, what a parent asks about during the parent session, recorded as
    notes rather than attributed statements.</p>
    <p>We collect this to confirm that a real, identifiable adult has given permission, to reach you if
    we need to, and to keep a record that permission was given, which the law requires us to be able to
    demonstrate.</p>

    <h3>From teachers, principals and school staff</h3>
    <p>Name, role, school, and what you tell us in an interview.</p>
    <p>We collect this because your account of how decisions are actually made in your school is the
    research. Interviews are recorded only where you have agreed to it, and you can ask us to stop
    recording at any point without giving a reason.</p>

    <h3>From volunteers</h3>
    <p>Name, phone or WhatsApp number, email, college or organisation, district, languages, how you
    would like to contribute, and why the work interests you. Before any student-facing work, identity
    verification documents and a record of training completed.</p>
    <p>We collect this to run the volunteer programme, to verify that people working near children are
    who they say they are, and to issue your Certificate of Contribution from Project&nbsp;Yaadhum,
    recording verified work and hours.</p>

    <h3>From people who contact us</h3>
    <p>Whatever you put in the form or the email: ordinarily name, email, who you are, district or town,
    and your message. We use it to reply to you, and for nothing else. We do not add you to a mailing
    list.</p>

    <h2>How we ask for permission, and how you can withdraw it</h2>
    <p>Before any child takes part, a parent or guardian is told, in a language they read comfortably,
    what the programme is, what will be collected, why, who will see it, and how long we will keep it.
    Permission is given after that explanation, not before it, and not by the school on the
    family&rsquo;s behalf.</p>
    <p>We verify that the person giving permission is an adult. Indian law requires more than a
    signature: we have to take reasonable steps to confirm that the person consenting is genuinely an
    identifiable adult and the child&rsquo;s parent or guardian.</p>
    <p><strong>Permission can be refused with no consequence to the student.</strong> A child whose
    parent does not give permission simply does not take part in that exercise. They are not separated
    out, not marked absent from anything, and nothing about the decision is recorded against them.</p>
    <p><strong>Permission can be withdrawn at any time</strong>, before or after a session, by writing to
    <a href="mailto:komala@projectyaadhum.com">komala@projectyaadhum.com</a> or telling the school
    coordinator. Withdrawing is as easy as giving permission. When permission is withdrawn we delete
    that child&rsquo;s individual responses, and we tell you when it has been done.</p>
    <p>One honest limit: if we have already used a child&rsquo;s responses inside an anonymised
    aggregate, a count or an average or a pattern across a cohort where no individual can be identified
    or extracted, we cannot pull that contribution back out, because by then it is no longer attached to
    your child in any recoverable way. Everything individual goes.</p>

    <h2>Children&rsquo;s information: what the law requires, and what we do anyway</h2>
    <p>Indian law treats everyone under 18 as a child, and applies specific protections. Some of these
    we would follow regardless, because they are the reason the organisation exists in the form it
    does.</p>
    <p><strong>We do not track, monitor or profile children.</strong> This is prohibited under
    Section&nbsp;9(3) of the Digital Personal Data Protection Act, 2023. It is also the thing we most
    want to be clear about, because it is what people assume an organisation like ours must be doing. We
    build no profile of any student. We do not follow a student across sessions to construct a picture
    of them. We do not attach anything to a child that follows them onwards.</p>
    <p><strong>We do not advertise to children, and we do not let anyone else do so.</strong> No sponsor
    branding appears on an individual child&rsquo;s output. No organisation gets access to students
    through us in order to market to them.</p>
    <p><strong>We do not produce scores, percentages, rankings or predictions.</strong> A student&rsquo;s
    responses are never used to rank them against others or to predict what they will become. There is
    no aptitude score, no career-fit percentage, no diagnosis, and no permanent label. This is not a
    limitation we have accepted reluctantly; it is a design decision, and it is why the exercise is not
    an aptitude test.</p>
    <p class="doc__pull">A student should leave with more possibilities to explore, not another label
    attached to them.</p>

    <h2>Who sees what</h2>
    <p>This is the part that matters most, so it is stated plainly.</p>
    <div class="whosees">
      <div class="whosees__row">
        <h3>A school pilot</h3>
        <p><strong>The school</strong> receives the agreed student-level findings for its own students.
        Everyone else receives cohort-level or anonymised findings only, unless the school has
        separately authorised something else.</p>
      </div>
      <div class="whosees__row">
        <h3>A community programme</h3>
        <p><strong>The student and their parent or guardian</strong> receive that child&rsquo;s own
        output, and nobody else does. Colleges, volunteers, sponsors and local partners receive no
        individual student reports at all.</p>
      </div>
      <div class="whosees__row">
        <h3>Everyone else</h3>
        <p>Authorised Project Yaadhum team members may process student information only to run the
        agreed programme, produce the agreed output and keep the programme record. Access is limited to
        the people who genuinely need it.</p>
      </div>
    </div>
    <p><strong>We do not sell personal data to anyone, in any form, for any purpose.</strong> There is no
    circumstance in which that changes. If it ever did, we would have to come back and ask you again,
    because that is not what you agreed to.</p>

    <h2>Research and publication</h2>
    <p>The point of the fieldwork is to write down how these decisions get made and hand that back to the
    people making them. That means publishing.</p>
    <ul>
      <li>Anything used for research or publication is anonymised, unless separate, explicit permission
      has been given for something specific. Anonymised means names removed, and details that could
      identify an individual removed or generalised: a school, a district in a small enough sample, or
      an unusual circumstance described in a way a local reader would recognise.</li>
      <li>We do not name a partner school in a publication without that school&rsquo;s written
      agreement.</li>
      <li>We quote teachers, principals and parents only where they have agreed to be quoted, and we
      show them the quote first.</li>
      <li>We do not publish photographs of children without the specific permission that requires. A
      general consent to take part is not a consent to be photographed, and we do not treat it as
      one.</li>
    </ul>

    <h2>How long we keep things</h2>
    <p>The principle is that we keep something for as long as the purpose we collected it for is still
    live, and then we delete it. Contact and application details are kept while the conversation you
    started is live. Research material is kept only for as long as the study needs it in identifiable
    form; when it no longer does, we delete it or strip out anything that identifies a person.</p>
    <p>You do not have to wait for a retention period to expire. You can ask us to delete something
    earlier, and we will, unless a law requires us to keep it.</p>

    <h2>Safeguarding, and the one limit on confidentiality</h2>
    <p>Working with minors requires clear boundaries, and these are the conditions under which anyone
    from Yaadhum is allowed near a student.</p>
    <ul>
      <li>Everyone in a student-facing role is 18 or older, identity-verified, and has completed
      mandatory training before any fieldwork.</li>
      <li>No one from Yaadhum works one-to-one with a minor without supervision.</li>
      <li>No one from Yaadhum contacts a student privately through personal WhatsApp, Instagram, phone or
      any other personal channel. If it happens, tell us.</li>
      <li>Volunteers may not copy, download or retain student information outside the approved process.
      Nothing goes onto a personal device, a personal account or a personal drive.</li>
      <li>A volunteer who breaches these does not continue with us.</li>
    </ul>
    <p>And the honest limit. Almost everything a student or family tells us is confidential, and this
    page describes how we protect it. There is one exception, and we would rather you heard it here than
    discovered it later.</p>
    <p>Under Section&nbsp;19 of the Protection of Children from Sexual Offences Act, 2012, any person in
    India who knows or suspects that a child has been sexually abused is legally required to report it to
    the police or the Special Juvenile Police Unit. This duty applies to everyone, it cannot be waived by
    anyone, and failing to report is itself an offence.</p>
    <p>So: if something a student tells us gives us reason to believe a child is being harmed, we are
    required by law to report it, and we will. We will not promise confidentiality we are not permitted
    to keep. Where it is safe and appropriate to do so, we would tell the family what we are doing and
    why.</p>

    <h2>Photographs and recordings</h2>
    <p>We do not photograph or record a child without the specific permission that requires, separately
    from the permission to take part. Where photographs are taken at a programme with permission, we use
    them only for the purpose explained at the time. No photograph of a child appears on a
    sponsor&rsquo;s material, and no sponsor branding appears alongside a child&rsquo;s image or an
    individual child&rsquo;s report. You can withdraw permission for a photograph later, and we will
    remove it from anything we control.</p>

    <h2>If something goes wrong</h2>
    <p>If personal data we hold is exposed or accessed in a way it should not have been, we are required
    to tell the Data Protection Board of India within 72 hours, and to tell the people affected. We will
    tell you plainly what happened, what was exposed, and what we are doing about it.</p>

    <h2>Your rights</h2>
    <p>Under the Digital Personal Data Protection Act, 2023 you can:</p>
    <ul>
      <li>Ask what we hold about you: a summary of your personal data and what we are doing with it.</li>
      <li>Ask us to correct it if something is wrong, incomplete or out of date.</li>
      <li>Ask us to delete it, where we do not have a legal reason to keep it.</li>
      <li>Withdraw consent at any time, as easily as you gave it.</li>
      <li>Complain to us, and get a proper answer.</li>
      <li>Nominate someone to exercise these rights on your behalf if you die or become unable to.</li>
    </ul>
    <p>A parent or guardian exercises these rights on behalf of a child.</p>
    <p><strong>How to use them:</strong> write to
    <a href="mailto:komala@projectyaadhum.com">komala@projectyaadhum.com</a> with what you want. You do
    not need to use any particular form of words. We will confirm we have received it and respond within
    30 days. If we need something from you to be sure who you are, we will ask for the least we can
    manage. There is no charge for any of this.</p>

    <h2>If you are unhappy with how we have handled something</h2>
    <p>Write to <a href="mailto:komala@projectyaadhum.com">komala@projectyaadhum.com</a> and say so. A
    person will read it and reply. If it is a complaint rather than a question, say that, and we will
    treat it as one.</p>
    <p>If we do not resolve it to your satisfaction, you can complain to the Data Protection Board of
    India, which is the statutory authority for data protection complaints under the DPDP Act. You do
    not need our permission to go to them, and you do not have to come to us first.</p>

    <h2>This website</h2>
    <p><strong>Forms.</strong> The forms on this site collect what the form shows. Submissions are
    delivered to us by email through Web3Forms, which passes the message on and does not use it for
    anything else. We use what you send to reply to you.</p>
    <p><strong>Cookies and analytics.</strong> This site sets no cookies, runs no analytics, and uses no
    third-party tracking of any kind. Nothing about your visit is recorded by us. The only external
    request the site makes is to Google Fonts, to load the typefaces the pages are set in.</p>
    <p><strong>Links to other sites.</strong> Where we link somewhere else, that site has its own policy
    and we are not responsible for it.</p>

    <h2>Changes to this page</h2>
    <p>If we change how we handle information, we will change this page and update the date at the top.
    If a change is substantive, if it affects what we collect, who sees it, or how long we keep it, we
    will say what changed rather than quietly replacing the text. Where a change affects information you
    have already given us, we will ask you again rather than assume the old permission covers the new
    thing.</p>

    <h2>Contact</h2>
    <p><a href="mailto:komala@projectyaadhum.com">komala@projectyaadhum.com</a><br>
    Project Yaadhum, Cuddalore, Tamil&nbsp;Nadu, India</p>
    <p>We reply to every message ourselves. No mailing list, no autoresponder.</p>

    <p class="doc__back"><a href="index.html">&larr; Back to home</a></p>
  </article>
</main>"""

B.page("privacy.html", "privacy", BODY)
print("privacy page built")
