document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.menu-item:has(.submenu) > a').forEach(link => {
        link.addEventListener('click', function(e) {
            if (this.getAttribute('href') !== '#') return;

            e.preventDefault();
            const menuItem = this.parentElement;
            menuItem.classList.toggle('expanded');
        });
    });
});