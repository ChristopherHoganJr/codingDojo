let navItems = document.querySelectorAll(".nav-links");
let cookieBar = document.getElementById("cookieBtn");
let tempCalc = document.getElementById("tempSelect");
let highTemps = document.querySelectorAll(".high-temp");
let lowTemps = document.querySelectorAll(".low-temp");

let highValues = [24, 27, 21, 26];
let lowValues = [18, 19, 16, 21];

highTemps.forEach((e, idx) => {
  e.innerText = `${highValues[idx]}°`;
});
lowTemps.forEach((e, idx) => {
  e.innerText = `${lowValues[idx]}°`;
});

navItems.forEach((e) => {
  e.addEventListener("click", () => {
    alert("Loading weather report...");
  });
});

cookieBar.addEventListener("click", () => {
  cookieBar.parentElement.remove();
});

tempCalc.addEventListener("change", () => {
  if (tempCalc.value === "fahrenheit") {
    highTemps.forEach((e, idx) => {
      e.innerText = `${Math.round(highValues[idx] * 1.8 + 32)}°`;
    });
    lowTemps.forEach((e, idx) => {
      e.innerText = `${Math.round(lowValues[idx] * 1.8 + 32)}°`;
    });
  } else {
    highTemps.forEach((e, idx) => {
      e.innerText = `${highValues[idx]}°`;
    });
    lowTemps.forEach((e, idx) => {
      e.innerText = `${lowValues[idx]}°`;
    });
  }
});
