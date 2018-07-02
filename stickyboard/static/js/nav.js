function responsive_nav() {
    let x = document.getElementById("myTopnav");
    let down_icon = document.getElementsByClassName('slide-down')[0];
    if (x.className === "topnav") {
        x.className += " responsive";
        down_icon.style.display = "none";
    } else {
        x.className = "topnav";
        down_icon.style.display = "block";
    }
}