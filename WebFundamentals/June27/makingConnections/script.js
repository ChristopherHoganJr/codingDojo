let connectionRequest = document.querySelectorAll(".icon");
let connectionsBadge = document.querySelector(".badge");

connectionsBadge.innerHTML = connectionRequest.length;
console.log(
  (connectionsBadge.innerText = connectionRequest.parentElement.length / 2)
);

connectionRequest.forEach((e, idx) => {
  e.addEventListener("click", () => {
    e.parentElement.parentElement.remove();
    console.log(connectionRequest);
  });
});

console.log(connectionsBadge.innerHTML);
console.log(connectionRequest);
