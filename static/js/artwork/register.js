document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('#form');
    const messageContainer = document.querySelector('#message');
    const priceInput = document.querySelector('#price');

    // 천 단위로 콤마를 추가하는 함수
    function formatPrice(value) {
        value = value.replace(/\D/g, '');  // 숫자만 남김
        return value.replace(/\B(?=(\d{3})+(?!\d))/g, ',');  // 천 단위마다 콤마 추가
    }

    // 가격 입력할 때마다 콤마 추가
    priceInput.addEventListener('input', function (e) {
        e.target.value = formatPrice(e.target.value);
    });

    form.addEventListener('submit', function (event) {
        event.preventDefault();

        // 콤마를 제거한 후 데이터를 전송
        const formData = {
            title: document.querySelector('#title').value,
            price: priceInput.value.replace(/,/g, ''),  // 콤마 제거
            size: document.querySelector('#size').value,
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
                alert("작품이 성공적으로 등록되었습니다.");
                window.location.href = "/";
            } else {
                messageContainer.innerHTML = data.errors;
                messageContainer.style.color = 'red';
            }
        })
        .catch(error => {
            messageContainer.innerHTML = "<div class='alert alert-danger'>서버와 통신 중 오류가 발생했습니다.</div>";
            console.error('Error:', error);
        });
    });
});
