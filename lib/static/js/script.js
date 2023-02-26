function textAreaUpdate(element) {
    element.style.height = "1px";
    element.style.height = (25+element.scrollHeight)+"px";
  }

$( ".dropdwn-btn" ).click(function() {
    const btnArrow = $(this).children('i')[0]
    if ($(this).children('p')[0].textContent === "Read") {
        $(this).removeClass('dropdwn-btn-read').addClass('dropdwn-btn-close')
        $(this).children('p')[0].textContent = "Close"
        $(btnArrow).removeClass('fa-chevron-down');
        $(btnArrow).addClass('fa-chevron-up');
    } else {
        $(this).removeClass('dropdwn-btn-close').addClass('dropdwn-btn-read')
        $(this).children('p')[0].textContent = "Read"
        $(btnArrow).removeClass('fa-chevron-up');
        $(btnArrow).addClass('fa-chevron-down');
    }
});


$(document).ready(function(){
    $('.sidenav').sidenav({
        outDuration: "400",
        inDuration: "400"});
        $('.collapsible').collapsible();
  });

