let displayValue = '';

function appendNumber(number) {
    displayValue += number;
    updateDisplay();
}

function appendDecimal() {
    if (!displayValue.includes('.')) {
        displayValue += '.';
        updateDisplay();
    }
}

function clearDisplay() {
    displayValue = '';
    updateDisplay();
}

function deleteLast() {
    displayValue = displayValue.slice(0, -1);
    updateDisplay();
}

function operate(operator) {
    switch(operator) {
        case 'π':
            displayValue += Math.PI;
            break;
        case 'e':
            displayValue += Math.E;
            break;
        default:
            displayValue += ` ${operator} `;
    }
    updateDisplay();
}

function calculate() {
    try {
        const replacedDisplayValue = displayValue.replace('÷', '/').replace('×', '*')
            .replace('sin', 'Math.sin')
            .replace('cos', 'Math.cos')
            .replace('tan', 'Math.tan')
            .replace('sqrt', 'Math.sqrt')
            .replace('pow', 'Math.pow')
            .replace('log', 'Math.log10')
            .replace('exp', 'Math.exp')
            .replace('ln', 'Math.log');
        const result = eval(replacedDisplayValue);
        displayValue = result;
        updateDisplay();
    } catch {
        displayValue = 'Error';
        updateDisplay();
    }
}

function updateDisplay() {
    document.getElementById('display').value = displayValue;
}
