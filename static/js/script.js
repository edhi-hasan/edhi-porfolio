// scripts.js
document.addEventListener('DOMContentLoaded', function() {
    const menuIcon = document.querySelector('#menu-icon');
    const navbar = document.querySelector('.navbar');

    menuIcon.onclick = () => {
        menuIcon.classList.toggle('bx-x'); // Toggle an additional class on the icon
        navbar.classList.toggle('active'); // Toggle visibility of the navbar
    };
});
