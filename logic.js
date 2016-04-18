var current = new Date();
var day = current.getDay();
if (current.getHours() >= 20) {
	// After 8pm, show tomorrow's menu
	day += 1;
}

var label = document.getElementById("label");
var menu = document.getElementById("menu");

var dayText = "";

switch(day) {
	case 1:
	    dayText = "Monday";
	    break;
	case 2:
	    dayText = "Tuesday";
	    break;
	case 3:
	    dayText = "Wednesday";
	    break;
	case 4:
	    dayText = "Thursday";
	    break;
	case 5:
	    dayText = "Friday";
	    break;
	default:
	    dayText = "Monday";
	    document.getElementById("error").textContent = "It's the weekend.";
}

menu.src = dayText + ".png";
label.textContent = "Here's " + dayText + "'s dinner menu:";
