function pizzaOven(crustType, sauceType, cheeses, toppings) {
    return {
        crustType: crustType,
        sauceType: sauceType,
        cheeses: cheeses,
        toppings: toppings
    };
}

var pizza1 = pizzaOven("deep dish", "traditional", ["mozzarella"], ["pepperoni", "sausage"]);
console.log(pizza1);
var pizza2 = pizzaOven("hand tossed", "marinara", ["mozzarella", "feta"], ["mushrooms", "olives", "onions"]);
console.log(pizza2);
var pizza3 = pizzaOven("thin crust", "pesto", ["cheddar"], ["spinach", "bacon"]);
console.log(pizza3);
var pizza4 = pizzaOven("stuffed crust", "alfredo", ["mozzarella"], ["ham", "pineapple"]);
console.log(pizza4);
function randomPizza() {
    var crustTypes = ["deep dish", "hand tossed", "thin crust", "stuffed crust"];
    var sauceTypes = ["marinara", "white sauce", "pesto", "traditional"];
    var cheeseOptions = ["mozzarella", "cheddar", "parmesan", "feta"];
    var toppingOptions = ["pepperoni", "sausage", "bacon", "mushrooms", "olives", "onions", "spinach", "pineapple"];
    function getRandom(arr) {
        var index = Math.floor(Math.random() * arr.length);
        return arr[index];
    }
    var pizza = {
        crustType: getRandom(crustTypes),
        sauceType: getRandom(sauceTypes),
        cheeses: [getRandom(cheeseOptions)], 
        toppings: [getRandom(toppingOptions), getRandom(toppingOptions)] 
    };
    return pizza;
}
console.log(randomPizza());