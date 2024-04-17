<template>

  <div id="mapid" class="absolute"></div>
  <q-btn id="pause"/>
</template>

<script>
  import maplibregl from 'maplibre-gl';
  import {onMounted} from "vue";

  import 'maplibre-gl/dist/maplibre-gl.css';
  import turf from 'turf';


  export default {
    name: "demo_4",
    setup() {

      var map = null;
      const initMap = () => {

        map = new maplibregl.Map({
          container: 'mapid',

          style: './data/style.json',
          center: [-96, 37.8],
          zoom: 3

        });
// San Francisco
        const origin = [-122.414, 37.776];

        // Washington DC
        const destination = [-77.032, 38.913];

        // A simple line from origin to destination.
        const route = {
          'type': 'FeatureCollection',
          'features': [
            {
              'type': 'Feature',
              'geometry': {
                'type': 'LineString',
                'coordinates': [origin, destination]
              }
            }
          ]
        };

        // A single point that animates along the route.
        // Coordinates are initially set to origin.
        const point = {
          'type': 'FeatureCollection',
          'features': [
            {
              'type': 'Feature',
              'properties': {},
              'geometry': {
                'type': 'Point',
                'coordinates': origin
              }
            }
          ]
        };

        // Calculate the distance in kilometers between route start/end point.
        const lineDistance = turf.lineDistance(route.features[0], 'kilometers');

        const arc = [];

        // Number of steps to use in the arc and animation, more steps means
        // a smoother arc and animation, but too many steps will result in a
        // low frame rate
        const steps = 500;

        // Draw an arc between the `origin` & `destination` of the two points
        for (let i = 0; i < lineDistance; i += lineDistance / steps) {
          const segment = turf.along(route.features[0], i, 'kilometers');
          arc.push(segment.geometry.coordinates);
        }

        // Update the route with calculated arc coordinates
        route.features[0].geometry.coordinates = arc;

        // Used to increment the value of the point measurement against the route.
        let counter = 0;

        map.on('load', () => {
          // Add a source and layer displaying a point which will be animated in a circle.
          map.addSource('route', {
            'type': 'geojson',
            'data': route
          });

          map.addSource('point', {
            'type': 'geojson',
            'data': point
          });

          map.addLayer({
            'id': 'route',
            'source': 'route',
            'type': 'line',
            'paint': {
              'line-width': 2,
              'line-color': '#007cbf'
            }
          });

          map.loadImage(
            'data/飞机.png',
            function (error, image) {
              if (error) throw error;
              //添加图片到map上
              map.addImage('newplane', image); //参数一位名称，参数二位加载的图片

          map.addLayer({
            'id': 'point',
            'source': 'point',
            'type': 'symbol',
            'layout': {
              'icon-image': 'newplane',
              'icon-rotate': ['get', 'bearing'],
              'icon-rotation-alignment': 'map',
              'icon-overlap': 'always',
              'icon-ignore-placement': true
            }
          });
            }
          )


          function animate() {
            // Update point geometry to a new position based on counter denoting
            // the index to access the arc.
            point.features[0].geometry.coordinates =
              route.features[0].geometry.coordinates[counter];

            // Calculate the bearing to ensure the icon is rotated to match the route arc
            // The bearing is calculate between the current point and the next point, except
            // at the end of the arc use the previous point and the current point
            point.features[0].properties.bearing = turf.bearing(
              turf.point(
                route.features[0].geometry.coordinates[
                  counter >= steps ? counter - 1 : counter
                  ]
              ),
              turf.point(
                route.features[0].geometry.coordinates[
                  counter >= steps ? counter : counter + 1
                  ]
              )
            );

            // Update the source with this new data.
            map.getSource('point').setData(point);

            // Request the next frame of animation so long the end has not been reached.
            if (counter < steps) {
              requestAnimationFrame(animate);
            }

            counter = counter + 1;
          }

          document
            .getElementById('pause')
            .addEventListener('click', () => {
              // Set the coordinates of the original point back to origin
              point.features[0].geometry.coordinates = origin;

              // Update the source layer
              map.getSource('point').setData(point);

              // Reset the counter
              counter = 0;

              // Restart the animation.
              animate(counter);
            });

          // Start the animation.
          animate(counter);
        });
      }
      onMounted(() => {
        initMap()

      })


      return {}
    }
  }
</script>

<style scoped>
  #mapid {
    top: 10vh;
    right: 10px;
    height: 70vh;
    width: 60vw
  }

  #pause {
    position: absolute;
    top: 20vh;
    right: 10vw;
    margin: 20px;
  }

  #pause::after {
    content: 'Pause';
  }

  #pause.pause::after {
    content: 'Play';
  }


</style>
