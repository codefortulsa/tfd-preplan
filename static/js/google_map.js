var map;

function initMap() {
    debugger

    coordinates = JSON.parse($("#coordinates").val())
    center = {lng:coordinates[0], lat:coordinates[1]}

    map = new google.maps.Map(document.getElementById('map'), {
        center: center,
        zoom: 18,
        mapTypeId: 'satellite',
        heading: 90,
        tilt: 45
    });
}

function rotate90() {
  var heading = map.getHeading() || 0;
  map.setHeading(heading + 90);
}

$('a[data-toggle="pill"]').on('shown.bs.tab', function (e) {
    google.maps.event.trigger(map, "resize");
});
