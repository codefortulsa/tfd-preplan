$().ready(function() {

    elements = ['streets','satellite']
    styles = ['mapbox://styles/jdungan/cj0loh44h000n2sns2eck9rdh',
              'mapbox://styles/mapbox/satellite-streets-v9'
            ]

    idx=0


// mapbox.landsat-live

    const map = new mapboxgl.Map({
        container: elements[idx],
        style: styles[idx],
        center: property.coordinates,
        zoom: 17,
        pitch: 45
    })

    map.addControl(new mapboxgl.NavigationControl())
    map .addSource("markers", {
       "type": "geojson",
       "data": {
           "type": "FeatureCollection",
           "features": [{
               "type": "Feature",
               "geometry": {
                   "type": "Point",
                   "coordinates": property.coordinates
               },
               "properties": {
                   "title": "location",
                   "marker-symbol": "star",
               }
            }]
        }
    })

    map.addLayer({
        "id": "markers",
        "type": "symbol",
        "source": "markers",
        "layout": {
            "icon-image": "{marker-symbol}-15",
            "icon-size": 3
        }
    })

    $('a[data-toggle="pill"]').on('shown.bs.tab', function (e) {
        var target = $(e.target).attr("href") // activated tab
        for (var map in maps){
            map.resize()
        }
    });

})
