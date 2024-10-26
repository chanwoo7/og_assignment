document.addEventListener('DOMContentLoaded', function() {
    const selectAllCheckbox = document.querySelector('#select-all');
    const form = document.querySelector('#application-form');
    const searchFieldDropdown = document.querySelector('#search_field');
    const resetButton = document.querySelector('#reset-button');
    const messageContainer = document.querySelector('#message');
    const downloadLink = document.querySelector('#csv-download-link'); // CSV 다운로드 링크

    // 체크박스 일괄 선택
    if (selectAllCheckbox) {
        selectAllCheckbox.addEventListener('change', function() {
            const checkboxes = document.querySelectorAll('input[name="applications"]');
            for (const checkbox of checkboxes) {
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

    // 검색 필드 전환, 초기화
    toggleSearchFieldOfUser(searchFieldDropdown.value);

    // 검색 필드 선택 변경 시 이벤트 핸들러
    searchFieldDropdown.addEventListener('change', function() {
        toggleSearchFieldOfUser(this.value);
        updateDownloadLink(); // 검색 필드 변경 시 다운로드 링크 업데이트
    });

    // 검색어 입력 필드가 변경될 때마다 다운로드 링크 업데이트
    document.querySelector('#search-input-wrapper').addEventListener('input', updateDownloadLink);

    // 검색 조건 초기화 버튼 동작
    resetButton.addEventListener('click', function() {
        window.location.href = window.location.pathname; // 쿼리 파라미터 제거하고 페이지 새로고침
    });

    // CSV 다운로드 링크 업데이트 함수
    function updateDownloadLink() {
        const searchFieldVal = searchFieldDropdown.value;
        const searchInput = document.querySelector('#search-input-wrapper input, #search-input-wrapper select'); // 검색어 입력 필드 (동적)
        const searchQueryVal = searchInput ? searchInput.value : '';

        const baseUrl = downloadLink.getAttribute('data-url'); // 기본 URL 가져오기

        // URL에 검색 조건 쿼리 파라미터 추가
        downloadLink.href = `${baseUrl}?search_field=${encodeURIComponent(searchFieldVal)}&q=${encodeURIComponent(searchQueryVal)}`;
    }

    // 페이지 로드 시 링크 초기 업데이트
    updateDownloadLink();
});
