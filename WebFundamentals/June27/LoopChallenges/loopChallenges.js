// 1. Print odds 1-20
let questionOneAnswer = 0;
for (let i = 1; i < 21; i++) {
  if (i % 2 != 0) {
    questionOneAnswer += i;
  }
}
console.log("Question 1: " + questionOneAnswer);

// 2. Decreasing Multiples of 3
let questionTwoAnswer = 0;
for (let j = 100; j >= 0; j--) {
  if (j % 3 == 0 && j > 0) {
    console.log("Question 2: " + j);
  }
}

// 3. Print the sequence
let counter = 1;
for (let k = 4; k > -4; k -= 1.5) {
  console.log(`Question 3: Step ${counter}: ${k}`);
  counter++;
}

// 4. Sigma
let sum = 0;
for (let l = 1; l <= 100; l++) {
  sum += l;
}
console.log("Question 4: " + sum);

// 5. Fractorial
let product = 1;
for (let m = 1; m <= 12; m++) {
  product *= m;
}
console.log("Question 5: " + product);
