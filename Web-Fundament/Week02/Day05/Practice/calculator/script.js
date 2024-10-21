let currentInput = "";
let operator = "";
let firstOperand = null;

function press(num) {
    if (currentInput.length < 10) {
        currentInput += num.toString();
        updateDisplay();
    }
}

function setOP(op) {
    if (currentInput === "") return;
    if (firstOperand === null) {
        firstOperand = parseFloat(currentInput);
    } else {
        calculate();
    }
    operator = op;
    currentInput = "";
}

function calculate() {
    if (firstOperand === null || currentInput === "") return;
    let secondOperand = parseFloat(currentInput);
    let result;

    switch (operator) {
        case "+":
            result = firstOperand + secondOperand;
            break;
        case "-":
            result = firstOperand - secondOperand;
            break;
        case "*":
            result = firstOperand * secondOperand;
            break;
        case "/":
            result = firstOperand / secondOperand;
            break;
        default:
            return;
    }

    currentInput = result.toString();
    firstOperand = null;
    operator = "";
    updateDisplay();
}

function clr() {
    currentInput = "";
    firstOperand = null;
    operator = "";
    updateDisplay();
}

function updateDisplay() {
    document.getElementById("display").innerText = currentInput || "0";
}
