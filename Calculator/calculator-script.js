function displayValue(val) {
    document.getElementById("display").value = document.getElementById("display").value + val;
}

function clearDisplay(val) {
    document.getElementById("display").value = "";
}

function Calculate() {
    var userInput = document.getElementById("display").value;
    var result = eval(userInput);
    document.getElementById("display").value = result;
}