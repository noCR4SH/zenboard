window.onload = function(){
    
    g1 = new JustGage({
            id: "new_gauge",
            value: 0,
            valueFontColor: "#ffffff",
            min: 0,
            max: 20,
            donut: true,
            gaugeWidthScale: 0.3,
            counter: true,
            title: "New",
            hideInnerShadow: true,
            relativeGaugeSize: true,
        });
    g2 = new JustGage({
            id: "transferred_gauge",
            value: 0,
            valueFontColor: "#ffffff",
            min: 0,
            max: 10,
            donut: true,
            gaugeWidthScale: 0.3,
            counter: true,
            title: "Transferred",
            hideInnerShadow: true,
            relativeGaugeSize: true,
        });
    g3 = new JustGage({
            id: "platinum_gauge",
            value: 0,
            valueFontColor: "#ffffff",
            min: 0,
            max: 5,
            donut: true,
            gaugeWidthScale: 0.3,
            counter: true,
            title: "Platinum",
            hideInnerShadow: true,
            relativeGaugeSize: true,
        });
    g4 = new JustGage({
            id: "premium_gauge",
            value: 0,
            valueFontColor: "#ffffff",
            min: 0,
            max: 10,
            donut: true,
            gaugeWidthScale: 0.3,
            counter: true,
            title: "Premium",
            hideInnerShadow: true,
            relativeGaugeSize: true,
        });
};

function unassignedList(list) {
    var ticketList = list;

    var getTable = document.getElementById('ticket-table-list');

    while(getTable.hasChildNodes()) {
        getTable.removeChild(getTable.firstChild);
    }

    var numberOfListItems = ticketList.length;

    for(var i = 0; i < numberOfListItems; i++) {
        if (i === 7) {
            break;
        }

        var trElement = document.createElement('tr');

        document.getElementById('ticket-table-list').appendChild(trElement);

        for(var n = 0; n < ticketList[i].length; n++){
            var tdItem = document.createElement('td');

            tdItem.innerHTML = ticketList[i][n];

            trElement.appendChild(tdItem);
        }
    }
}

function notAnsweredList(list) {
    var ticketList = list;

    var getTable = document.getElementById('na-ticket-table-list');

    while(getTable.hasChildNodes()) {
        getTable.removeChild(getTable.firstChild);
    }

    var numberOfListItems = ticketList.length;

    for(var i = 0; i < numberOfListItems; i++) {
        if (i === 14) {
            break;
        }

        var trElement = document.createElement('tr');

        document.getElementById('na-ticket-table-list').appendChild(trElement);

        for(var n = 0; n < ticketList[i].length; n++){
            var tdItem = document.createElement('td');
            // tdItem.className = "td-na";

            tdItem.innerHTML = ticketList[i][n];

            trElement.appendChild(tdItem);
        }
    }
}

var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');
var numbers_received = [];

socket.on('newstatus', function(msg) {

    g1.refresh(msg.un_ticket_count);
    g2.refresh(msg.trans_count);
    g3.refresh(msg.un_platinum_count);
    g4.refresh(msg.un_premium_count);

    //Pickup Rate
    document.getElementById("bart_pickup").innerHTML = msg.taken_list[1];
    document.getElementById("harsh_pickup").innerHTML = msg.taken_list[2];
    document.getElementById("woj_pickup").innerHTML = msg.taken_list[3];
    document.getElementById("jak_pickup").innerHTML = msg.taken_list[4];

    //Closure Rate
    // document.getElementById("mat_closure").innerHTML = msg.solved_list[0];
    // document.getElementById("bart_closure").innerHTML = msg.solved_list[1];
    // document.getElementById("harsh_closure").innerHTML = msg.solved_list[2];
    // document.getElementById("woj_closure").innerHTML = msg.solved_list[3];
    // document.getElementById("jak_closure").innerHTML = msg.solved_list[4];

    unassignedList(msg.un_list);
    notAnsweredList(msg.not_answered_list);
    console.log("Not answered ticket list " + msg.not_answered_list + ", Var type: " + typeof(msg.not_answered_list));
});


//////////////////////////////////////////////////////////////
// Clock 

function dateToText(date) {
    var hours = date.getHours()
    var minutes = date.getMinutes();
    // var seconds = date.getSeconds();
    if (minutes < 10) minutes = '0'+minutes;
    //if  seconds < 10) seconds = '0'+seconds;
    if (hours < 10) hours = '0'+hours;
    return hours + ":" + minutes; // + ":" + seconds;
}
function updateClocks() {
	for (var i = 0; i < window.arrClocks.length; i++) {
		var clock = window.arrClocks[i];
		var offset = window.arrOffsets[i];
		clock.innerHTML = dateToText(new Date(new Date().getTime()+offset));
	}
}
function startClocks() {
	clockElements = document.getElementsByClassName('clock');
	window.arrClocks = []
	window.arrOffsets = [];
	var j = 0;
	for(var i = 0; i < clockElements.length; i++) {
		el = clockElements[i];
		timezone = parseInt(el.getAttribute('timezone'));
		if (!isNaN(timezone)) {
			var tzDifference = timezone * 60 + (new Date()).getTimezoneOffset();
			var offset = tzDifference * 60 * 1000;
			window.arrClocks.push(el);
			window.arrOffsets.push(offset);
		}
	}
	updateClocks();
	clockID = setInterval(updateClocks, 1000);
}
setTimeout(startClocks, 100);