<template>

  <div id="mapid" class="absolute"></div>

<pre id="coordinates" class="coordinates"></pre>
</template>

<script>
  import maplibregl from 'maplibre-gl';
  import {onMounted} from "vue";

  import 'maplibre-gl/dist/maplibre-gl.css';

  export default {
    name: "demo_6",
    setup() {

      var map = null;
      const initMap = () => {

        map = new maplibregl.Map({
          container: 'mapid',

          style: './data/style.json',
          center: [0, 0], // 地图初始中心点
          zoom: 3 // 地图初始缩放级别
        });

        const size = 200;

        // implementation of StyleImageInterface to draw a pulsing dot icon on the map
        // Search for StyleImageInterface in https://maplibre.org/maplibre-gl-js/docs/API/
        const pulsingDot = {
          width: size,
          height: size,
          data: new Uint8Array(size * size * 4),

          // get rendering context for the map canvas when layer is added to the map
          onAdd() {
            const canvas = document.createElement('canvas');
            canvas.width = this.width;
            canvas.height = this.height;
            this.context = canvas.getContext('2d');
          },

          // called once before every frame where the icon will be used
          render() {
            const duration = 1000;
            const t = (performance.now() % duration) / duration;

            const radius = (size / 2) * 0.3;
            const outerRadius = (size / 2) * 0.7 * t + radius;
            const context = this.context;

            // draw outer circle
            context.clearRect(0, 0, this.width, this.height);
            context.beginPath();
            context.arc(
              this.width / 2,
              this.height / 2,
              outerRadius,
              0,
              Math.PI * 2
            );
            context.fillStyle = `rgba(255, 200, 200,${1 - t})`;
            context.fill();

            // draw inner circle
            context.beginPath();
            context.arc(
              this.width / 2,
              this.height / 2,
              radius,
              0,
              Math.PI * 2
            );
            context.fillStyle = 'rgba(255, 100, 100, 1)';
            context.strokeStyle = 'white';
            context.lineWidth = 2 + 4 * (1 - t);
            context.fill();
            context.stroke();

            // update this image's data with data from the canvas
            this.data = context.getImageData(
              0,
              0,
              this.width,
              this.height
            ).data;

            // continuously repaint the map, resulting in the smooth animation of the dot
            map.triggerRepaint();

            // return `true` to let the map know that the image was updated
            return true;
          }
        };


        const canvas = map.getCanvasContainer();

        const geojson = {
          'type': 'FeatureCollection',
          'features': [
            {
              'type': 'Feature',
              'geometry': {
                'type': 'Point',
                'coordinates': [4, -9]
              }
            }
          ]
        };

        function onMove(e) {
          const coords = e.lngLat;

          // Set a UI indicator for dragging.
          canvas.style.cursor = 'grabbing';

          // Update the Point feature in `geojson` coordinates
          // and call setData to the source layer `point` on it.
          geojson.features[0].geometry.coordinates = [coords.lng, coords.lat];
          map.getSource('point').setData(geojson);
        }

        function onUp(e) {
          const coords = e.lngLat;

          // Print the coordinates of where the point had
          // finished being dragged to on the map.
          coordinates.style.display = 'block';
          coordinates.innerHTML =
            `Longitude: ${coords.lng}<br />Latitude: ${coords.lat}`;
          canvas.style.cursor = '';

          // Unbind mouse/touch events
          map.off('mousemove', onMove);
          map.off('touchmove', onMove);
        }

        map.on('load', () => {
          map.addImage('pulsing-dot', pulsingDot, {pixelRatio: 2});

          map.addSource('points', {
            'type': 'geojson',
            'data': {
              'type': 'FeatureCollection',
              'features': [
                {
                  'type': 'Feature',
                  'geometry': {
                    'type': 'Point',
                    'coordinates': [0, 0]
                  }
                }
              ]
            }
          });
          map.addLayer({
            'id': 'points',
            'type': 'symbol',
            'source': 'points',
            'layout': {
              'icon-image': 'pulsing-dot'
            }
          });


          const marker = new maplibregl.Marker();

          function animateMarker(timestamp) {
            const radius = 20;

            // Update the data to a new position based on the animation timestamp. The
            // divisor in the expression `timestamp / 1000` controls the animation speed.
            marker.setLngLat([
              Math.cos(timestamp / 1000) * radius,
              Math.sin(timestamp / 1000) * radius
            ]);

            // Ensure it's added to the map. This is safe to call if it's already added.
            marker.addTo(map);

            // Request the next frame of the animation.
            requestAnimationFrame(animateMarker);
          }

          // Start the animation.
          requestAnimationFrame(animateMarker);





           // Add a single point to the map
        map.addSource('point', {
            'type': 'geojson',
            'data': geojson
        });

        map.addLayer({
            'id': 'point',
            'type': 'circle',
            'source': 'point',
            'paint': {
                'circle-radius': 10,
                'circle-color': '#3887be'
            }
        });

        // When the cursor enters a feature in the point layer, prepare for dragging.
        map.on('mouseenter', 'point', () => {
            map.setPaintProperty('point', 'circle-color', '#3bb2d0');
            canvas.style.cursor = 'move';
        });

        map.on('mouseleave', 'point', () => {
            map.setPaintProperty('point', 'circle-color', '#3887be');
            canvas.style.cursor = '';
        });

        map.on('mousedown', 'point', (e) => {
            // Prevent the default map drag behavior.
            e.preventDefault();

            canvas.style.cursor = 'grab';

            map.on('mousemove', onMove);
            map.once('mouseup', onUp);
        });

        map.on('touchstart', 'point', (e) => {
            if (e.points.length !== 1) return;

            // Prevent the default map drag behavior.
            e.preventDefault();

            map.on('touchmove', onMove);
            map.once('touchend', onUp);
        });

        })
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
      .coordinates {
        background: rgba(0, 0, 0, 0.5);
        color: #fff;
        position: absolute;
        bottom: 40vh;
        right: 10vw;
        padding: 5px 10px;
        margin: 0;
        font-size: 11px;
        line-height: 18px;
        border-radius: 3px;
        display: none;
    }
</style>
