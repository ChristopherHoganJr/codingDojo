console.log("page loaded...");

let video = document.getElementById("video");

video.addEventListener("mouseover", () => {
  video.play();
});
video.addEventListener("mouseout", () => {
  video.pause();
});
