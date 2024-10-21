document.addEventListener('DOMContentLoaded', function () {
    const signoutLink = document.querySelector('#signoutLink');  // 로그아웃 링크 선택

    signoutLink.addEventListener('click', function (e) {
        e.preventDefault();

        // CSRF 토큰 가져오기
        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

        fetch('/user/signout/', {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrfToken,
            },
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                window.location.href = "/";  // 로그아웃 후 홈 페이지로 리다이렉트
            }
        })
        .catch(error => console.error('Error:', error));
    });
});