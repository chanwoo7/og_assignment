document.addEventListener('DOMContentLoaded', function() {
    const searchFieldDropdown = document.querySelector('#search_field');
    const resetButton = document.querySelector('#reset-button');

    // 검색 필드 전환, 초기화
    toggleSearchFieldOfUser(searchFieldDropdown.value);

    // 검색 필드 선택 변경 시 이벤트 핸들러
    searchFieldDropdown.addEventListener('change', function() {
        toggleSearchFieldOfUser(this.value);
    });

    // 검색 조건 초기화 버튼 동작
    resetButton.addEventListener('click', function() {
        window.location.href = window.location.pathname;  // 쿼리 파라미터 제거하고 페이지 새로고침
    });
});
