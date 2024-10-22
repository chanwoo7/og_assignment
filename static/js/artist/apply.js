function addHyphenToPhoneNumber(phoneNumberInput) {
    let phoneNumber = phoneNumberInput.value.replace(/[^0-9]/g, "");

    // 숫자가 11자 이상 입력되지 않도록 자름
    if (phoneNumber.length > 11) {
        phoneNumber = phoneNumber.substring(0, 12);
    }

    // 010-XXXX-XXXX 형식으로 변환
    if (phoneNumber.length >= 9) {
        phoneNumber = phoneNumber.replace(/^(\d{2,3})(\d{3,4})(\d{4})$/, `$1-$2-$3`);
    }

    phoneNumberInput.value = phoneNumber;
}

document.addEventListener('DOMContentLoaded', function () {
    // Flatpickr로 생년월일 입력 필드에 날짜 선택기 적용
    flatpickr("#birth_date", {
        dateFormat: "Y-m-d",
        maxDate: "2010-12-31",
        locale: "ko"
    });

    const form = document.querySelector('#form');
    const messageContainer = document.querySelector('#message');

    form.addEventListener('submit', function (event) {
        event.preventDefault();  // 폼 기본 제출 동작을 막음

        // 각 폼 필드에서 값 가져오기
        const formData = {
            name: document.querySelector('#name').value,
            birth_date: document.querySelector('#birth_date').value,
            gender: document.querySelector('#gender').value,
            email: document.querySelector('#email').value,
            contact_number: document.querySelector('#contact_number').value,
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
            // 메시지 컨테이너 초기화
            messageContainer.innerHTML = '';

            if (data.success) {
                alert("신청이 성공적으로 완료되었습니다.");
                window.location.href = "/";  // 메인 페이지로 리다이렉트
            } else {
                let errorMessage = '';

                // 각 필드의 에러 메시지를 출력
                try {
                    for (let [field, errors] of Object.entries(data.errors)) {
                        if (field !== 'non_field_errors') {
                            errorMessage += `${field}: ${errors.join(', ')}<br>`;
                        }
                    }
                } catch (error) {
                    const errorsAsString = JSON.stringify(data.errors);
                    // 'string=' 위치 찾기
                    let startIndex = errorsAsString.indexOf("string='");
                    startIndex += 8;

                    // 그 뒤의 ' 위치 찾기
                    let endIndex = errorsAsString.indexOf("'", startIndex);

                    errorMessage = errorsAsString.substring(startIndex, endIndex);
                }

                messageContainer.innerHTML = errorMessage;
                messageContainer.style.color = 'red';
            }
        })
        .catch(error => {
            // 네트워크 또는 서버 오류 처리
            messageContainer.innerHTML = "<div class='alert alert-danger'>서버와 통신 중 오류가 발생했습니다.</div>";
            console.error('Error:', error);
        });
    });
});
