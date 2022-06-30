var nums = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
];
var moreNums = [
  [1, 2, 3, 4, 5, 6],
  [2.7, 4, 1, 5, 5],
];

function printAll2d(arr2d) {
  for (var i = 0; i < arr2d.length; i++) {
    console.log("outer loop new iteration");
    for (var j = 0; j < arr2d[i].length; j++) {
      console.log("inner loop new iteration");
      console.log(arr2d[i][j]);
    }
  }
}

printAll2d(numms);

function flatten(arr2d) {
  var flat = [];
  // your code here
  for (let i = 0; i < arr2d.length; i++) {
    for (let j = 0; j < arr2d[i].length; j++) {
      flat.push(arr2d[i][j]);
    }
  }
  return flat;
}

console.log(flatten(nums));
console.log(flatten(moreNums));

// Challenge to reverse an array with arrays
function flip(arr2d) {
  let newArr = [];
  for (let i = arr2d.length - 1; i >= 0; i--) {
    for (let j = 0; j < arr2d[i].length / 2; j++) {
      let tempVar;
      tempVar = arr2d[i][j];
      arr2d[i][j] = arr2d[i][arr2d[i].length - 1 - j];
      arr2d[i][arr2d[i].length - 1 - j] = tempVar;
    }
    newArr.push(arr2d[i]);
  }
  console.log(newArr);
}

console.log(flip(nums));
