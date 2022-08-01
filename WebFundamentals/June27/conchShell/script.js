let userQuestion = document.getElementById("user-question");
let btn = document.getElementById("questionBtn");
let fortune = document.getElementById("fortune");

btn.addEventListener("click", () => {
  var answer = [
    "yes",
    "no",
    "ask again later",
    "maybe",
    "seems logical",
    "i highly doubt that",
    "i have a bad feeling about htis",
    "hello there",
    "theres a chance",
    "you're screwed",
  ];
  let randIDX = Math.floor(Math.random() * answer.length);
  fortune.innerText = `${userQuestion.value}... ${answer[randIDX]}`;
  userQuestion.value = "";
  userQuestion.focus();
});

function pullString() {
  let conchShell;
}

// functionName, time in milisecons to wait
// setTimeout(functionToRun, 5000)
