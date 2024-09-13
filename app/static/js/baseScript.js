let menuBox = document.getElementById('menuBox');
let menuIcon = document.getElementById('menu-icon');
let sidenavIcon = document.getElementById('side-navLogo');

// Use Flask to generate the URL on the server-side
const menuIconOpen = "static/img/close.png";
const menuIconClosed = "/static/img/menu.png";

menuIcon.onclick = () => {
    menuBox.classList.toggle('open-menu');
    if (menuBox.classList.contains('open-menu')) {
        // Use the pre-generated URL here
        menuIcon.src = menuIconOpen;
    } else {
        // Use the pre-generated URL here
        menuIcon.src = menuIconClosed;
    }
};

sidenavIcon.onclick = () => {
    // Add functionality if needed
}

const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        console.log(entry);
        if (entry.isIntersecting) {
            entry.target.classList.add('show');
        } else {
            entry.target.classList.remove('show');
        }
    });
});

const hiddenElements = document.querySelectorAll('.hidden');
hiddenElements.forEach((el) => {
    observer.observe(el);
});