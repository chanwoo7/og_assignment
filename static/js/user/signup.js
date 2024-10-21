document.querySelector('form').addEventListener('submit', function (e) {
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
        if (data.success) {
            window.location.href = "/";
        } else {
            console.log(data.errors);
        }
    })
    .catch(error => console.error('Error:', error));
});
