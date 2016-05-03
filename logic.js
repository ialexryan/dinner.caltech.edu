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
	    dayText = "Weekend";
	    label.textContent += "It's the weekend. New menus coming soon.";
      var fullweek = document.getElementById("fullweek");
      fullweek.parentNode.removeChild(fullweek);
}

menu.style.backgroundImage = "url('" + dayText + ".png')";

if (dayText != "Weekend") {
  label.textContent += dayText + "'s menu:";
}
