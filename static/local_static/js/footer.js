// Get the current year from the Date object
const currentYear = new Date().getFullYear();

// Select the element with the ID 'year' and check if it exists
const yearElement = document.getElementById('year');
if (yearElement) {
    // If the element exists, set its text content to the current year
    yearElement.textContent = currentYear;
}
