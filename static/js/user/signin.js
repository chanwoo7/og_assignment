document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('#form');
    const messageContainer = document.querySelector('#message');

    form.addEventListener('submit', function (e) {
        e.preventDefault();

        const formData = {
            username: document.querySelector('#username').value,
            password: document.querySelector('#password').value,
        }

        handleFormSubmit(event, form, formData, messageContainer);
    });
});
