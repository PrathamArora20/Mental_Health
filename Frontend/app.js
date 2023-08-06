// app.js

function sendMessage() {
    const messageInput = document.querySelector('input[name="message"]');
    const messagesBody = document.querySelector('.body');

    const userMessage = messageInput.value.trim();
    if (userMessage !== '') {
        const userMessageElement = document.createElement('p');
        userMessageElement.classList.add('message', 'user_msg');
        userMessageElement.textContent = userMessage;

        messagesBody.appendChild(userMessageElement);

        messageInput.value = '';
    }
}

function handleEnterKey(event) {
    if (event.keyCode === 13) {
        // If the Enter key is pressed, call sendMessage()
        sendMessage();

        // Prevent form submission (in case the input is inside a form)
        event.preventDefault();
    }
}


function botMessage(message) {

    const messagesBody = document.querySelector('.body');
    if (message !== '') {
        const msg = document.createElement('p');
        msg.classList.add('message');
        msg.textContent = message;

        messagesBody.appendChild(msg);
    }
}