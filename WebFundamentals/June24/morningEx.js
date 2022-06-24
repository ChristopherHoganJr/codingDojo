var fruit1 = "apples";
var fruit2 = "oranges";

var temp = "";

temp = fruit1;
fruit1 = fruit2;
fruit2 = temp;

console.log(fruit1, fruit2);

function reverse(arr) {
  //   arr = arr.reverse();
  return arr;
}

console.log(reverse(["a", "b", "c", "d", "e"]));
