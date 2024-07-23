function appendCharacter(char) {
    const display = document.getElementById('display');
    const currentValue = display.value;
    if (char === 'TE4splay!') {
        display.value = "Error 404, UPM not found";
        return;
    }
    display.value += char;
}

function clearDisplay() {
    document.getElementById('display').value = '';
}

function deleteLastCharacter() {
    const display = document.getElementById('display');
    display.value = display.value.slice(0, -1);
}

function moveCursor(direction) {
    const display = document.getElementById('display');
    const pos = display.selectionStart;
    display.selectionStart = display.selectionEnd = pos + direction;
}

function calculateResult() {
    const display = document.getElementById('display');
    try {
        let equation = display.value;
        equation = equation.replace('e**', 'Math.exp(');
        equation = equation.replace('sqrt(', 'Math.sqrt(');
        equation = equation.replace('log(', 'Math.log(');
        equation = equation.replace('%', '/100');
        const result = eval(equation);
        display.value = result;
    } catch (error) {
        display.value = 'Error';
    }
}