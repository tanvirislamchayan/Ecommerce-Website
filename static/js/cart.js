(function() {
    const plusButtons = document.getElementsByClassName('plus');
    const minusButtons = document.getElementsByClassName('minus');

    for (let i = 0; i < plusButtons.length; i++) {
        plusButtons[i].addEventListener('click', function() {
            updateValue(i, 1);
        });
    }

    for (let i = 0; i < minusButtons.length; i++) {
        minusButtons[i].addEventListener('click', function() {
            updateValue(i, -1);
        });
    }

    function updateValue(index, delta) {
        const qtyElement = document.getElementsByClassName('qty')[index];
        const priceElement = document.getElementsByClassName('productPrice')[index];

        let qty = parseInt(qtyElement.value); // Changed innerText to value
        const unitPrice = parseFloat(priceElement.innerText);

        qty = Math.max(1, qty + delta);
        const updatedPrice = qty * unitPrice;
        
        qtyElement.value = qty; // Changed innerText to value
        document.getElementsByClassName('totalPrice')[index].innerText = updatedPrice.toFixed(2);
    }

    window.addEventListener('DOMContentLoaded', function() {
        const priceElements = document.getElementsByClassName('productPrice');
        for (let i = 0; i < priceElements.length; i++) {
            const priceElement = priceElements[i];
            const qtyElement = document.getElementsByClassName('qty')[i];
            const unitPrice = parseFloat(priceElement.innerText);
            priceElement.dataset.unitPrice = unitPrice.toFixed(2);
        }
    });
})();
