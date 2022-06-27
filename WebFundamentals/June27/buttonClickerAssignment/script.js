let loginBtn = document.getElementById("loginBtn");
let addDefBtn = document.getElementById("add");
let likeBtn = document.querySelectorAll(".likeBtn");

// login button on click
loginBtn.addEventListener("click", () => {
  if (loginBtn.innerText == "Login") {
    loginBtn.innerText = "Logout";
  } else {
    loginBtn.innerText = "Login";
  }
});

addDefBtn.addEventListener("click", () => {
  addDefBtn.remove();
});

likeBtn.forEach((e) => {
  e.addEventListener("click", () => {
    alert("Ninja was liked");
  });
});
