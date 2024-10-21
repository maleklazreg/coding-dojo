let isLogIn = false; // Track the login state

// Function to toggle login/logout
function funLogin(button) {
    isLogIn = !isLogIn; // Toggle the state

    if (isLogIn) {
        button.textContent = "Logout"; // Change button text to Logout
    } else {
        button.textContent = "Login"; // Change button text back to Login
    }
}
function removeDefinition(button) {
    button.remove(); // Remove the button from the DOM
}
