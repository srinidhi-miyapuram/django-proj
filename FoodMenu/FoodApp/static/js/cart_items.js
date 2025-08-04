const url_items = "http://127.0.0.1:8000/cart";

if (localStorage.getItem("cart") != undefined) {
  cart = JSON.parse(localStorage.getItem("cart"));
} else {
  var cart = {};
}
$(document).on("click", ".add_btn", function () {
  var item_id = this.id;
  if (cart[item_id] != undefined) {
    cart[item_id] += 1;
  } else {
    cart[item_id] = 1;
  }
  localStorage.setItem("cart", JSON.stringify(cart));
  show_cart();
});

function show_cart() {
  // const my_data = JSON.parse(document.getElementById("my-data").textContent);
  let cart_item = JSON.parse(localStorage.getItem("cart"));
  const csrf_token = document.querySelector(
    'input[name="csrfmiddlewaretoken"]'
  ).value;
  fetch(url_items, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      X_CSRF_TOKEN: csrf_token,
    },
    body: JSON.stringify(cart_item),
  });
}
