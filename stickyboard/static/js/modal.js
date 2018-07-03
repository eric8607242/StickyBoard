/* create-modal stuff */

var create_modal = document.getElementById('createBoard');
var create_btn = document.getElementById("create-btn");
var create_span = document.getElementsByClassName("close")[0];
var create_cancel = document.getElementsByClassName("cancel-btn")[0];

create_btn.onclick = function() {
    create_modal.style.display = "block";
}

create_span.onclick = function() {
    create_modal.style.display = "none";
}

create_cancel.onclick = function() {
    create_modal.style.display = "none";
}

/* delete-modal stuff */

var delete_modal = document.getElementById('deleteBoard');
var delete_btn = document.getElementById("delete-btn");
var delete_span = document.getElementsByClassName("close")[1];
var delete_cancel = document.getElementsByClassName("cancel-btn")[1];

delete_btn.onclick = function() {
    delete_modal.style.display = "block";
}

delete_span.onclick = function() {
    delete_modal.style.display = "none";
}

delete_cancel.onclick = function() {
    delete_modal.style.display = "none";
}

/* invite-modal stuff */

var invite_modal = document.getElementById('invite');
var invite_btn = document.getElementById("invite-btn");
var invite_span = document.getElementsByClassName("close")[2];
var invite_cancel = document.getElementsByClassName("cancel-btn")[2];

invite_btn.onclick = function() {
    invite_modal.style.display = "block";
}

invite_span.onclick = function() {
    invite_modal.style.display = "none";
}

invite_cancel.onclick = function() {
    invite_modal.style.display = "none";
}

window.onclick = function(event) {
    if (event.target == delete_modal || event.target == create_modal || event.target == invite_modal) {
        create_modal.style.display = "none";
        delete_modal.style.display = "none";
        invite_modal.style.display = "none";
    }
}
