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

// === home section clicks → SPA navigation (no HTML changes)
const SPA_CONTAINER = document.getElementById('SPA-container');
if (SPA_CONTAINER) {
    SPA_CONTAINER.addEventListener('click', (e) => {
        const section = e.target.closest('.home-services, .home-project, .home-abilities');
        if (!section || typeof mix_fetch !== 'function') return;
        const url = section.classList.contains('home-services') ? '/services'
            : section.classList.contains('home-project') ? '/projects'
            : '/abilities';
        e.preventDefault();
        mix_fetch(url, 'GET', false, true, false, false);
        setActiveNav(url);
    });
}



