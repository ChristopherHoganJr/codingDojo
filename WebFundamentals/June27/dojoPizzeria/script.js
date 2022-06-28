function pizzaOven(crustType, sauceType, cheeses, toppings) {
  let Pizza = {};
  Pizza.crustType = crustType;
  Pizza.sauceType = sauceType;
  Pizza.cheeses = cheeses;
  Pizza.toppings = toppings;
  return Pizza;
}

let pizzaA = pizzaOven(
  "deep dish",
  "traditional",
  ["mozzarelaa"],
  ["pepperoni", "sausage"]
);
let pizzaB = pizzaOven(
  "hand tossed",
  "marinara",
  ["mozzarella", "feta"],
  ["mushrooms", "olives", "onions"]
);
let pizzaC = pizzaOven(
  "stuffed crust",
  "pesto",
  ["parmesan", "gouda"],
  ["sausage", "onions", "bacon"]
);
let pizzaD = pizzaOven(
  "thin crust",
  "pesto",
  ["parmesan"],
  ["pepperoni", "mushrooms", "chicken"]
);

function randomPizza() {
  let pizzaItems = {
    crustType: ["deep dish", "hand tossed", "stuffed crust", "thin crust"],
    sauceType: ["traditional", "marinara", "pesto"],
    cheeses: ["mozzarella", "feta", "parmesan", "gouda"],
    toppings: [
      "pepperoni",
      "sausage",
      "chicken",
      "olives",
      "onions",
      "bacons",
      "mushrooms",
    ],
  };
  let crust =
    pizzaItems.crustType[
      Math.floor(Math.random() * Object.values(pizzaItems.crustType).length)
    ];
  let sauce =
    pizzaItems.sauceType[
      Math.floor(Math.random() * Object.values(pizzaItems.sauceType).length)
    ];
  let cheeseitems = Math.floor(Math.random() * 2) + 1;
  let cheesearr = [];
  for (let cheese = 0; cheese < cheeseitems; cheese++) {
    cheesearr.push(
      pizzaItems.cheeses[
        Math.floor(Math.random() * Object.values(pizzaItems.cheeses).length)
      ]
    );
  }
  let toppingCount = Math.floor(
    Math.random() * Object.values(pizzaItems.toppings).length
  );
  let toppingsArr = [];
  for (let topping = 0; topping < toppingCount + 1; topping++) {
    toppingsArr.push(
      pizzaItems.toppings[
        Math.floor(Math.random() * Object.values(pizzaItems.toppings).length)
      ]
    );
  }
  toppingsArr = [...new Set(toppingsArr)];
  return pizzaOven(crust, sauce, cheesearr, toppingsArr);
}

let pizzaZ = randomPizza();
console.log(pizzaZ);
