document.addEventListener('DOMContentLoaded', function () {
    document.querySelector('#form').addEventListener('submit', function (e) {
        e.preventDefault();

        const formData = {
            username: document.querySelector('#username').value,
            password: document.querySelector('#password').value,
            password2: document.querySelector('#password2').value,
        };

        fetch('/user/signup/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
            },
            body: JSON.stringify(formData),
        })
            .then(response => response.json())
            .then(data => {
                const messageElement = document.querySelector('#message');

                if (data.success) {
                    window.location.href = "/user/signin";
                } else {
                    // 오류 메시지를 표시
                    let errorMessage = '';
                    for (let [field, errors] of Object.entries(data.errors)) {
                        errorMessage += `${field}: ${errors.join(', ')}<br>`;
                    }
                    messageElement.innerHTML = errorMessage;
                    messageElement.style.color = 'red';
                }
            })
            .catch(error => console.error('Error:', error));
    })
});