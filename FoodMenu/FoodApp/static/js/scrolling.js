// Scroll Effect when a url targeting id in the page is clicked
let anchor_tags = document.querySelectorAll('a[href^="#"]');
anchor_tags.forEach((link) => {
  link.onclick = function (e) {
    e.preventDefault();
    let destination = document.querySelector(this.hash);
    destination.scrollIntoView({
      behavior: "smooth",
    });
  };
});
