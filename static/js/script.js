function textAreaUpdate(element) {
    element.style.height = "1px";
    element.style.height = (25+element.scrollHeight)+"px";
  }

function areYouSure() {
  window.alert("This will delete your account and reviews permanently")  
}

$(document).ready(function(){
    $('.sidenav').sidenav({
        outDuration: "400",
        inDuration: "400"});
        $('.collapsible').collapsible();
  });