document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('#form');
    const messageContainer = document.querySelector('#message');
    const priceInput = document.querySelector('#price');

    // 가격 입력할 때마다 콤마 추가
    priceInput.addEventListener('input', function (e) {
        e.target.value = formatNumber(e.target.value);
    });

    form.addEventListener('submit', function (event) {
        event.preventDefault();

        // 콤마를 제거한 후 데이터를 전송
        const formData = {
            title: document.querySelector('#title').value,
            price: priceInput.value.replace(/,/g, ''),  // 콤마 제거
            size: document.querySelector('#size').value,
        };

        handleFormSubmit(event, form, formData, messageContainer, "/artist/dashboard");
    });
});
