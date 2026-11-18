// Ink & Quill (INQEDU) — site behaviour

// Where the enquiry form sends its data. Leave empty until a form service is connected.
var FORM_ENDPOINT = "";

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

  // Enquiry form
  var form = document.getElementById("enquiry-form");
  if (form) {
    try {
      var wanted = new URLSearchParams(window.location.search).get("subject");
      var select = document.getElementById("course");
      if (wanted && select && select.querySelector('option[value="' + wanted.replace(/[^a-z-]/g, "") + '"]')) {
        select.value = wanted;
      }
    } catch (e) {}
    var status = document.getElementById("form-status");
    var say = function (text) { status.textContent = text; status.hidden = false; status.focus(); };
    form.addEventListener("submit", function (event) {
      event.preventDefault();
      if (!form.reportValidity()) { return; }
      if (!FORM_ENDPOINT) {
        say("The enquiry form is not connected yet, so your message has not been sent. Please use the contact details on this page for now.");
        return;
      }
      var button = form.querySelector("button[type=submit]");
      button.disabled = true;
      fetch(FORM_ENDPOINT, { method: "POST", headers: { Accept: "application/json" }, body: new FormData(form) })
        .then(function (response) {
          if (!response.ok) { throw new Error("Request failed"); }
          form.reset();
          say("Thank you. Your enquiry has been sent and we will reply soon.");
        })
        .catch(function () {
          say("Your message could not be sent. Please try again, or use the contact details on this page.");
        })
        .then(function () { button.disabled = false; });
    });
  }
})();
