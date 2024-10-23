document.addEventListener('DOMContentLoaded', function() {
    const selectAllCheckbox = document.getElementById('select-all');
    const form = document.getElementById('application-form');  // form 요소를 올바르게 가져오기

    if (selectAllCheckbox) {  // 전체 선택
        selectAllCheckbox.addEventListener('change', function() {
            const checkboxes = document.querySelectorAll('input[name="applications"]');
            for (const checkbox of checkboxes) {
                checkbox.checked = this.checked;
            }
        });
    }

    // 폼 제출 전 체크박스 선택 여부 확인
    if (form) {  // form 요소가 존재하는지 확인
        form.addEventListener('submit', function(event) {
            const checkboxes = document.querySelectorAll('input[name="applications"]:checked');

            if (checkboxes.length === 0) {
                event.preventDefault();  // 폼 제출을 막음
                alert('최소 하나 이상의 신청을 선택하세요.');
            }
        });
    }

});