var secondsHand = document.getElementById("seconds");
var minutesHand = document.getElementById("minutes");

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
  var secondsTime = (time % 60) * 6;
  console.log("seconds: " + secondsTime);
  secondsHand.style.transform = `rotate(${(time % 1000) * 6}deg)`;
}, 1000);

setInterval(function () {
  var time = getSecondsSinceStartOfDay();
  console.log(time);
  var minutesTime = (time % 600) * 6;
  minutesHand.style.transform = `rotate(${(time % 60000) * 6}deg)`;
  console.log("minutes time: " + minutesTime);
}, 60000);
