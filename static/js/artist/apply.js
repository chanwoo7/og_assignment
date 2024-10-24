// 전화번호에 하이픈 추가
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

        handleFormSubmit(event, form, formData, messageContainer);
    });
});
