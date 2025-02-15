document.addEventListener('DOMContentLoaded', function () {
    const buttons = document.querySelectorAll('.clubs__btn');
    const select = document.getElementById('region-select');
    const cards = document.querySelectorAll('.clubs__card');

    function filterCards(regionId) {
        cards.forEach(card => {
            if (regionId === 'all') {
                card.style.display = 'block'; // Показываем все карточки
            } else if (card.getAttribute('data-region') === regionId) {
                card.style.display = 'block';
            } else {
                card.style.display = 'none';
            }
        });
    }

    buttons.forEach(button => {
        button.addEventListener('click', function () {
            const regionId = this.getAttribute('data-region');
            filterCards(regionId);
        });
    });

    select.addEventListener('change', function () {
        const regionId = this.value;
        filterCards(regionId);
    });

    // Показываем все карточки при загрузке страницы
    cards.forEach(card => {
        card.style.display = 'block';
    });
});