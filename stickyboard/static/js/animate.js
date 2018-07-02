var str = 'Sticky Board - The best reminder in your life.';
var i = 0;

function typing() {
    var divTyping = document.getElementById('hero-text');
    if (i <= str.length) {
        divTyping.innerHTML = str.slice(0, i++) + '|';
        setTimeout('typing()', 80);
    } else {
        divTyping.innerHTML = str;
    }
}

typing();