// Code to copy to clipboard

function clip() {

    let key = document.getElementById("key");

    navigator.clipboard.writeText(key.textContent);

    alert("Key copied to Clipboard");

}

