document.addEventListener('DOMContentLoaded', function () {
    const buttons = document.querySelectorAll('.clubs__btn');
    const select = document.getElementById('region-select');
    const cards = document.querySelectorAll('.clubs__card');
    const clubSwiper = document.getElementById('clubSwiper')

    function filterCards(regionId, cityId) {
        console.log(regionId, cityId)
        cards.forEach(card => {
            if (regionId === 'all') {
                card.style.display = 'block';
            } else if (card.getAttribute('data-city') == cityId) {
                console.log("фильтр по сити")
                card.style.display = 'block';
            } else if (card.getAttribute('data-region') === regionId) {
                console.log("фильтр по регион")
                card.style.display = 'block';
            } else {
                card.style.display = 'none';
            }
        });
        clubSwiper.swiper.slideTo(0);
    }

    buttons.forEach(button => {
        button.addEventListener('click', function () {

            buttons.forEach(btn => {
                btn.style.backgroundColor = 'white';
                btn.style.color = 'black';
            });

            if (this.getAttribute('data-region') === '5') {
                let minskButton = document.getElementById('minskButton')
                minskButton.style.backgroundColor = '#328ca7';
                minskButton.style.color = 'white';
            }

            this.style.backgroundColor = '#328ca7';
            this.style.color = 'white';

            const regionId = this.getAttribute('data-region');
            const cityID = Number(this.getAttribute('data-city'));
            filterCards(regionId, cityID);
        });
    });

    select.addEventListener('change', function () {
        const regionId = this.value;
        const cityID = this.value;
        filterCards(regionId, cityID);
    });

    cards.forEach(card => {
        card.style.display = 'block';
    });
});