"use strict";


// PART 1: SHOW A FORTUNE
// event handler for generating random fortune
function showFortune(evt) {

    // TODO: get the fortune and show it in the #fortune-text div
    var fortune = evt;
    $('#fortune-text').html(fortune);
}

function getFortune() {
	$.get('/fortune', showFortune);
}

$('#get-fortune-button').on('click', getFortune);





// PART 2: SHOW WEATHER

function showWeather(evt) {
    evt.preventDefault();

    var url = "/weather.json?zipcode=" + $("#zipcode-field").val();

    // TODO: request weather with that URL and show the forecast in #weather-info
    $.get("/weather.json?zipcode=", $("#zipcode-field").val());
 	//    if ($("#zipcode-field").val() in WEATHER){
	// 	console.log("The weather for " + WEATHER);
	// }
	// else {
	// 	console.log("The weather for " + DEFAULT_WEATHER);
	// }
    $("#weather-form").html(evt);
}
$("#weather-form").on('submit', showWeather);




// PART 3: ORDER MELONS

function orderMelons(evt) {
    evt.preventDefault();

    // TODO: show the result message after your form
    // TODO: if the result code is ERROR, make it show up in red (see our CSS!)
}

$("#order-form").on('submit', orderMelons);


