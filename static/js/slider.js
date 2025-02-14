const swiper = new Swiper(".swiper", {
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
  // loop: true,
  // loopedSlides: 3,
  // autoplay: {
  //   delay: 3000,
  //   disableOnInteraction: false,
  // },
  slideToClickedSlide: true,
  simulateTouch: true,
});
