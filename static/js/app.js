const hamburgerButton = document.getElementById("hamburger");
const navMenu = document.getElementById("nav-menu");
const hamburgerIcon = document.getElementById("hamburger-icon");
const closeIcon = document.getElementById("close-icon");

hamburgerButton.addEventListener("click", () => {
  // Toggle the visibility of the menu
  navMenu.classList.toggle("hidden");

  // Toggle between hamburger and close icons
  hamburgerIcon.classList.toggle("hidden");
  closeIcon.classList.toggle("hidden");
});
