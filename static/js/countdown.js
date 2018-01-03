var doClock = (function () {
    var serverOffset = unixCountdown - (new Date() / 1000 | 0);
    return function () {
        var currentTime = new Date(unixCountdown*1000);
        var hours = currentTime.getHours();
        var minutes = "0" + currentTime.getMinutes();
        var seconds = "0" + currentTime.getSeconds();
        var formattedTime = hours + ':' + minutes.substr(-2) + ':' + seconds.substr(-2);
        unixCountdown++;
        var now = new Date();
        now.setSeconds(now.getSeconds() + serverOffset);
        document.getElementById('countdown').innerHTML = formattedTime;
        setTimeout(doClock, 1020 - now.getMilliseconds());
    };
}());
window.onload = doClock;