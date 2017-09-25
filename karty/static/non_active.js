var prev = 0;
var now = 0;
function activity_detect(time) {

    now = Number(time);

    if (now - prev > limit)
    {
        prev = now;
        return false;
    }
    prev = now;
    return true;
}