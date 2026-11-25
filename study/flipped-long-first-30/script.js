(function () {
  "use strict";

  var figures = Array.prototype.slice.call(document.querySelectorAll("[data-figure]"));
  var lightbox = document.getElementById("lightbox");
  var lightboxImg = document.getElementById("lightbox-img");
  var lightboxCap = document.getElementById("lightbox-cap");
  var btnClose = document.getElementById("lightbox-close");
  var btnPrev = document.getElementById("lightbox-prev");
  var btnNext = document.getElementById("lightbox-next");
  var toggleAll = document.getElementById("toggle-all");
  var allSource = false;
  var activeIndex = 0;
  var lastFocus = null;

  function setMode(fig, mode) {
    var img = fig.querySelector(".chart-img");
    var annotated = fig.getAttribute("data-annotated");
    var source = fig.getAttribute("data-source");
    var isSource = mode === "source";
    img.src = isSource ? source : annotated;
    img.alt = fig.getAttribute(isSource ? "data-alt-source" : "data-alt-annotated");
    fig.setAttribute("data-mode", mode);
    Array.prototype.forEach.call(fig.querySelectorAll("[data-mode]"), function (btn) {
      var on = btn.getAttribute("data-mode") === mode;
      btn.classList.toggle("is-active", on);
      btn.setAttribute("aria-pressed", on ? "true" : "false");
    });
  }

  Array.prototype.forEach.call(document.querySelectorAll(".mode-toggle button"), function (btn) {
    btn.addEventListener("click", function () {
      setMode(btn.closest("[data-figure]"), btn.getAttribute("data-mode"));
    });
  });

  if (toggleAll) {
    toggleAll.addEventListener("click", function () {
      allSource = !allSource;
      var mode = allSource ? "source" : "annotated";
      figures.forEach(function (fig) {
        setMode(fig, mode);
      });
      toggleAll.textContent = allSource ? "全部改回註解圖" : "全部顯示原畫面";
    });
  }

  function openLightbox(index) {
    var fig = figures[index];
    var img = fig.querySelector(".chart-img");
    activeIndex = index;
    lastFocus = document.activeElement;
    lightboxImg.src = img.src;
    lightboxImg.alt = img.alt;
    lightboxCap.textContent = fig.getAttribute("data-caption") || "";
    lightbox.hidden = false;
    document.body.classList.add("lb-open");
    btnClose.focus();
  }

  function closeLightbox() {
    lightbox.hidden = true;
    document.body.classList.remove("lb-open");
    lightboxImg.removeAttribute("src");
    if (lastFocus && typeof lastFocus.focus === "function") {
      lastFocus.focus();
    }
  }

  function nav(delta) {
    activeIndex = (activeIndex + delta + figures.length) % figures.length;
    var fig = figures[activeIndex];
    var img = fig.querySelector(".chart-img");
    lightboxImg.src = img.src;
    lightboxImg.alt = img.alt;
    lightboxCap.textContent = fig.getAttribute("data-caption") || "";
  }

  figures.forEach(function (fig, i) {
    var img = fig.querySelector(".chart-img");
    var zoom = fig.querySelector(".zoom-btn");
    img.addEventListener("click", function () {
      openLightbox(i);
    });
    img.addEventListener("keydown", function (e) {
      if (e.key === "Enter" || e.key === " ") {
        e.preventDefault();
        openLightbox(i);
      }
    });
    if (zoom) {
      zoom.addEventListener("click", function () {
        openLightbox(i);
      });
    }
  });

  if (lightbox && btnClose && btnPrev && btnNext) {
    btnClose.addEventListener("click", closeLightbox);
    btnPrev.addEventListener("click", function () {
      nav(-1);
    });
    btnNext.addEventListener("click", function () {
      nav(1);
    });
    lightbox.addEventListener("click", function (e) {
      if (e.target === lightbox || e.target.classList.contains("lightbox-stage")) {
        closeLightbox();
      }
    });
    document.addEventListener("keydown", function (e) {
      if (lightbox.hidden) {
        return;
      }
      if (e.key === "Escape") {
        closeLightbox();
      } else if (e.key === "ArrowLeft") {
        nav(-1);
      } else if (e.key === "ArrowRight") {
        nav(1);
      }
    });
  }
})();
