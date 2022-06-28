let connectionRequest = document.querySelectorAll(".icon");
let connectionsBadge = document.querySelectorAll(".badge");
let acceptIcon = document.querySelectorAll('img[alt="accept"]');
let profileName = document.querySelectorAll("h1");
let settingsSelector = document.querySelectorAll("a");

connectionsBadge[0].innerHTML = connectionRequest.length / 2;
connectionsBadge[1].innerHTML = 418;
// console.log(
//   (connectionsBadge.innerText = connectionRequest.parentElement.length / 2)
// );

connectionRequest.forEach((e) => {
  e.addEventListener("click", () => {
    e.parentElement.parentElement.remove();
    connectionsBadge[0].innerHTML--;
  });
});

acceptIcon.forEach((icon) => {
  icon.addEventListener("click", () => {
    connectionsBadge[1].innerHTML++;
  });
});

settingsSelector[3].addEventListener("click", () => {
  let newName = prompt("What is your name?: ");
  profileName[1].innerText = newName;
});
