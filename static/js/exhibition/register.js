document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('#form');
    const messageContainer = document.querySelector('#message');

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
            return;  // 폼 제출 중단
        }

        const formData = {
            title: document.querySelector('#title').value,
            start_date: document.querySelector('#start_date').value,
            end_date: document.querySelector('#end_date').value,
            artworks: selectedArtworks
        };

        fetch(form.action, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
            },
            body: JSON.stringify(formData),
        })
        .then(response => response.json())
        .then(data => {
            messageContainer.innerHTML = '';

            if (data.success) {
                alert("전시가 성공적으로 등록되었습니다.");
                window.location.href = "/";
            } else {
                let errorMessage = '';
                for (let [field, errors] of Object.entries(data.errors)) {
                    errorMessage += `${field}: ${errors.join(', ')}<br>`;
                }
                messageContainer.innerHTML = "<div class='alert alert-danger'>" + errorMessage + "</div>";
                messageContainer.style.color = 'red';
            }
        })
        .catch(error => {
            messageContainer.innerHTML = "<div class='alert alert-danger'>서버와 통신 중 오류가 발생했습니다.</div>";
            console.error('Error:', error);
        });
    });
});
