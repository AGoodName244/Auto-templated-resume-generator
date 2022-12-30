function form_input_func() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    var form_button = document.getElementById("form-button");
    if (username != "" && password != "") {
        form_button.style.backgroundColor = "rgb(7, 24, 196)";
    }
    else {
        form_button.style.backgroundColor = "";
    }
}

function form_submit_func(event) {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    if (username == "" || password == "") {
        event.preventDefault()
    }
}