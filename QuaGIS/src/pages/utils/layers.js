import L from 'leaflet'
/**
 * add polygon
 * @param {*} latlngs
 */
export function addPloygon (latlngs ) {
  var layer = L.polygon(latlngs , {color: 'rgb(80,227,194)'})
  return layer
}

/**
 * add scatterPoint
 * @param {*} latlngs
 */
export function addScatterPoint (latlng) {
  let circleMarker = L.circle(latlng,{
    radius:800000,
    fillColor:'red',
    fillOpacity:'1',
    color: 'red', //颜色
  })
  circleMarker.on('mouseover',function(){
    circleMarker.bindPopup('<p>Hello world!<br />This is a nice popup.</p>').openPopup();
  })
  circleMarker.on('mouseout', function(){
    circleMarker.closePopup()
  });
  return circleMarker
}



/**
 * add scatterPoint VIP
 * @param {*} latlngs 点经纬度
 */
export function addScatterPointIcon2 (latlng) {
  var iconSettings = {
    mapIconUrl: '<svg version="1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 149 178"><path fill="{mapIconColor}" stroke="#FFF" stroke-width="6" stroke-miterlimit="30" d="M126 23l-6-6A69 69 0 0 0 74 1a69 69 0 0 0-51 22A70 70 0 0 0 1 74c0 21 7 38 22 52l43 47c6 6 11 6 16 0l48-51c12-13 18-29 18-48 0-20-8-37-22-51z"/><circle fill="{mapIconColorInnerCircle}" cx="74" cy="75" r="61"/><circle fill="#FFF" cx="74" cy="75" r="{pinInnerCircleRadius}"/><image x="34" y="35" width="80" height="80"  xlink:href="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fwww.51tfb.com%2Fuploadfile%2F20190316%2F201903160950595c8c568363cdc.jpg&refer=http%3A%2F%2Fwww.51tfb.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1633143290&t=bf91e17fa94f787ffafaa729eb843a6f"/></svg>',
    mapIconColor: 'red',
    mapIconColorInnerCircle: '#fff',
    pinInnerCircleRadius:48
  };
  var divIcon = L.divIcon({
    className: 'leaflet-data-marker',
    html: L.Util.template(iconSettings.mapIconUrl, iconSettings), //.replace('#','%23'),
    iconAnchor  : [12, 32],
    iconSize    : [30, 30],
    popupAnchor : [0, -28]
  });
  var marker = L.marker(latlng, {
    icon: divIcon,
    id: 'scatter'
  });
  return marker
}
/**
 * new scatterPoint style
 * marker.setIcon(newScatterStyle);
 * @param {*} color 颜色
 * @param {*} radius 半径
 * @param {*} isVip 是否是vip
 */
export function newScatterStyle (color,radius,isVip) {
  var iconSettings
  if(isVip){
    iconSettings = {
      mapIconUrl: '<svg version="1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 149 178"><path fill="{mapIconColor}" stroke="#FFF" stroke-width="6" stroke-miterlimit="30" d="M126 23l-6-6A69 69 0 0 0 74 1a69 69 0 0 0-51 22A70 70 0 0 0 1 74c0 21 7 38 22 52l43 47c6 6 11 6 16 0l48-51c12-13 18-29 18-48 0-20-8-37-22-51z"/><circle fill="{mapIconColorInnerCircle}" cx="74" cy="75" r="61"/><circle fill="#FFF" cx="74" cy="75" r="{pinInnerCircleRadius}"/><image x="34" y="35" width="80" height="80"  xlink:href="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fwww.51tfb.com%2Fuploadfile%2F20190316%2F201903160950595c8c568363cdc.jpg&refer=http%3A%2F%2Fwww.51tfb.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1633143290&t=bf91e17fa94f787ffafaa729eb843a6f"/></svg>',
      mapIconColor: color,
      mapIconColorInnerCircle: '#fff',
      pinInnerCircleRadius:61
    };
  }else{
    iconSettings = {
      mapIconUrl: '<svg version="1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 149 178"><path fill="{mapIconColor}" stroke="#FFF" stroke-width="6" stroke-miterlimit="30" d="M126 23l-6-6A69 69 0 0 0 74 1a69 69 0 0 0-51 22A70 70 0 0 0 1 74c0 21 7 38 22 52l43 47c6 6 11 6 16 0l48-51c12-13 18-29 18-48 0-20-8-37-22-51z"/></svg>',
      mapIconColor: color,
      mapIconColorInnerCircle: '#fff',
      pinInnerCircleRadius:61
    };
  }
  var divIcon = L.divIcon({
    className: 'leaflet-data-marker',
    html: L.Util.template(iconSettings.mapIconUrl, iconSettings), //.replace('#','%23'),
    iconAnchor  : [12, 32],
    iconSize    : [radius, radius],
    popupAnchor : [0, -28]
  });
  return divIcon
}
