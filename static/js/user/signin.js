document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('#form');

    form.addEventListener('submit', function (e) {
        e.preventDefault();

        const formData = new FormData(form);

        fetch('/user/signin/', {
            method: 'POST',
            headers: {
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
            },
            body: formData,
        })
        .then(response => response.json())
        .then(data => {
            const messageElement = document.querySelector('#message');

            if (data.success) {
                window.location.href = "/";
            } else {
                messageElement.innerHTML = data.error;
                messageElement.style.color = 'red';
            }
        })
        .catch(error => console.error('Error:', error));
    });
});
