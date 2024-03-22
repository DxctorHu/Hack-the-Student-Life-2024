// hello.js

// Display an alert message
//alert("Message Saved");

// hello.js

// Function to send data to the Lambda function
function sendData(selectedText, currentUrl) {
    const lambdaUrl = `https://ozm33yhroqc4elpy77diwq6vxe0hgeya.lambda-url.us-west-2.on.aws?user_text=Michael&user_email_text=michaelmoshui@gmail.com&original_text=${selectedText}&url_text=${currentUrl}`;
    fetch(lambdaUrl)
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        alert('Message Saved'); // Show success message to the user
    })
    .catch((error) => {
        console.error('Error:', error);
        alert('Error saving message'); // Show error message to the user
    });
}

// Execute when the script is loaded
(function() {
    const selectedText = window.getSelection().toString();
    const currentUrl = window.location.href;

    // Check if there's selected text
    if (selectedText) {
        sendData(selectedText, currentUrl);
    }
})();
