function center() {
    var h = $( "#center" ).css("height").replace(/[^-\d\.]/g, '');;
    var w = $( "#center" ).css("width").replace(/[^-\d\.]/g, '');;
    $( "#center" ).css("position","absolute");

    $( "#center" ).css("top", (($(window).height() - h) /2));
    $( "#center" ).css("left", (($(window).width() - w) /2));
}
function center_div() {
    $(document).ready(function () {
        center();
        $(window).resize(function () {
            center();
        });
    });
}

