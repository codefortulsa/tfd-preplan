var map;

function initMap() {

    coordinates = JSON.parse($("#coordinates").val())
    address = $("#address").val()

    center = {lng:coordinates[0], lat:coordinates[1]}

    map = new google.maps.Map(document.getElementById('map'), {
        center: center,
        zoom: 20,
        mapTypeId: 'satellite',
        heading: 90,
        tilt: 45
    });

    var marker = new google.maps.Marker({
      position: center,
      map: map,
      title: address
    });

}

function rotate90() {
  var heading = map.getHeading() || 0;
  map.setHeading(heading + 90);
}

$('a[data-toggle="pill"]').on('shown.bs.tab', function (e) {
    google.maps.event.trigger(map, "resize");
});
