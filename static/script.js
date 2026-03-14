// === active nav link ===
const navLinks = document.querySelectorAll('.primary-nav a[href^="/"], .nav-mobile a[href^="/"]');
function setActiveNav(href) {
    navLinks.forEach(link => {
        link.classList.toggle('active', link.getAttribute('href') === href);
    });
}
navLinks.forEach(link => {
    link.addEventListener('click', () => setActiveNav(link.getAttribute('href')));
});

// === makes sure deault home button is active when going into the page
const path = window.location.pathname;
const homePaths = ['/', '/english', '/danish', '/japanese'];
setActiveNav(homePaths.includes(path) ? '/home' : path);

