const burgerMenu = document.querySelector('#burger-menu');

const secretMenu = document.querySelector('.secret-menu');

burgerMenu.addEventListener('click', () => {
    burgerMenu.classList.toggle('active');
    secretMenu.classList.toggle('active');
});