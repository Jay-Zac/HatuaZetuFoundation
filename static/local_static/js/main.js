// Wait for the DOM to be fully loaded before running the script
document.addEventListener('DOMContentLoaded', function() {
    // **Navigation Menu Functionality**
    const burger = document.querySelector('.burger'); // Select the burger icon for mobile navigation
    const nav = document.querySelector('.nav-links'); // Select the navigation links container
    const navLinks = document.querySelectorAll('.nav-links li'); // Select all individual navigation links

    // Function to toggle the navigation menu
    function toggleNav() {
        nav.classList.toggle('nav-active'); // Toggle the active class to show/hide navigation
        burger.classList.toggle('toggle'); // Toggle the burger icon animation

        // Add animation to each navigation link
        navLinks.forEach((link, index) => {
            // Check if the animation is already applied and toggle accordingly
            link.style.animation = link.style.animation ? '' : `navLinkFade 1s ease forwards ${index / 5 + 0.5}s`;
        });
    }

    // Add event listeners to the burger menu and navigation links
    if (burger && nav && navLinks.length > 0) {
        burger.addEventListener('click', toggleNav); // Toggle navigation when burger icon is clicked
        navLinks.forEach(link => link.addEventListener('click', toggleNav)); // Close navigation when a link is clicked
    }

    // Close navigation when clicking outside of it
    document.addEventListener('click', function(event) {
        const isClickInsideNav = nav.contains(event.target); // Check if click is inside navigation
        const isClickOnBurger = burger.contains(event.target); // Check if click is on the burger icon

        // Close navigation if clicked outside and it is currently active
        if (!isClickInsideNav && !isClickOnBurger && nav.classList.contains('nav-active')) {
            toggleNav();
        }
    });

    // **Slide Show Functionality**
    const slides = document.querySelectorAll('.slide'); // Select all slide elements
    let currentIndex = 0; // Initialize the current slide index

    // Function to show the next slide
    function showNextSlide() {
        slides[currentIndex].classList.remove('active'); // Remove 'active' class from the current slide
        currentIndex = (currentIndex + 1) % slides.length; // Increment index and loop back to the first slide if needed
        slides[currentIndex].classList.add('active'); // Add 'active' class to the new current slide
    }

    // Automatically change slides every 5 seconds if slides are present
    if (slides.length > 0) {
        setInterval(showNextSlide, 5000); // Set interval for the slide transition
    }

    // **Initial Fade-in Animation for the Main Content**
    const mainDetailContainer = document.querySelector('.main-detail-container'); // Select the main content container
    if (mainDetailContainer) {
        mainDetailContainer.classList.add('fade-in'); // Add fade-in class to animate content appearance
    }

    // **Scroll Animation for Elements**
    const revealElements = () => {
        const cards = document.querySelectorAll('.main-detail-card'); // Select all detail cards
        const scrollPosition = window.scrollY + window.innerHeight; // Get current scroll position

        cards.forEach(card => {
            const cardOffset = card.getBoundingClientRect().top + window.scrollY; // Calculate card's position
            if (cardOffset < scrollPosition - 100) {
                // Show card when it comes into view
                card.style.opacity = '1';
                card.style.transform = 'translateY(0)';
            } else {
                // Hide card when it is out of view
                card.style.opacity = '0';
                card.style.transform = 'translateY(30px)';
            }
        });
    };

    // Trigger scroll animations
    window.addEventListener('scroll', revealElements);
    revealElements(); // Run on initial load to handle any already visible elements

    // **Message Auto-hide and Close Button Functionality**
    document.querySelectorAll('.message').forEach(message => {
        // Automatically hide messages after 5 seconds
        setTimeout(() => message.classList.add('fade-out'), 5000);

        const closeButton = message.querySelector('.message-close-btn'); // Select the close button within the message
        if (closeButton) {
            // Hide the message when close button is clicked
            closeButton.addEventListener('click', () => {
                message.classList.add('fade-out');
            });
        }
    });

    // **Back to Top Button Functionality**
    const backToTopButton = document.getElementById('back-to-top'); // Select the 'back to top' button
    let hideTimeout;
    let scrollTimeout;

    // Function to show the 'back to top' button
    function showBackToTopButton() {
        backToTopButton.classList.add('show'); // Show button
        clearTimeout(hideTimeout); // Clear any existing timeout to hide the button
        hideTimeout = setTimeout(() => {
            backToTopButton.classList.remove('show'); // Hide the button after 5 seconds
        }, 5000);
    }

    // Show or hide the 'back to top' button based on scroll position
    window.addEventListener('scroll', () => {
        if (window.scrollY > 100) {
            showBackToTopButton(); // Show button if scrolled down more than 100 pixels
        } else {
            backToTopButton.classList.remove('show'); // Hide button if near the top of the page
        }
        clearTimeout(scrollTimeout); // Clear any previous scroll timeout
        scrollTimeout = setTimeout(() => {
            if (window.scrollY > 100) {
                backToTopButton.classList.remove('show'); // Hide the button after 5 seconds of inactivity
            }
        }, 5000);
    });

    // Smooth scroll to the top when the button is clicked
    if (backToTopButton) {
        backToTopButton.addEventListener('click', () => {
            window.scrollTo({ top: 0, behavior: 'smooth' }); // Smooth scroll to top
            showBackToTopButton(); // Show the button while scrolling
        });
    }

    // Show the button on touch events
    window.addEventListener('touchstart', showBackToTopButton);

    // **Cookies Consent Script**
    const loader = document.querySelector('.loader'); // Select the loader element
    const cookiesConsent = document.getElementById('cookies-consent'); // Select the cookies consent banner
    const acceptCookiesButton = document.getElementById('accept-cookies'); // Select the 'Accept Cookies' button
    const rejectCookiesButton = document.getElementById('reject-cookies'); // Select the 'Reject Cookies' button
    const cookiesAccepted = localStorage.getItem('cookiesAccepted'); // Check if cookies were accepted
    const cookiesRejected = localStorage.getItem('cookiesRejected'); // Check if cookies were rejected

    // Hide the loader once the page is fully loaded
    window.addEventListener('load', function() {
        if (loader) {
            loader.classList.add('hidden'); // Add class to hide loader
        }
    });

    // Check cookie consent status and hide the banner if already accepted or rejected
    if (cookiesConsent && (cookiesAccepted || cookiesRejected)) {
        cookiesConsent.style.display = 'none'; // Hide the consent banner
    } else if (cookiesConsent) {
        // Handle 'Accept Cookies' button click
        acceptCookiesButton.addEventListener('click', function() {
            localStorage.setItem('cookiesAccepted', 'true'); // Save acceptance to localStorage
            cookiesConsent.style.display = 'none'; // Hide the consent banner
        });

        // Handle 'Reject Cookies' button click
        rejectCookiesButton.addEventListener('click', function() {
            localStorage.setItem('cookiesRejected', 'true'); // Save rejection to localStorage
            cookiesConsent.style.display = 'none'; // Hide the consent banner
        });
    }
});
