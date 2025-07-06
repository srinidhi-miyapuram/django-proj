// Splitting the words in label text to array of elements placed in span tag
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

// Redirect to items page when we click let's buy button in home page
function redirect() {
  let curr_url = window.location.href;
  window.location.replace(`${curr_url}/items`);
}

// Pop up window with item details
var popup_elem = document.getElementById("popup");
var item_body = document.getElementById("item-body");

function popup(name, desc, img_name, price, rating) {
  popup_elem.innerHTML = `<img src="media/${img_name}" alt="${desc}" />
  <div class="item-block">
  
  <h2 class="item-detail">${name}</h2>
  <p class="item-detail">${desc}</p>
  <div class="item-price">
    <h3 class="item-detail">Price: ${price}</h3>
    <h4 class="item-detail">Rating: ${rating}</h4>
  </div>
        <div class="links">
        <a
          href="#"
          onclick="restore()"
          >Close</a
        >
        <a href="#">Add</a>
      </div>
  </div>`;
  popup_elem.style.visibility = "visible";
  item_body.style.opacity = "0.3";
}

function restore() {
  popup_elem.style.visibility = "hidden";
  item_body.style.opacity = "1";
}
