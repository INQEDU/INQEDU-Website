// Ink & Quill (INQEDU) — site behaviour

(function () {
  // Mobile menu
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.getElementById("site-nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }

  // Annotated passage: link each note to the words it explains
  var reading = document.querySelector(".reading");
  if (reading) {
    var setActive = function (n, on) {
      reading.querySelectorAll('[data-n="' + n + '"]').forEach(function (el) {
        el.classList.toggle("is-active", on);
      });
    };
    reading.querySelectorAll("[data-n]").forEach(function (el) {
      var n = el.getAttribute("data-n");
      el.addEventListener("mouseenter", function () { setActive(n, true); });
      el.addEventListener("mouseleave", function () { setActive(n, false); });
      el.addEventListener("focus", function () { setActive(n, true); });
      el.addEventListener("blur", function () { setActive(n, false); });
    });
  }

})();
