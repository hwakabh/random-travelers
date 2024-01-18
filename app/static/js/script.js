
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

  document.getElementById("title").style.display = "none";
  document.getElementById("describe").style.display = "none";
  document.getElementById("country").style.display = "inline-block";
  document.getElementById("country-ja").style.display = "inline-block";
  document.getElementById("country").innerHTML = "";
  document.getElementById("country-ja").innerHTML = "";

  $.ajax({
    type: 'POST',
    url: '/api/v1/shuffle',
    data: '',
  })
  .done(function(result) {

    // Output the result of selecting a country at random.
    var output = result;
    document.getElementById("country").innerHTML = output;

    var xhr = new XMLHttpRequest();
    // TODO: need to updated with another way
    xhr.open('GET','https://script.google.com/macros/s/AKfycbw64MMQ9W8oyCPGvDxRvTg4VActbv2ww8XC0wuv62VXMriCVtY/exec?text=' + result + '&source=en&target=ja');
    xhr.send();
    xhr.onreadystatechange = function() {
      if(xhr.readyState === 4 && xhr.status === 200) {
        //console.log(xhr.responseText);
        var data = JSON.parse(xhr.responseText);
        document.getElementById("country-ja").innerHTML = " " + data.text;
      }
    }

    // Display the location of the selected country on a google map.
    var geocoder = new google.maps.Geocoder();

    geocoder.geocode({
      address: result
    }, function(results, status) {
      if (status == google.maps.GeocoderStatus.OK) {

        var bounds = new google.maps.LatLngBounds();

        for (var i in results) {
          if (results[0].geometry) {
            var latlng = results[0].geometry.location;
            var address = results[0].formatted_address;
            var mapOptions = {
              zoom : 3,
              center : latlng
            };
            var map = new google.maps.Map(
              document.getElementById("map"),
              mapOptions
            );
            var marker = new google.maps.Marker({
              map : map,
              position : latlng
            });
          }
        }
      } else if (status == google.maps.GeocoderStatus.ZERO_RESULTS) {
        alert("not found.");
      } else {
        console.log(status);
        alert("error.");
      }
    });
  })
  .fail(function(){
    document.getElementById("country").innerHTML = "fail";
  });
}

