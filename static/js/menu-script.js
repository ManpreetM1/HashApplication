     //Opens side menu, hides menu icon, and displays overlay, which can be clicked on to close menu
     function toggleMenu() {
        const menu = document.getElementById('menu');
        const icon = document.querySelector('.menu-icon');
        const overlay = document.getElementById('overlay');
        menu.classList.toggle('open');
        icon.classList.toggle('open');
        overlay.classList.add('show');
    }

    //Closes side menu, shows menu icon, and removes overlay
    function closeMenu() {
        const menu = document.getElementById('menu');
        const icon = document.querySelector('.menu-icon');
        const overlay = document.getElementById('overlay');
        menu.classList.toggle('open');
        icon.classList.toggle('open');
        overlay.classList.remove('show');
    }