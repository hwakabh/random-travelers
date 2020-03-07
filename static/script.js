function gacha(){
    $.ajax({
      type: 'POST',
      url: '/gacha',
      data: '',
    })
    .done(function(result) {

      document.getElementById("describe").innerHTML = "";
      document.getElementById("region").innerHTML = result;

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
      document.getElementById("region").innerHTML = "fail";
    });
}

$(function () {
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
})
