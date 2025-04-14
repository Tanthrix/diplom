document.addEventListener('DOMContentLoaded', function () {
    // Добавляем класс для анимации появления при загрузке страницы
    document.body.classList.add('page-transition-enter');
    document.body.classList.add('page-transition-enter-active');

    // Перехватываем клики по всем ссылкам
    document.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', function (e) {
            // Исключаем ссылки, которые не ведут на другие страницы (например, якоря или внешние ссылки)
            const href = this.getAttribute('href');
            if (!href || href.startsWith('#') || href.includes('://') || href === '/logout/') {
                return;
            }

            e.preventDefault();
            document.body.classList.add('page-transition-exit');
            document.body.classList.add('page-transition-exit-active');

            // Задержка перед переходом, чтобы анимация завершилась
            setTimeout(() => {
                window.location.href = href;
            }, 500); // Должно совпадать с длительностью transition в CSS
        });
    });
});