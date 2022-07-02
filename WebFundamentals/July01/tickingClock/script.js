var secondsHand = document.getElementById("seconds");
var minutesHand = document.getElementById("minutes");
var hoursHand = document.getElementById("hour");

function getSecondsSinceStartOfDay() {
  return (
    new Date().getSeconds() +
    new Date().getMinutes() * 60 +
    new Date().getHours() * 3600
  );
}

setInterval(function () {
  var time = getSecondsSinceStartOfDay();
  // your code here
  secondsHand.style.transform = `rotate(${new Date().getSeconds() * 6}deg)`;
  minutesHand.style.transform = `rotate(${new Date().getMinutes() * 6}deg)`;
  hoursHand.style.transform = `rotate(${new Date().getHours() * 6}deg)`;
}, 1000);

console.log(new Date().getMinutes());
