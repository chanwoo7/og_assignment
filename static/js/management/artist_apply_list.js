// 검색 필드에 따라 검색어 입력 필드, 성별 드롭다운, 생년월일 입력 표시
function toggleSearchInput(selectedField) {
    const searchInputWrapper = document.getElementById('search-input-wrapper');

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

document.addEventListener('DOMContentLoaded', function() {
    const selectAllCheckbox = document.querySelector('#select-all');
    const form = document.querySelector('#application-form');
    const searchFieldDropdown = document.querySelector('#search_field');
    const resetButton = document.querySelector('#reset-button');
    const messageContainer = document.querySelector('#message');

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
        const applicationIds = Array.from(checkboxes).map(checkbox => checkbox.value);
        const submitAction = event.submitter.value;

        if (checkboxes.length === 0) {
            messageContainer.innerHTML = "<div class='alert alert-danger'>하나 이상의 작품을 선택해야 합니다.</div>";
            return;
        }

        const formData = {
            submitAction: submitAction,
            applications: applicationIds
        };

        handleFormSubmit(event, form, formData, messageContainer);
    });

    // 검색 필드 전환 로직
    // 초기화 시 성별 선택 드롭다운 숨기기
    toggleSearchInput(searchFieldDropdown.value);

    // 검색 필드 선택 변경 시 이벤트 핸들러
    searchFieldDropdown.addEventListener('change', function() {
        toggleSearchInput(this.value);
    });

    // 검색 조건 초기화 버튼 동작
    resetButton.addEventListener('click', function() {
        window.location.href = window.location.pathname;  // 쿼리 파라미터 제거하고 페이지 새로고침
    });
});
