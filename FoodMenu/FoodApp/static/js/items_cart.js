if (localStorage.getItem("cart") != undefined) {
  cart = JSON.parse(localStorage.getItem("cart"));
} else {
  var cart = {};
}
$(document).on("click", ".add_btn", function () {
  var item_id = this.id;
  if (cart[item_id] != undefined) {
    cart[item_id] += 1;
    show_cart();
  } else {
    cart[item_id] = 1;
  }
  localStorage.setItem("cart", JSON.stringify(cart));
});
