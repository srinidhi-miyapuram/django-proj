var labels = document.querySelectorAll(".form-label");
labels.forEach((label) => {
  label.innerHTML = label.innerText
    .split("")
    .map(
      (letter, idx) =>
        `<span style="transition-delay:${idx * 50}ms">${letter}</span>`
    )
    .join("");
});

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
