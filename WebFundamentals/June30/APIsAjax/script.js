let currentUsername = "";

function getUsername(element) {
  currentUsername = element.value;
}

function makeCoderCard(data) {
  let res = `<div class="card">
                <h2>${data.login}</h2>
                <h3>${data.location}</h3>
                <img src="${data.avatar}" alt="${data.login} profile picture">
  
            </div>`;
  return res;
}

async function search() {
  console.log("clicked");
  let response = await fetch("https://api.github.com/users/" + currentUsername);
  let coderData = await response.json();

  console.log(coderData);
  document.getElementById("cards").innerHTML = makeCoderCard(coderData);
}
