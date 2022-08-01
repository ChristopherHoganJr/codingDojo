let btn = document.getElementById("customBtn");
// let header = document.getElementById("header");
let headerQ = document.querySelector("#header");

var count = 1;

function buttonClick(element) {
  console.log("yay! you clicked the button" + count);
  count++;
  element.innerText = `clicked ${count} times`;
}

btn.addEventListener("dblclick", () => {
  console.log("this is an event listener");
});

function printThis(element) {
  console.log(element);
}

function clickToChangeTitle() {
  headerQ.innerText = `You clicked ${count} times`;
  count++;
}
