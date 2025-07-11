var register_form = document.querySelector(".register-form").children;

for (let i = 0; i < register_form.length; i++) {
  if (register_form[i].tagName == "DIV") {
    register_form[i].classList.add("form-data");
    let label = register_form[i].children[0].classList.add("form-label");
  }
}
