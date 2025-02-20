function copyTextToClipboard(text) {
  navigator.clipboard
    .writeText(text)
    .then(() => {
      alert("Скопировано в буфер обмена");
    })
    .catch((err) => {
      console.error("Ошибка копирования: ", err);
    });
}

//Обработчик события для всех элементов с классом 'copy-to-clipboard'
document.addEventListener("DOMContentLoaded", () => {
  const copyElements = document.querySelectorAll(".copy-to-clipboard");
  copyElements.forEach((element) => {
    element.addEventListener("click", (event) => {
      event.preventDefault();
      const textToCopy = element.getAttribute("data-copy");
      if (textToCopy) {
        copyTextToClipboard(textToCopy);
      } else {
        console.error("Атрибут 'data-copy' не найден");
      }
    });
  });
});

//Модальное окно
document.addEventListener("DOMContentLoaded", () => {
  const modal = document.querySelector(".main-modal");
  const modalClose = document.querySelector(".main-modal__close");
  const modalOpen = document.querySelector(".question__btn");

  modalOpen.addEventListener("click", () => {
    modal.classList.add("modal-open");
  });

  modalClose.addEventListener("click", () => {
    modal.classList.remove("modal-open");
  });
});

//Бургер меню
(function () {
  const burgerItem = document.querySelector(".header__burger");
  const menu = document.querySelector(".header__nav");
  const menuCloseItem = document.querySelector(".header__nav-close");
  burgerItem.addEventListener("click", () => {
    menu.classList.add("header__nav-active");
    menuCloseItem.classList.add("open-close-item");
    burgerItem.classList.add("close-burger-item");
  });

  menuCloseItem.addEventListener("click", () => {
    menu.classList.remove("header__nav-active");
    menuCloseItem.classList.remove("open-close-item");
    burgerItem.classList.remove("close-burger-item");
  });
})();

//Dropdown
function checkScreenSize() {
  var buttons = document.querySelector(".clubs__buttons");
  var dropdown = document.querySelector(".dropdown-select");
  if (window.innerWidth < 768) {
    buttons.style.display = "none";
    dropdown.style.display = "block";
  } else {
    buttons.style.display = "flex";
    dropdown.style.display = "none";
  }
}

document.addEventListener("DOMContentLoaded", () => {
  const video = document.querySelector(".project__video");
  const playButton = document.querySelector(".project__video-play-btn");
  const videoOverlay = document.querySelector(".project__video-overlay");
  const videoLink = document.querySelector(".project__video-link");

  playButton.addEventListener("click", () => {
    video.play();
    video.controls = true;
    videoOverlay.style.display = "none";
    videoLink.style.display = "none";
  });

  video.addEventListener("play", () => {
    videoLink.style.display = "none";
  });

  video.addEventListener("ended", () => {
    videoLink.style.display = "block";
  });
});
document.addEventListener("DOMContentLoaded", () => {
  const readMoreButton = document.querySelector(".project__read-more");
  const moreText = document.querySelector(".project__more-text");
  let isTextVisible = false;

  readMoreButton.addEventListener("click", () => {
    if (isTextVisible) {
      moreText.style.display = "none";
      readMoreButton.textContent = "Читать полностью";
      readMoreButton.classList.remove("expanded");
    } else {
      moreText.style.display = "inline";
      readMoreButton.textContent = "Скрыть";
      readMoreButton.classList.add("expanded");
    }
    isTextVisible = !isTextVisible;
  });
});
