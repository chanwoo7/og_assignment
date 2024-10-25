document.addEventListener('DOMContentLoaded', function () {
    const prices = document.querySelectorAll('.price');

    prices.forEach(function (priceElement) {
        const originalPrice = priceElement.getAttribute('data-price');
        priceElement.textContent = formatNumber(originalPrice);
    });
});