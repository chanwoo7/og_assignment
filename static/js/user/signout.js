document.addEventListener('DOMContentLoaded', function () {
    const signoutLink = document.querySelector('#signoutLink');  // 로그아웃 링크 선택

    if (signoutLink) {
        signoutLink.addEventListener('click', function (e) {
            e.preventDefault();

            // 폼 객체 없이 빈 데이터와 빈 메시지 컨테이너 전달
            const formData = {};
            const messageContainer = '';

            handleFormSubmit(e, { action: '/user/signout/' }, formData, messageContainer, "/");
        });
    }
});