window.onload = async function() {
  const res = await fetch("/api/v1/fetch");
  const src = await res.text();
  const script = document.createElement("script");
  script.textContent = src;
  document.body.appendChild(script);
  initMap();

  // Search the current location and display it on google map.
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(
      function(position) {
        // Set current latitude/longitude to sessionStorage by Location Service
        sessionStorage.setItem("latitude", position.coords.latitude);
        sessionStorage.setItem("longitude", position.coords.longitude);

        var mapLatLng = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);
        var mapOptions = {
          zoom : 3,
          center : mapLatLng
        };
        var map = new google.maps.Map(
          document.getElementById("map"),
          mapOptions
        );
        var marker = new google.maps.Marker({
          map : map,
          position : mapLatLng
        });
      },
      function(error) {
        switch(error.code) {
          case 1:
            alert("permission denied.");
            break;
          case 2:
            alert("position unavailable.");
            break;
          case 3:
            alert("timeout.");
            break;
          default:
            alert("error(error code:"+error.code+")");
            break;
        }
      }
    );
  } else {
    alert("Location information is not available on this device.");
  }

}


function initMap() {
  var uluru = {lat: -25.344, lng: 131.036};
  var map = new google.maps.Map(document.getElementById('map'), {zoom: 4, center: uluru});
  var marker = new google.maps.Marker({position: uluru, map: map});
}


function executeShuffle(){

  // Hide default elements and inject result of random choice
  document.getElementById("title").style.display = "none";
  document.getElementById("describe").style.display = "none";
  document.getElementById("country").style.display = "inline-block";
  document.getElementById("country-ja").style.display = "inline-block";
  document.getElementById("country").innerHTML = "";
  document.getElementById("country-ja").innerHTML = "";

  //--- get user input parameter
  var time_limit = document.getElementById("time").value;
  var expense_limit = document.getElementById("amount").value;
  console.log("time_limit: " + time_limit + " hour");
  console.log("expense_limit: " + expense_limit + " $");

  //--- get sessionStorage
  var current_lat = sessionStorage.getItem('latitude');
  var current_lng = sessionStorage.getItem('longitude');

  document.getElementById("city").style.display = "none";
  document.getElementById("search").style.display = "inline-block";
  document.getElementById("detail").style.display = "none";

  document.getElementById("search").innerHTML = "Search...";

  $('#submit').toggleClass('d-none').toggleClass('d-inline-block');
  $('#load').toggleClass('d-none').toggleClass('d-inline-block');


  $.ajax({
    type: 'POST',
    url: '/api/v1/shuffle',
    contentType:'application/json',
    data: JSON.stringify({
      "time_limit":time_limit,
      "expense_limit":expense_limit,
      "current_lat":current_lat,
      "current_lng":current_lng
    })
  })
  .done(function(result) {
    console.log(result);

    //--- display the location of random selected country on a google map.
    var current_LatLng = new google.maps.LatLng(current_lat, current_lng);
    var transit_LatLng = new google.maps.LatLng(result["tran_lat"], result["tran_lng"]);
    var destination_LatLng = new google.maps.LatLng(result["dest_lat"], result["dest_lng"]);

    console.log("current: " + "[latlng]" + current_LatLng);
    console.log("transit: " + "[country]" + result["tran_country"] + " [airport]" + result["tran_airport"] + " [latlng]" + transit_LatLng);
    console.log("destination: " + "[country]" + result["dest_country"] + " [airport]" + result["dest_airport"] + " [latlng]" + destination_LatLng);

    //var bounds = new google.maps.LatLngBounds();

    var mapOptions = {
      zoom: 3,
      center: destination_LatLng
    };

    var map = new google.maps.Map(document.getElementById("map"),mapOptions);
    var marker = new google.maps.Marker({
      map : map,
      position : current_LatLng
    });
    //bounds.extend (marker.position);
    var marker = new google.maps.Marker({
      map : map,
      position : transit_LatLng
    });
    //bounds.extend (marker.position);
    var marker = new google.maps.Marker({
      map : map,
      position : destination_LatLng
    });
    //bounds.extend (marker.position);
    var flightPath = new google.maps.Polyline({
      path: [
        current_LatLng,
        transit_LatLng,
        destination_LatLng
      ],
      geodesic: true,
      strokeColor: '#ff0000',
      strokeOpacity: 1.0,
      strokeWeight: 2
    });
    flightPath.setMap(map);
    //map.fitBounds (bounds);


    //--- output the result of random selected country to pallet
    document.getElementById("country").style.display = "inline-block";
    document.getElementById("city").style.display = "inline-block";
    document.getElementById("search").style.display = "none";
    document.getElementById("detail").style.display = "inline-block";

    document.getElementById("country").innerHTML = result["dest_country"];
    document.getElementById("city").innerHTML = ' <span class="badge badge-light">City</span> ' + result["dest_city"];
    $('#collapseOne').removeClass('collapse show');
    $('#collapseOne').addClass('collapse');
    $("#detail-item").empty();
    $("#detail-item").append('<li class="list-group-item"><h5><span class="badge badge-light">your location</span></h5> ' + current_LatLng + '</li>');
    $("#detail-item").append('<li class="list-group-item"><h5><span class="badge badge-light">origin</span></h5> ' + 'Country: ' + result["tran_country"] + '<br>City: ' + result["tran_city"] + '<br>Airport: ' + '[' + result["tran_iata"] + '] ' + result["tran_airport"] + '<br>Departure time: XX:XX' + '</li>');
    $("#detail-item").append('<li class="list-group-item"><h5><span class="badge badge-light">destination</span></h5> ' + 'Country: ' + result["dest_country"] + '<br>City: ' + result["dest_city"] + '<br>Airport: ' + '[' + result["dest_iata"] + '] ' +  result["dest_airport"] + '<br>Arrival time : XX:XX' + '</li>');
    $("#detail-item").append('<li class="list-group-item" style="color:dodgerblue;"><b><h5><span class="badge badge-light">travel hour</span></h5> ' + 'XXXXXX Hour' + '</b></li>');
    $("#detail-item").append('<li class="list-group-item" style="color:dodgerblue;"><b><h5><span class="badge badge-light">travel expense</span></h5> ' + 'XXXXXX USD' + '</b></li>');

    $('#submit').toggleClass('d-none').toggleClass('d-inline-block');
    $('#load').toggleClass('d-none').toggleClass('d-inline-block');


    const xhr = new XMLHttpRequest();
    const url = '/api/v1/translate';
    xhr.open('POST', url, true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.send(JSON.stringify({
      "country": result["dest_country"]
    }));

    xhr.onreadystatechange = function() {
      if (xhr.readyState === 4 && xhr.status === 200) {
        const countryTranslated = JSON.parse(xhr.responseText);
        document.getElementById("country-ja").style.display = "inline-block";
        document.getElementById("country-ja").innerHTML = ' ' + countryTranslated;
      }
    }
  })
  .fail(function() {
    document.getElementById("country").innerHTML = "fail";
    $('#submit').toggleClass('d-none').toggleClass('d-inline-block');
    $('#load').toggleClass('d-none').toggleClass('d-inline-block');
  });
}
