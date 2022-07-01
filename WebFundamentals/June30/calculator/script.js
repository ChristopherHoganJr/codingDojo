var displayDiv = document.querySelector("#display");

var userInput = "";
var userEquation = "";

display(0);

function display(x) {
  displayDiv.innerText = x;
  if (x.length > 11) {
    display(x.splice(10) + "...");
  }
}

function press(num) {
  userInput += num;
  userEquation += num;
  display(userInput);
  console.log(`userEquation = ${userEquation}`);
}

function setOP(op) {
  userEquation += " " + op + " ";
  display(userInput);
  userInput = "";
}

function clr() {
  userInput = "";
  userEquation = "";
  display(0);
}

function calculate() {
  display(eval(userEquation));
  userEquation = "(" + userEquation + ")";
}
