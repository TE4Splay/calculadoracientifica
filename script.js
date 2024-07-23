body {
    background-color: #bfbfbf;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    margin: 0;
    font-family: Arial, sans-serif;
}

.calculator {
    background-color: #505050;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
    padding: 20px;
}

.display {
    width: 100%;
    padding: 10px;
    margin-bottom: 10px;
    font-size: 24px;
    text-align: right;
    background-color: #303030;
    color: white;
    border: none;
    border-radius: 5px;
}

.buttons {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 5px;
}

.btn {
    padding: 15px;
    font-size: 18px;
    background-color: #d3d3d3;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

.btn:hover {
    background-color: #c0c0c0;
}

.btn:active {
    background-color: #a9a9a9;
}

.btn.number {
    background-color: #f0f0f0;
}

.btn.operator {
    background-color: #f0c040;
}

.btn.function {
    background-color: #80c0ff;
}

.wide {
    grid-column: span 2;
}

.tall {
    grid-row: span 2;
}
