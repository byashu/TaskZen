const navbar = document.querySelector(".navbar");

window.addEventListener("scroll", function () {

    if (window.scrollY > 210) {
        navbar.classList.remove("navbar-top");
        navbar.classList.add("navbar-scrolled");
    }
    else {
        navbar.classList.remove("navbar-scrolled");
        navbar.classList.add("navbar-top");
    }

});

const sections = document.querySelectorAll(".fade-section");

window.addEventListener("scroll", () => {
    sections.forEach(section => {
        const sectionTop = section.getBoundingClientRect().top;
        const screenHeight = window.innerHeight;

        if (sectionTop < screenHeight - 100) {
            section.classList.add("show");
        }
    });
});