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

function appendOperator(operator) {
    displayValue += ` ${operator} `;
    updateDisplay();
}

function appendFunction(func) {
    displayValue += `${func}(`;
    updateDisplay();
}

function appendConstant(constant) {
    displayValue += constant;
    updateDisplay();
}

function calculate() {
    try {
        const result = eval(displayValue.replace('÷', '/').replace('×', '*'));
        displayValue = result;
        updateDisplay();
    } catch (error) {
        displayValue = 'Error';
        updateDisplay();
    }
}

function updateDisplay() {
    document.getElementById('display').value = displayValue;
}
