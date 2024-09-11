// Wait for the DOM content to be fully loaded before executing any JavaScript
document.addEventListener('DOMContentLoaded', () => {
    // Get the form element by its ID
    const form = document.getElementById("form");

    // Check if the form element exists to avoid potential errors
    if (!form) {
        console.error("Form element not found."); // Log an error message if the form is not found
        return; // Exit the function if the form is not present
    }

    // Get the submit button inside the form
    const submitButton = form.querySelector('button[type="submit"]');

    // Variable to track if any changes have been made to the form
    let formChanged = false;

    // Add an event listener for any input changes in the form
    form.addEventListener('input', () => {
        formChanged = true; // Mark the form as changed whenever the user modifies any input field
    });

    // Add an event listener for the form submission
    form.addEventListener('submit', submitHandler);

    // Function to handle form submission
    function submitHandler(e) {
        e.preventDefault(); // Prevent the default form submission behavior

        // Change the submit button text and disable it to prevent multiple submissions
        submitButton.textContent = 'Sending message, please wait...';
        submitButton.disabled = true;

        // Send the form data using the Fetch API
        fetch(form.action, {
            method: 'POST', // Use the POST method to submit form data
            body: new FormData(form), // Include the form data
        })
        .then(response => {
            // Check if the response content type is JSON
            const contentType = response.headers.get("content-type");
            if (contentType && contentType.includes("application/json")) {
                return response.json(); // Parse the response as JSON if the content type is correct
            }
            throw new Error("Unexpected response type"); // Throw an error if the content type is not JSON
        })
        .then(data => {
            // Handle the response data
            if (data.message === 'success') { // Check if the response message indicates success
                alert('Thank you for your message! We will get back to you soon.'); // Show success alert
                form.reset(); // Reset the form fields
                formChanged = false; // Reset the form change tracker
            } else {
                throw new Error('Submission was not successful! Please try again.'); // Handle unsuccessful submission
            }
        })
        .catch(error => {
            // Handle any errors that occur during form submission
            console.error('Error:', error); // Log the error to the console
            alert('There was a problem submitting your form. Please try again later.'); // Show error alert to the user
        })
        .finally(() => {
            // Re-enable the submit button and reset its text after the form submission attempt
            submitButton.textContent = 'Send Message';
            submitButton.disabled = false;
        });
    }

    // Add an event listener for when the user attempts to leave the page
    window.addEventListener('beforeunload', (event) => {
        if (formChanged) { // Check if the form has been changed
            event.preventDefault(); // Prevent the page from unloading immediately
            event.returnValue = ''; // Show a confirmation dialog in some browsers
        }
    });
});
