$('.links a').click(function(event) {
    $('.links a').removeClass('active');
    $(this).addClass('active');
});

$(document).ready(function() {
    // Get current page URL and extract the page name
    var url = window.location.pathname;
    var pageName = url.substring(url.lastIndexOf('/') + 1);

    // Check if the current page is index1.html
    if (pageName === "index1.html") {
        $('#link1').css('background-color', 'blue');
    }
    if (pageName === "index2.html") {
        $('#link2').css('background-color', 'blue');
        $('#link2_2').css('background-color', 'blue');
    }
    if (pageName === "index3.html") {
        $('#link3').css('background-color', 'blue');
    }
});