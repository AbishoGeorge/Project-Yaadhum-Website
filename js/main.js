/* =========================================================================
   PROJECT YAADHUM - interactions
   Deliberate, few, never two things at once. Respects reduced motion.
   ========================================================================= */
(function () {
  "use strict";

  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var motion = !reduce;

  if (motion) document.body.classList.add("js-motion");

  /* ----------------------------------------------------------------------
     1. THE OPENING - logo travels into the nav.
        The tagline & everything below stay in normal document flow and
        scroll up with the page; ONLY the logo is transformed on scroll.
     ---------------------------------------------------------------------- */
  var heroLogo = document.querySelector(".hero__logo--fixed");
  var navEl = document.querySelector(".nav");
  var navSlot = document.querySelector(".nav__logo");
  var hero = document.querySelector(".hero");
  var holder = document.querySelector(".hero__holder");

  // The three partner marks sit in the page under the slogan and simply
  // scroll with it. They are deliberately NOT animated or pinned.

  if (motion && heroLogo && navEl && navSlot && hero && holder) {
    var start = {}, end = {}, travel = 1;

    function measure() {
      var vh = window.innerHeight;
      var lw = heroLogo.offsetWidth, lh = heroLogo.offsetHeight;

      // resting position = wherever the flow reserves the logo (so the logo sits
      // exactly in its slot and the tagline sits a clear gap below it). Use the
      // holder's document position so this is correct at any scroll, no jitter.
      var y0 = window.pageYOffset || 0;
      var h = holder.getBoundingClientRect();
      start.cx = h.left + h.width / 2;
      start.cy = h.top + y0 + h.height / 2;   // viewport Y of holder centre when at top
      start.s = 1;

      // landed position: exactly over the (invisible) nav logo slot (fixed, so
      // its rect is constant regardless of scroll).
      var r = navSlot.getBoundingClientRect();
      end.cx = r.left + r.width / 2;
      end.cy = r.top + r.height / 2;
      end.s = r.height / lh;

      heroLogo._lw = lw; heroLogo._lh = lh;
      // a slightly longer travel reads smoother; ease-out makes the logo LEAD,
      // darting clear of the tagline instead of colliding with it.
      travel = Math.max(1, vh * 0.82);
      frame();
    }

    // ease-out: fast at the start (logo clears the tagline), gentle landing
    function easeOut(t) { return 1 - Math.pow(1 - t, 3); }

    function frame() {
      // Drive everything from where the flow holders ACTUALLY are right now,
      // rather than from a scroll offset. This makes the whole opening a pure
      // function of layout: it tracks correctly whatever is doing the
      // scrolling (window, a wrapper element, an embedded frame), and it
      // reverses exactly, because scrolling back puts the holders back.
      var hLive = holder.getBoundingClientRect();
      var travelled = start.cy - (hLive.top + hLive.height / 2);
      var p = Math.min(1, Math.max(0, travelled / travel));
      var e = easeOut(p);

      var cx = start.cx + (end.cx - start.cx) * e;
      var cy = start.cy + (end.cy - start.cy) * e;
      var s = start.s + (end.s - start.s) * e;

      var tx = cx - heroLogo._lw / 2;
      var ty = cy - heroLogo._lh / 2;
      heroLogo.style.transform = "translate(" + tx + "px," + ty + "px) scale(" + s + ")";

      // nav materialises as the logo nears its landing (and in time to mask
      // the tagline sliding up underneath it)
      var navOp = Math.min(1, Math.max(0, (p - 0.4) / 0.32));
      document.body.style.setProperty("--nav-op", navOp.toFixed(3));
      // Do NOT kill pointer events on the whole bar: the mobile menu button
      // lives here and must stay tappable over the hero. Only the parts that
      // are actually invisible are made inert, and only on desktop.
      navEl.classList.toggle("nav--ghost", navOp <= 0.5);

    }

    var ticking = false;
    function onScroll() {
      if (ticking) return;
      ticking = true;                      // claim the frame BEFORE requesting it
      window.requestAnimationFrame(function () { ticking = false; frame(); });
    }
    window.addEventListener("scroll", onScroll, { passive: true });
    // capture phase on the document catches scrolling done by a wrapper
    // element or an embedded host, not just the window itself
    document.addEventListener("scroll", onScroll, { passive: true, capture: true });
    window.addEventListener("resize", measure);
    // fonts can change slot size; re-measure once loaded
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(measure);
    window.addEventListener("load", measure);
    measure();
  }

  /* ----------------------------------------------------------------------
     2. REVEAL on scroll - text rising gently
     ---------------------------------------------------------------------- */
  if (motion && "IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); }
      });
    }, { threshold: 0.16, rootMargin: "0px 0px -8% 0px" });
    document.querySelectorAll(".reveal, .descent, .roll").forEach(function (el) { io.observe(el); });
  } else {
    document.querySelectorAll(".descent, .roll").forEach(function (el) { el.classList.add("in"); });
  }

  /* ----------------------------------------------------------------------
     3. THE PUBLIC PICTURE - 100 students resolve into place
        66 science (navy) · 2 arts (marigold) · 32 elsewhere (grey)
        Marks the two arts students deliberately, so the eye finds them.
     ---------------------------------------------------------------------- */
  var roll = document.querySelector(".roll");
  if (roll) {
    // a small walking-figure glyph, echoing the logo
    var FIG = '<svg viewBox="0 0 20 27" aria-hidden="true"><path d="M10 0a3 3 0 1 1 0 6 3 3 0 0 1 0-6Zm-3.4 7.2h6.8c1 0 1.7.8 1.7 1.8l1.3 6.4c.2.9-.4 1.7-1.3 1.7-.7 0-1.2-.4-1.4-1l-1-4.7v3.3l1.3 9.9c.1 1-.6 1.7-1.5 1.7-.8 0-1.4-.6-1.5-1.4l-1-7.7h-.6l-1 7.7c-.1.8-.7 1.4-1.5 1.4-.9 0-1.6-.7-1.5-1.7l1.3-9.9v-3.3l-1 4.7c-.2.6-.7 1-1.4 1-.9 0-1.5-.8-1.3-1.7l1.3-6.4c.2-1 .9-1.8 1.9-1.8Z"/></svg>';

    // classes: 66 sci, 2 art, 32 else - placed so the 2 arts are easy to spot
    var artIndex = { 27: 1, 74: 1 };            // two marked seats
    var elseCount = 32, sci = 0;
    // build an order: distribute 'else' pseudo-evenly, arts fixed
    var seats = [];
    for (var i = 0; i < 100; i++) {
      var cls = "is-sci";
      if (artIndex[i]) cls = "is-art";
      seats.push(cls);
    }
    // scatter 32 "else" seats deterministically among the non-art seats
    var placed = 0, step = 3;
    for (var j = 2; placed < elseCount && j < 100; j += step) {
      if (!artIndex[j]) { seats[j] = "is-else"; placed++; }
      if (j + step >= 100 && step > 1) { step--; j = 1; }
    }
    var frag = document.createDocumentFragment();
    seats.forEach(function (cls, idx) {
      var d = document.createElement("div");
      d.className = "roll__seat " + cls;
      d.style.transitionDelay = (idx * 7) + "ms";
      d.innerHTML = FIG;
      frag.appendChild(d);
    });
    roll.appendChild(frag);
  }

  /* ----------------------------------------------------------------------
     4. FIELDWORK COUNTERS - count up when they enter view
        Values come straight from the data-count attributes in the HTML.
     ---------------------------------------------------------------------- */
  function countUp(el) {
    var target = parseInt(el.getAttribute("data-count"), 10) || 0;
    if (!motion || target === 0) { el.textContent = pad(target); return; }
    var dur = 1400, t0 = null;
    function tick(ts) {
      if (!t0) t0 = ts;
      var p = Math.min(1, (ts - t0) / dur);
      var eased = 1 - Math.pow(1 - p, 3);
      el.textContent = pad(Math.round(target * eased));
      if (p < 1) requestAnimationFrame(tick);
    }
    requestAnimationFrame(tick);
  }
  function pad(n) { return n < 10 ? "0" + n : "" + n; }

  var counters = document.querySelectorAll(".counter__n");
  if (counters.length) {
    if ("IntersectionObserver" in window) {
      var cio = new IntersectionObserver(function (entries) {
        entries.forEach(function (en) {
          if (en.isIntersecting) { countUp(en.target); cio.unobserve(en.target); }
        });
      }, { threshold: 0.6 });
      counters.forEach(function (c) { cio.observe(c); });
    } else {
      counters.forEach(countUp);
    }
  }

  /* ----------------------------------------------------------------------
     5. FAQ - quiet accordion with smooth height
     ---------------------------------------------------------------------- */
  document.querySelectorAll(".faq__item").forEach(function (item) {
    var q = item.querySelector(".faq__q");
    var a = item.querySelector(".faq__a");
    q.addEventListener("click", function (e) {
      e.preventDefault();               // we manage open/close ourselves (smooth height)
      var open = item.hasAttribute("open");
      if (open) {
        a.style.maxHeight = a.scrollHeight + "px";
        requestAnimationFrame(function () { a.style.maxHeight = "0px"; });
        item.removeAttribute("open");
        q.setAttribute("aria-expanded", "false");
      } else {
        item.setAttribute("open", "");
        q.setAttribute("aria-expanded", "true");
        a.style.maxHeight = a.scrollHeight + "px";
        a.addEventListener("transitionend", function te() {
          if (item.hasAttribute("open")) a.style.maxHeight = "none";
          a.removeEventListener("transitionend", te);
        });
      }
    });
  });

  /* ----------------------------------------------------------------------
     6. FORMS - submitted to Web3Forms in the background, so the reader stays
        on the page and gets the inline confirmation instead of being thrown
        to a third-party success screen. The access key lives in the markup;
        it is a public identifier and only routes mail to the registered
        address. Falls back to a normal form POST if fetch is unavailable.
     ---------------------------------------------------------------------- */
  document.querySelectorAll("form[data-yaadhum]").forEach(function (form) {
    if (!window.fetch) return;                 // let the browser POST it the old way

    var btn = form.querySelector("button[type=submit]");
    var label = btn ? btn.textContent : "";

    function state(cls, msg) {
      form.classList.remove("is-sending", "is-done", "is-failed");
      if (cls) form.classList.add(cls);
      var out = form.querySelector(".form__note");
      if (out && msg) out.textContent = msg;
    }

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (form.classList.contains("is-sending")) return;

      // a bot filled the hidden field: pretend all is well and send nothing
      var hp = form.querySelector('input[name="botcheck"]');
      if (hp && hp.checked) { state("is-done"); return; }

      state("is-sending");
      if (btn) { btn.disabled = true; btn.textContent = "Sending"; }

      fetch(form.action, {
        method: "POST",
        headers: { Accept: "application/json" },
        body: new FormData(form)
      })
        .then(function (r) { return r.json().then(function (d) { return { ok: r.ok, d: d }; }); })
        .then(function (res) {
          if (res.ok) {
            state("is-done");
            form.reset();
            form.scrollIntoView({ behavior: reduce ? "auto" : "smooth", block: "center" });
          } else {
            throw new Error((res.d && res.d.message) || "That did not go through");
          }
        })
        .catch(function () {
          state("is-failed");
          if (btn) { btn.disabled = false; btn.textContent = label; }
        });
    });
  });

  /* ----------------------------------------------------------------------
     6b. PARTNER MARKS - until the logo files exist in assets/, hide the
         broken images (and any strip left empty) so nothing looks unfinished.
         Drop the files in and they simply appear; no code change needed.
     ---------------------------------------------------------------------- */
  (function () {
    var marks = document.querySelectorAll(".partners__logo, .hero__partners img, .cred__logo img");
    Array.prototype.forEach.call(marks, function (img) {
      function hide() {
        img.style.display = "none";
        var box = img.closest(".cred__logo");
        if (box && !box.querySelector(".ph")) {
          var ph = document.createElement("span");
          ph.className = "ph";
          ph.textContent = img.getAttribute("alt") || "Logo";
          box.appendChild(ph);
        }
      }
      if (img.complete && img.naturalWidth === 0) hide();
      img.addEventListener("error", hide);
    });
    // if a whole strip ended up empty, collapse it
    [".partners", ".hero__partners"].forEach(function (sel) {
      document.querySelectorAll(sel).forEach(function (strip) {
        window.addEventListener("load", function () {
          var any = Array.prototype.some.call(strip.querySelectorAll("img"), function (i) {
            return i.naturalWidth > 0;
          });
          if (!any) strip.style.display = "none";
        });
      });
    });
  })();

  /* ----------------------------------------------------------------------
     7. THE MOBILE MENU - the six links do not fit across a phone, so below
        900px they live in a panel. Closes on a link, on Escape, on an outside
        tap, and if the window grows back to desktop width.
     ---------------------------------------------------------------------- */
  var navToggle = document.querySelector(".nav__toggle");
  var navPanel = document.querySelector(".nav__links");
  if (navToggle && navPanel) {
    function setMenu(open) {
      navPanel.classList.toggle("is-open", open);
      navToggle.setAttribute("aria-expanded", open ? "true" : "false");
      navToggle.setAttribute("aria-label", open ? "Close menu" : "Open menu");
    }
    navToggle.addEventListener("click", function (e) {
      e.stopPropagation();
      setMenu(navToggle.getAttribute("aria-expanded") !== "true");
    });
    navPanel.addEventListener("click", function (e) {
      if (e.target.tagName === "A") setMenu(false);
    });
    document.addEventListener("click", function (e) {
      if (navPanel.classList.contains("is-open") &&
          !navPanel.contains(e.target) && !navToggle.contains(e.target)) setMenu(false);
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") setMenu(false);
    });
    window.addEventListener("resize", function () {
      if (window.innerWidth > 900) setMenu(false);
    });
  }

  /* ----------------------------------------------------------------------
     8. Smooth in-page anchor for the "Volunteer" nav link
     ---------------------------------------------------------------------- */
  document.querySelectorAll('a[href^="#"]').forEach(function (a) {
    a.addEventListener("click", function (e) {
      var id = a.getAttribute("href");
      if (id.length < 2) return;
      var t = document.querySelector(id);
      if (t) { e.preventDefault(); t.scrollIntoView({ behavior: reduce ? "auto" : "smooth" }); }
    });
  });
})();
