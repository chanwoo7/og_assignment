// 소숫점 제거 및 천 단위로 콤마 추가
function formatNumber(value) {
    value = value.split('.')[0];  // 소숫점 아래의 숫자 제거
    value = value.replace(/\D/g, '');  // 숫자만 남김
    return value.replace(/\B(?=(\d{3})+(?!\d))/g, ',');  // 천 단위마다 콤마 추가
}

document.addEventListener('DOMContentLoaded', function() {
    const searchFieldDropdown = document.querySelector('#search_field');
    const resetButton = document.querySelector('#reset-button');
    const prices = document.querySelectorAll('.price');
    const minValueInput = document.querySelector('#min_value');
    const maxValueInput = document.querySelector('#max_value');

    // 최소값, 최대값 필드가 페이지 로드 후에도 포맷팅되도록 초기 값 처리
    if (minValueInput.value) {
        minValueInput.value = formatNumber(minValueInput.value);
    }

    if (maxValueInput.value) {
        maxValueInput.value = formatNumber(maxValueInput.value);
    }

    // 최소값, 최대값 입력값 -> 포맷팅
    minValueInput.addEventListener('input', function(e) {
        e.target.value = formatNumber(e.target.value);
    });

    maxValueInput.addEventListener('input', function(e) {
        e.target.value = formatNumber(e.target.value);
    });

    // 테이블 상 가격 -> 포맷팅
    prices.forEach(function (priceElement) {
        const originalPrice = priceElement.getAttribute('data-price');
        priceElement.textContent = formatNumber(originalPrice);
    });

    // 폼 제출 시 쉼표를 제거하고 순수 숫자로 변환
    document.querySelector('form').addEventListener('submit', function() {
        minValueInput.value = minValueInput.value.replace(/,/g, '');
        maxValueInput.value = maxValueInput.value.replace(/,/g, '');
    });

    // 검색 필드 전환, 초기화
    toggleSearchFieldOfArtwork(searchFieldDropdown.value);

    // 검색 필드 선택 변경 시 이벤트 핸들러
    searchFieldDropdown.addEventListener('change', function() {
        toggleSearchFieldOfArtwork(this.value);
    });

    // 검색 조건 초기화 버튼 동작
    resetButton.addEventListener('click', function() {
        window.location.href = window.location.pathname;  // 쿼리 파라미터 제거하고 페이지 새로고침
    });
});
