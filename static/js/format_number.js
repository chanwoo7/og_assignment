// 숫자 포맷팅 함수
function formatNumber(value) {
    value = value.split('.')[0];  // 소숫점 아래의 숫자 제거
    value = value.replace(/\D/g, '');  // 숫자만 남김
    return value.replace(/\B(?=(\d{3})+(?!\d))/g, ',');  // 천 단위마다 콤마 추가
}
