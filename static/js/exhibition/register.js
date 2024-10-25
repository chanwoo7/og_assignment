document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('#form');
    const messageContainer = document.querySelector('#message');
    const prices = document.querySelectorAll('.price');

    prices.forEach(function (priceElement) {
        const originalPrice = priceElement.getAttribute('data-price');  // 원본 가격
        priceElement.textContent = formatNumber(originalPrice);  // 포맷팅된 가격으로 업데이트
    });

    flatpickr('#start_date', {
        dateFormat: 'Y-m-d',
        minDate: new Date().toISOString().split('T')[0],  // 오늘 날짜
        onChange: function(selectedDates, dateStr, instance) {
            const endDatePicker = document.querySelector('#end_date')._flatpickr;
            endDatePicker.set('minDate', dateStr);  // 시작일 이후로만 종료일 선택 가능
        }
    });

    flatpickr('#end_date', {
        dateFormat: 'Y-m-d',
        onChange: function(selectedDates, dateStr, instance) {
            const startDatePicker = document.querySelector('#start_date')._flatpickr;
            startDatePicker.set('maxDate', dateStr);  // 종료일 이전으로만 시작일 선택 가능
        }
    });

    form.addEventListener('submit', function (event) {
        event.preventDefault();

        // 선택된 작품 목록을 배열로 수집
        const selectedArtworks = Array.from(document.querySelectorAll('input[name="artworks"]:checked')).map(el => el.value);

        // 작품을 하나도 선택하지 않은 경우 메시지 출력 및 제출 중단
        if (selectedArtworks.length === 0) {
            messageContainer.innerHTML = "<div class='alert alert-danger'>하나 이상의 작품을 선택해야 합니다.</div>";
            return;
        }

        const formData = {
            title: document.querySelector('#title').value,
            start_date: document.querySelector('#start_date').value,
            end_date: document.querySelector('#end_date').value,
            artworks: selectedArtworks
        };

        handleFormSubmit(event, form, formData, messageContainer, "/artist/dashboard");
    });
});
