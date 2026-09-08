/* Irish Air to Water — shared behaviour */
(function () {
  'use strict';

  /* ---------- Mobile nav ---------- */
  var toggle = document.querySelector('.nav-toggle');
  var panel = document.getElementById('mobile-panel');

  if (toggle && panel) {
    var setMenu = function (open) {
      toggle.setAttribute('aria-expanded', String(open));
      panel.classList.toggle('open', open);
      document.body.classList.toggle('nav-open', open);
    };
    toggle.addEventListener('click', function () {
      setMenu(toggle.getAttribute('aria-expanded') !== 'true');
    });

    panel.addEventListener('click', function (e) {
      if (e.target.closest('a')) setMenu(false);
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
        setMenu(false);
        toggle.focus();
      }
    });

    window.addEventListener('resize', function () {
      if (window.innerWidth > 900) setMenu(false);
    });
  }

  /* ---------- FAQ accordion ---------- */
  document.querySelectorAll('.faq-q').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var open = btn.getAttribute('aria-expanded') === 'true';
      var answer = document.getElementById(btn.getAttribute('aria-controls'));
      btn.setAttribute('aria-expanded', String(!open));
      if (answer) answer.classList.toggle('open', !open);
    });
  });

  /* ---------- Autoplay video honours reduced motion ---------- */
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    document.querySelectorAll('video[autoplay]').forEach(function (v) {
      v.removeAttribute('autoplay');
      v.pause();
    });
  }

  /* ---------- Reveal on scroll ---------- */
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var items = document.querySelectorAll('.reveal');

  function revealAll() {
    items.forEach(function (el) { el.classList.add('in'); });
  }

  if (reduce || !('IntersectionObserver' in window)) {
    revealAll();
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('in');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.08, rootMargin: '0px 0px -40px 0px' });
    items.forEach(function (el) { io.observe(el); });

    /* Safety net: a fast jump-scroll (anchor link, End key, scrollbar drag)
       can skip elements entirely. Sweep anything already above the fold. */
    var sweep = function () {
      items.forEach(function (el) {
        if (el.classList.contains('in')) return;
        var r = el.getBoundingClientRect();
        if (r.top < window.innerHeight && r.bottom > 0) {
          el.classList.add('in');
          io.unobserve(el);
        }
      });
    };
    window.addEventListener('load', sweep);
    window.addEventListener('scroll', function () {
      window.clearTimeout(sweep._t);
      sweep._t = window.setTimeout(sweep, 120);
    }, { passive: true });
  }

  /* ---------- Contact forms ----------
     If the form has an action (set FORM_ACTION in build.py), submit it
     in the background and show the result. Without one, this is the
     pre-launch placeholder that only pretends to send. */
  document.querySelectorAll('form[data-iatw-form]').forEach(function (form) {
    var btn = form.querySelector('button[type="submit"]');
    var original = btn ? btn.textContent : '';

    var lock = function (label) {
      if (!btn) return;
      btn.textContent = label;
      btn.disabled = true;
      form.querySelectorAll('input, select, textarea').forEach(function (f) { f.disabled = true; });
    };

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      /* honeypot: bots fill every field, people never see this one */
      var trap = form.querySelector('input[name="website"]');
      if (trap && trap.value) { lock('Sent. We will be in touch.'); return; }

      var action = form.getAttribute('action');
      if (!action) { lock('Sent. We will be in touch.'); return; }

      if (btn) { btn.textContent = 'Sending…'; btn.disabled = true; }
      fetch(action, {
        method: 'POST',
        body: new FormData(form),
        headers: { 'Accept': 'application/json' }
      }).then(function (r) {
        if (r.ok) { lock('Sent. We will be in touch.'); return; }
        throw new Error('bad status');
      }).catch(function () {
        if (btn) { btn.textContent = original; btn.disabled = false; }
        var note = form.querySelector('.form-error');
        if (!note) {
          note = document.createElement('p');
          note.className = 'form-error';
          note.setAttribute('role', 'alert');
          form.appendChild(note);
        }
        note.textContent = 'That did not send. Please call or WhatsApp 087 341 3114.';
      });
    });
  });
})();
