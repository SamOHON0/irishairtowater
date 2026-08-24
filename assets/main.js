/* Irish Air to Water — shared behaviour */
(function () {
  'use strict';

  /* ---------- Mobile nav ---------- */
  var toggle = document.querySelector('.nav-toggle');
  var panel = document.getElementById('mobile-panel');

  if (toggle && panel) {
    toggle.addEventListener('click', function () {
      var open = toggle.getAttribute('aria-expanded') === 'true';
      toggle.setAttribute('aria-expanded', String(!open));
      panel.classList.toggle('open', !open);
    });

    panel.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') {
        toggle.setAttribute('aria-expanded', 'false');
        panel.classList.remove('open');
      }
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
        toggle.setAttribute('aria-expanded', 'false');
        panel.classList.remove('open');
        toggle.focus();
      }
    });

    window.addEventListener('resize', function () {
      if (window.innerWidth > 900) {
        toggle.setAttribute('aria-expanded', 'false');
        panel.classList.remove('open');
      }
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
     Placeholder handler. Wire to Formspree / Vercel function / email
     endpoint before go-live. */
  document.querySelectorAll('form[data-iatw-form]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var btn = form.querySelector('button[type="submit"]');
      if (!btn) return;
      btn.textContent = 'Sent. We will be in touch.';
      btn.disabled = true;
      form.querySelectorAll('input, select, textarea').forEach(function (f) {
        f.disabled = true;
      });
    });
  });
})();
