const swiper = new Swiper(".mySwiper1", {
  direction: "horizontal",
  effect: "coverflow",
  grabCursor: true,
  centeredSlides: true,
  slidesPerView: "auto",
  coverflowEffect: {
    rotate: 0,
    stretch: 0,
    depth: 100,
    modifier: 2,
    slideShadows: true,
  },
  loop: true,
  loopedSlides: 3,
  autoplay: {
    delay: 9000,
    disableOnInteraction: false,
  },
  slideToClickedSlide: true,
  simulateTouch: true,
});

const swiper2 = new Swiper(".mySwiper2", {
  direction: "horizontal",
  slidesPerView: 3.5,
  loop: true,
  navigation: {
    nextEl: ".swiper-button-next-1",
    prevEl: ".swiper-button-prev-1",
  },
});

const swiper3 = new Swiper(".mySwiper3", {
  direction: "horizontal",
  slidesPerView: 3.5,
  loop: true,

  navigation: {
    nextEl: ".swiper-button-next-2",
    prevEl: ".swiper-button-prev-2",
  },
});
