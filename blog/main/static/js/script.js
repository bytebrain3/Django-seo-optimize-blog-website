document.addEventListener('DOMContentLoaded', function() {
    let currentTheme = localStorage.getItem('theme') || 'light';
    const iconSun = document.getElementById('icon-sun');
    const iconMoon = document.getElementById('icon-moon');
    const themeOptions = document.querySelectorAll('.theme-controller');
    const themeMenuToggle = document.getElementById('theme-menu-toggle');
    const themeLabels = document.querySelectorAll('.theme-option');

    // Initialize theme and icon on page load
    function setThemeIcon(theme) {
        if (theme === 'mytheme') {
            iconSun.classList.add('hidden');
            iconMoon.classList.remove('hidden');
        } else {
            iconSun.classList.remove('hidden');
            iconMoon.classList.add('hidden');
        }
    }
    document.documentElement.setAttribute('data-theme', currentTheme);
    setThemeIcon(currentTheme);

    // Apply/remove 'btn-ghost' based on active theme
    function updateActiveThemeLabel(theme) {
        themeLabels.forEach((label) => {
            if (label.dataset.theme === theme) {
                label.classList.remove('btn-ghost');
            } else {
                label.classList.add('btn-ghost');
            }
        });
    }

    updateActiveThemeLabel(currentTheme);

    // Handle hover effects
    themeLabels.forEach((label) => {
        label.addEventListener('mouseenter', function() {
            this.classList.remove('btn-ghost');
        });

        label.addEventListener('mouseleave', function() {
            if (this.querySelector('input').value !== currentTheme) {
                this.classList.add('btn-ghost');
            }
        });
    });

    // Open the dropdown menu when clicking on the icon (Sun/Moon)
    themeMenuToggle.addEventListener('click', (e) => {
        e.stopPropagation(); // Prevent theme toggle on click
    });

    // Change theme based on the selected option
    themeOptions.forEach((option) => {
        option.addEventListener('change', (e) => {
            const selectedTheme = e.target.value;
            document.documentElement.setAttribute('data-theme', selectedTheme);
            localStorage.setItem('theme', selectedTheme);
            currentTheme = selectedTheme;

            // Update the icon based on the theme
            setThemeIcon(selectedTheme);

            // Update the active label's class
            updateActiveThemeLabel(selectedTheme);
        });
    });
});




document.addEventListener('DOMContentLoaded', () => {
    let lastScrollTop = 0;
    const navbar = document.querySelector('.navbar');

    window.addEventListener('scroll', () => {

        const currentScrollTop = window.pageYOffset || document.documentElement.scrollTop;

        if (currentScrollTop > lastScrollTop) {
            // Scrolling down
            navbar.classList.add('navbar-hidden');

        } else {
            // Scrolling up
            navbar.classList.remove('navbar-hidden');

        }

        lastScrollTop = currentScrollTop <= 0 ? 0 : currentScrollTop; // For Mobile or negative scrolling
    });
});

function showCommandPalette() {
    const palette = document.getElementById('command-palette');
    palette.classList.remove('hidden');
    palette.classList.add('show');
    palette.querySelector('input[type="text"]').focus();
}

function hideCommandPalette(event) {
    const palette = document.getElementById('command-palette');
    if (event.target === palette || event.key === "Escape" || event.target.closest('button[onclick*="hideCommandPalette"]')) {
        palette.classList.add('hidden');
        palette.classList.remove('show');
    }
}

document.addEventListener('click', hideCommandPalette);
document.addEventListener('keydown', hideCommandPalette);




// Check if cookies are accepted
function checkCookieConsent() {
    return document.cookie.split(';').some(cookie => cookie.trim().startsWith('cookies_accepted='));
}

// Check if cookies are rejected
function checkCookieRejection() {
    return document.cookie.split(';').some(cookie => cookie.trim().startsWith('cookies_rejected='));
}

// Show the cookie consent banner if neither acceptance nor rejection cookie is found
window.onload = function() {
    if (!checkCookieConsent() && !checkCookieRejection()) {
        document.getElementById('cookies-card').classList.remove('hidden');
    }
};

// Accept cookies
function acceptCookies() {
    document.cookie = "cookies_accepted=true; path=/; max-age=31536000"; // 1 year
    document.getElementById('cookies-card').classList.add('hidden');
}

// Reject cookies
function rejectCookies() {
    // Remove the cookies_accepted cookie (if it exists)
    document.cookie = "cookies_accepted=; path=/; max-age=0";

    // Set a cookie to track the rejection, expiring in 1 day
    document.cookie = "cookies_rejected=true; path=/; max-age=86400"; // 1 day

    // Hide the cookie consent banner
    document.getElementById('cookies-card').classList.add('hidden');
}

// Set a cookie with a specified name, value, and expiration
function setCookie(name, value, days) {
    let expires = "";
    if (days) {
        const date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000)); // Set expiration date
        expires = "; expires=" + date.toUTCString();
    }
    document.cookie = name + "=" + (value || "") + expires + "; path=/";
}

// Get a cookie by name
function getCookie(name) {
    const nameEQ = name + "=";
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
        let cookie = cookies[i];
        while (cookie.charAt(0) === ' ') {
            cookie = cookie.substring(1);
        }
        if (cookie.indexOf(nameEQ) === 0) {
            return cookie.substring(nameEQ.length, cookie.length);
        }
    }
    return null;
}

// Append search input to the search history cookie
function appendToSearchHistory(searchTerm) {
    let history = getCookie('searchHistory');
    let searchHistory = [];

    if (history) {
        searchHistory = JSON.parse(history);
    }

    searchHistory.push(searchTerm);
    setCookie('searchHistory', JSON.stringify(searchHistory), 365); // Cookie expires in 365 days
}

// Handle form submission
document.getElementById('searchForm').addEventListener('submit', function(event) {
    var searchInput = document.getElementById('searchInput').value.trim();
    if (searchInput.length === 0) {
        // Prevent form submission if input is empty
        event.preventDefault();
        alert('Please enter a search term.');
    } else {
        if (checkCookieConsent()) {
            // Append the search term to the search history cookie if consent is given
            appendToSearchHistory(searchInput);
        } else {
            // Handle the case where cookie consent is not given
            alert('Cookie consent is required to save your search history.');
        }
    }
});


function goBack() {
    window.history.back();
}