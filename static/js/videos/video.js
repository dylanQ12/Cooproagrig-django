var modal = document.getElementById("myModal");
var btn = document.getElementById("playButton");
var span = document.getElementsByClassName("close")[0];
var iframe = document.getElementById("youtubeVideo");

btn.onclick = function() {
    modal.style.display = "flex";
    iframe.src = "https://www.youtube.com/embed/LiicQoWogbg";
}

span.onclick = function() {
    modal.style.display = "none";
    iframe.src = "";
}

window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
        iframe.src = "";
    }
}