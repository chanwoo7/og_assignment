document.addEventListener('DOMContentLoaded', function() {
    const selectAllCheckbox = document.getElementById('select-all');
    const form = document.getElementById('application-form');
    const searchFieldDropdown = document.getElementById('search_field');
    const searchInputWrapper = document.getElementById('search-input-wrapper');
    const resetButton = document.getElementById('reset-button');

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
    form.addEventListener('submit', function(event) {
        event.preventDefault();

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

    // 검색 필드 전환 로직
    // 초기화 시 성별 선택 드롭다운 숨기기
    toggleSearchInput(searchFieldDropdown.value);

    // 검색 필드 선택 변경 시 이벤트 핸들러
    searchFieldDropdown.addEventListener('change', function() {
        toggleSearchInput(this.value);
    });

    // 검색 필드에 따라 검색어 입력 필드, 성별 드롭다운, 생년월일 입력 표시
    function toggleSearchInput(selectedField) {
        if (selectedField === 'gender') {
            searchInputWrapper.innerHTML = `
                <select name="q" class="form-control">
                    <option value="M" {% if search_query == "M" %}selected{% endif %}>남성</option>
                    <option value="F" {% if search_query == "F" %}selected{% endif %}>여성</option>
                </select>
            `;
        }
        else if (selectedField === 'birth_date') {
            searchInputWrapper.innerHTML = `
                <input type="text" class="form-control" id="birth_date" name="q" placeholder="생년월일을 선택하세요">
            `;
            // flatpickr 적용
            flatpickr("#birth_date", {
                dateFormat: "Y년 m월 d일"
            });
        }
        else {
            searchInputWrapper.innerHTML = `
                <input type="text" name="q" class="form-control" placeholder="검색어 입력" value="">
            `;
        }
    }

    // 검색 조건 초기화 버튼 동작
    resetButton.addEventListener('click', function() {
        window.location.href = window.location.pathname;  // 쿼리 파라미터 제거하고 페이지 새로고침
    });
});
