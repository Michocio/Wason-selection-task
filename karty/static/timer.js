
var set_time = 310;
var real_time = 0;
var events_time = [];
var events_msg = [];
var stopped = false;

function count()
{
    setInterval(function ()
    {
        if(stopped == true)
            return;
       if(real_time >= set_time)
        {
            postMessage("timeIsUp");
            real_time = 0;
        }
        real_time+= 0.1;
        //console.log(real_time);
    },100);// Miliseconds
}

onmessage = function (oEvent) {
    var name  = oEvent.data.name;
    var obj = oEvent.data;

    if(name == "reset")
    {
        real_time  = 0;
    }
    else if(name == "stop")
    {
        stopped = true;
    }
    else if(name == "start")
    {
        set_time = Number(obj.time);
        real_time = 0;
        count();
    }
    else if(name == "event")
    {
        events_time.push(Number(obj.time));
        events_msg.push(obj.msg);
    }
    else if (obj == "ask")
    {
         postMessage(String(real_time));
    }
};