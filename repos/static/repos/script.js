var button = document.querySelector(".repogen");
//Refreshes The Page On Click
if (button) {
    button.onclick = refreshPage
} 
function refreshPage(){
    window.location.reload();
}