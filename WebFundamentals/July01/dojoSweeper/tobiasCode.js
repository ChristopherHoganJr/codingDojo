var theDojo = [
  [1, 0, 1, 1, 1, 0, 4, 0, 8, 0],
  [3, 1, 0, 7, 0, 0, 6, 0, 8, 8],
  [5, 0, 7, 0, 3, 6, 6, 6, 0, 0],
  [2, 3, 0, 9, 0, 0, 6, 0, 8, 0],
  [6, 0, 3, 3, 0, 2, 0, 3, 0, 4],
  [0, 0, 3, 3, 0, 0, 2, 2, 3, 0],
  [0, 0, 0, 0, 5, 0, 1, 2, 0, 6],
  [2, 2, 2, 2, 0, 7, 1, 1, 1, 0],
  [5, 2, 0, 2, 0, 0, 0, 1, 1, 2],
  [9, 2, 2, 2, 0, 7, 0, 1, 1, 0],
];
var dojoDiv = document.querySelector("#the-dojo");

// Creates the rows of buttons for this game
function render(theDojo) {
  var result = "";
  for (var i = 0; i < theDojo.length; i++) {
    for (var j = 0; j < theDojo[i].length; j++) {
      result += `<button class="tatami" onclick="howMany(${i}, ${j}, this)"></button>`;
    }
  }
  return result;
}

// newGame called at start and when you lose
function newGame() {
  //clear the board
  dojoDiv.innerHTML = "";
  //generate random board
  randomBoard();
  // shows the dojo for debugging purposes
  console.table(theDojo);
  // adds the rows of buttons into <div id="the-dojo"></div>
  dojoDiv.innerHTML = render(theDojo);
}

// TODO - Make this function tell us how many ninjas are hiding
//        under the adjacent (all sides and corners) squares.
//        Use i and j as the indexes to check theDojo.
function howMany(i, j, element) {
  // console.log({i, j});

  if (theDojo[i][j] != 0) {
    alert("game over");
    newGame();
    return;
  }

  var imin = Math.max(0, i - 1);
  var imax = Math.min(theDojo.length - 1, i + 1);
  var jmin = Math.max(0, j - 1);
  var jmax = Math.min(theDojo[i].length - 1, j + 1);

  // console.log({ imin, imax, jmin, jmax })

  var sum = 0;
  for (var i2 = imin; i2 <= imax; i2++)
    for (var j2 = jmin; j2 <= jmax; j2++) sum += theDojo[i2][j2];

  // alert(sum + " ninjas hiding under this and adjacent squares");

  // draw number on this button
  element.innerText = sum;

  //reveal adjacent squares if there are 0 adjacent ninjas
  if (sum == 0) {
    // "click" the adjacent button elements
    for (var i2 = imin; i2 <= imax; i2++)
      for (var j2 = jmin; j2 <= jmax; j2++) {
        //don't re-reveal already revealed squares, including this one (or else infinite loop)
        var e = document.querySelector(
          "#the-dojo > button:nth-child(" +
            (i2 * theDojo[i2].length + j2 + 1) +
            ")"
        );
        if (e.innerText === "") howMany(i2, j2, e);
      }
  }
}

function randomBoard() {
  //clear the board
  for (var i = 0; i < theDojo.length; i++)
    for (var j = 0; j < theDojo[i].length; j++) theDojo[i][j] = 0;

  var count = 0;
  while (count < 10) {
    var i = Math.floor(Math.random() * theDojo.length);
    var j = Math.floor(Math.random() * theDojo[i].length);
    if (theDojo[i][j] == 0) {
      theDojo[i][j] = 1;
      count++;
    }
    //the loop continues without count increasing if already a ninja in square
  }
}

// BONUS CHALLENGES
// 1. draw the number onto the button instead of alerting it
// 2. at the start randomly place 10 ninjas into theDojo with at most 1 on each spot
// 3. if you click on a ninja you must restart the game
//    dojoDiv.innerHTML = `<button onclick="location.reload()">restart</button>`;

// start the game
// message to greet a user of the game
var style = "color:cyan;font-size:1.5rem;font-weight:bold;";
console.log("%c" + "IF YOU ARE A DOJO STUDENT...", style);
console.log("%c" + "GOOD LUCK THIS IS A CHALLENGE!", style);

newGame();
