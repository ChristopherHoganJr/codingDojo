let likeBtn = document.querySelectorAll(".likeBtn");
let likeText = document.querySelectorAll(".likeCounter");

let likeCounter = [];

likeText.forEach((counter, idx) => {
  likeCounter.push(0);
  likeText[idx].innerHTML = `${likeCounter[idx]} like(s)`;
});

likeBtn.forEach((btn, idx) => {
  btn.addEventListener("click", () => {
    likeCounter[idx]++;
    likeText[idx].innerHTML = `${likeCounter[idx]} like(s)`;
  });
});
