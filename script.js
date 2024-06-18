function appendNumber(number) {
    const display = document.getElementById('display');
    display.value += number;
}

function appendOperation(operation) {
    const display = document.getElementById('display');
    display.value += operation;
}

function clearDisplay() {
    const display = document.getElementById('display');
    display.value = '';
}

function calculate() {
    const display = document.getElementById('display');
    try {
        display.value = eval(display.value);
    } catch {
        display.value = 'Error';
    }
}
