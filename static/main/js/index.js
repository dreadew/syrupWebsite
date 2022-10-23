const menuBtn = document.querySelector(".nav-menu");
const menu = document.querySelector(".nav-list__mobile");
menuBtn.addEventListener("click", (e) => {
    menu.classList.toggle('active');
    menuBtn.classList.toggle('active');
})