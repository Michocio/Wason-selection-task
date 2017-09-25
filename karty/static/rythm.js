var click_times = [];

function check_rythm(time, yes) {
    console.log("DFSDS");
    console.log(yes);
    if(yes == false)
        return false;

    time *= 1000;

    if (click_times.length < 4) {
        click_times.push(time);
    }
    else
    {
         for(var i = 1; i < 4; i++)
            click_times[i-1] = click_times[i];
         click_times[3] = time;
    }
    if(click_times.length >= 4)
    {
        var X = 0;
        for(var i = 1; i < 4; i++)
            X+= 1/3 * (click_times[i] - click_times[i-1]);
        var Q = 0;
        for(var i = 1; i < 4; i++)
            Q += Math.pow((click_times[i] - click_times[i-1]) - X, 2);
        //console.log(Q);
        if(Q < 10000)
            return true
    }
    return false;
}

