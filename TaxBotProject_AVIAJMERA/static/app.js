
document.getElementById('query-form').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const userQuery = document.getElementById('user-query').value;
    displayMessage('User', userQuery);
    
    const response = await fetch('/query', {
        method: 'POST',
        body: JSON.stringify({ query: userQuery }),
        headers: {
            'Content-Type': 'application/json'
        }
    });
    
    const data = await response.json();
    displayMessage('Bot', data.bot_response);
});

function displayMessage(sender, message) {
    const chatBox = document.getElementById('chat-box');
    chatBox.innerHTML += `<p><strong>${sender}:</strong> ${message}</p>`;
}

// Clearing the textbox after sending a message
document.getElementById('query-form').addEventListener('submit', function() {
    setTimeout(function() {
        document.getElementById('user-query').value = '';
    }, 10);
});

// Implementing the cancel button functionality to refresh the page
document.getElementById('cancel-btn').addEventListener('click', function() {
    location.reload();
});
