function getSecondsSinceStartOfDay() {
    return new Date().getSeconds() + 
        new Date().getMinutes() * 60 + 
        new Date().getHours() * 3600;
}

setInterval(function() {
    var time = getSecondsSinceStartOfDay();
    var seconds = time % 60;
    var minutes = Math.floor((time / 60) % 60);
    var hours = Math.floor((time / 3600) % 12); // 12-hour format

    // Calculate the angles for each hand
    var secondsAngle = seconds * 6; // 360 / 60
    var minutesAngle = minutes * 6 + seconds / 10; // 360 / 60
    var hoursAngle = (hours * 30) + (minutes / 2); // 360 / 12

    // Rotate the hands
    document.querySelector('.seconds').style.transform = 'rotate(' + (90 + secondsAngle) + 'deg)';
    document.querySelector('.minutes').style.transform = 'rotate(' + (90 + minutesAngle) + 'deg)';
    document.querySelector('.hour').style.transform = 'rotate(' + (90 + hoursAngle) + 'deg)';
}, 1000);