/* create-modal stuff */

var create_modal = document.getElementById('createBoard');
var create_btn = document.getElementById("create-btn");
var create_span = document.getElementsByClassName("close")[0];

create_btn.onclick = function() {
    create_modal.style.display = "block";
}

create_span.onclick = function() {
    create_modal.style.display = "none";
}

window.onclick = function(event) {
    if (event.target == create_modal) {
        create_modal.style.display = "none";
    }
}

/* delete-modal stuff */

var delete_modal = document.getElementById('deleteBoard');
var delete_btn = document.getElementById("delete-btn");
var delete_span = document.getElementsByClassName("close")[1];

delete_btn.onclick = function() {
    delete_modal.style.display = "block";
}

delete_span.onclick = function() {
    delete_modal.style.display = "none";
}

window.onclick = function(event) {
    if (event.target == delete_modal) {
        delete_modal.style.display = "none";
    }
}

/* invite-modal stuff */

var invite_modal = document.getElementById('invite');
var invite_btn = document.getElementById("invite-btn");
var invite_span = document.getElementsByClassName("close")[2];

invite_btn.onclick = function() {
    invite_modal.style.display = "block";
}

invite_span.onclick = function() {
    invite_modal.style.display = "none";
}

window.onclick = function(event) {
    if (event.target == invite_modal) {
        invite_modal.style.display = "none";
    }
}
