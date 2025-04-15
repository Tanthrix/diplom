document.addEventListener('DOMContentLoaded', function () {

    document.body.classList.add('page-transition-enter');
    document.body.classList.add('page-transition-enter-active');


    document.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', function (e) {

            const href = this.getAttribute('href');
            if (!href || href.startsWith('#') || href.includes('://') || href === '/logout/') {
                return;
            }

            e.preventDefault();
            document.body.classList.add('page-transition-exit');
            document.body.classList.add('page-transition-exit-active');


            setTimeout(() => {
                window.location.href = href;
            }, 500);
        });
    });
});