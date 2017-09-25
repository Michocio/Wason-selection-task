
$( document ).contextmenu(function (e) {
    e.preventDefault();
    if(e.target.tagName.search('BUTTON') == -1 && opis == false) {
        activity_timer.postMessage({"name": "reset"});
        timer.postMessage("ask");
    }
});

function time_of_clik(event, yes) {

    times.push(Number(event.data));
    var x = check_rythm(Number(event.data), yes);
    if(x)
        $('body').css("background-color", "green");
    else
        $('body').css("background-color", "white");
    if (!x)
        $('body').css("background-color", "white");
}