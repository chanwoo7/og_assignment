document.addEventListener('DOMContentLoaded', function() {
    const selectAllCheckbox = document.getElementById('select-all');
    const form = document.getElementById('application-form');

    // 체크박스 일괄 선택
    if (selectAllCheckbox) {
        selectAllCheckbox.addEventListener('change', function() {
            const checkboxes = document.querySelectorAll('input[name="applications"]');
            for (const checkbox of checkboxes) {
                // disabled가 아닌 경우에만 선택/해제
                if (!checkbox.disabled) {
                    checkbox.checked = this.checked;
                }
            }
        });
    }

    // 폼 제출 전 체크박스 선택 여부 확인 및 AJAX 요청
    if (form) {
        form.addEventListener('submit', function(event) {
            event.preventDefault();  // 폼 기본 제출 막기

            const checkboxes = document.querySelectorAll('input[name="applications"]:checked');
            if (checkboxes.length === 0) {
                alert('최소 하나 이상의 신청을 선택하세요.');
                return;
            }

            // 선택된 신청 ID를 배열로 수집
            const applicationIds = Array.from(checkboxes).map(checkbox => checkbox.value);

            // 폼 데이터 구성
            const formData = new FormData(form);

            const action = event.submitter.value;
            formData.append('action', action);

            formData.delete('applications');  // 기존 데이터 제거

            // 선택된 신청 ID들을 개별적으로 추가
            applicationIds.forEach(id => {
                formData.append('applications', id);
            });

            // AJAX 요청으로 서버에 제출
            fetch('/management/process_applications/', {  // form.action 대신 명시적인 URL 사용
                method: 'POST',
                body: formData,
                headers: {
                    'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
                }
            })
            .then(response => {
                if (response.ok) {
                    // 처리 성공 시
                    alert('선택한 신청들이 정상적으로 처리되었습니다.');
                    window.location.reload();  // 페이지 새로고침
                } else {
                    // 실패 시
                    alert('처리 중 오류가 발생했습니다.');
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('서버와 통신 중 오류가 발생했습니다.');
            });
        });
    }
});
