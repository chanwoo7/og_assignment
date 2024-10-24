function handleFormSubmit(event, form, formData, messageContainer) {
    event.preventDefault();

    fetch(form.action, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
        },
        body: JSON.stringify(formData),
    })
    .then(response => response.json())
    .then(data => {
        messageContainer.innerHTML = '';

        if (data.success) {
            alert("성공적으로 처리되었습니다.");
            window.location.href = "/";  // TODO: 리다이렉트 주소도 parameter 처리할 것
        } else {
            let errorMessage = '';
            try {
                for (let [field, errors] of Object.entries(data.errors)) {
                    errorMessage += `${field}: ${errors.join(', ')}<br>`;
                }
            } catch {  // 배열이 아니라면
                errorMessage += data.error;
            }
            messageContainer.innerHTML = "<div class='alert alert-danger'>" + errorMessage + "</div>";
            messageContainer.style.color = 'red';
        }
    })
    .catch(error => {
        messageContainer.innerHTML = "<div class='alert alert-danger'>서버와 통신 중 오류가 발생했습니다.</div>";
        console.error('Error:', error);
    });
}