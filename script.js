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
    displayValue += ` ${operator} `;
    updateDisplay();
}

function calculate() {
    try {
        const result = eval(displayValue.replace('÷', '/').replace('×', '*'));
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