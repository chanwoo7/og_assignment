// 검색 필드에 따라 검색어 입력 필드, 성별 드롭다운, 생년월일 입력 필드 표시
function toggleSearchFieldOfUser(selectedField) {
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

// 검색 필드에 따라 검색어 입력 필드, 최소값-최대값 입력 필드 표시
function toggleSearchFieldOfArtwork(selectedField) {
    const searchInputWrapper = document.querySelector('#search-input-wrapper');
    const rangeFields = document.querySelector('.range-fields');

    if (selectedField === 'price' || selectedField === 'size') {
        searchInputWrapper.classList.add('d-none');  // 단일 검색어 입력 필드 숨김
        rangeFields.classList.remove('d-none');  // 범위 검색 필드 표시
    } else {
        searchInputWrapper.innerHTML = `
            <input type="text" name="q" class="form-control" placeholder="검색어 입력" value="">
        `;
        searchInputWrapper.classList.remove('d-none');  // 단일 검색어 입력 필드 표시
        rangeFields.classList.add('d-none');  // 범위 검색 필드 숨김
    }
}