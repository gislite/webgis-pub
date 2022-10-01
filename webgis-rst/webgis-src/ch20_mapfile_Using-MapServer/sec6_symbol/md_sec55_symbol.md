; Author: Bu Kun
; Title: Use custom styles in Mapfile

# Use custom styles in Mapfile

Vector data can be divided into three types: point, line and surface.
The simplicity of the data type structure gives the diversity of expression.
In MapServer, you can set styles in various dimensions such as color, size (thickness), and transparency for points, lines, and surfaces.

## Point

<div align="center">
<img class="img_border" src="http://webgis.pub/cgi-bin/mapserv?map=/owg/mfy3.map&layer=world-country&layer=world-city&mode=map"/>
</div>

The Mapfile used is:

->-> mfy3.map

## Line fill example

<div align="center">
<img class="img_border" src="http://webgis.pub/cgi-bin/mapserv?map=/owg/mfu1.map&layer=world-country&mode=map"/>
</div>

The Mapfile used is:

->-> mfu1.map

## Circular fill exampl

<div align="center">
<img class="img_border" src="http://webgis.pub/cgi-bin/mapserv?map=/owg/mfu2.map&layer=world-country&mode=map"/>
</div>

The Mapfile used is:

->-> mfu2.map

## River style

<p align="center">
<img class="img_border" src="http://webgis.pub/cgi-bin/mapserv?map=/owg/mfmr.map&layer=wroads&mode=map" />
</p>

The Mapfile used is:

->-> mfmr.map

``GepMap`` can be further used to get the effect of the magnification:

<p align="center">
<img class="img_border" src="http://webgis.pub/cgi-bin/mapserv?map=/owg/mfmr.map&SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMAP&LAYERS=wroads&BBOX=73,3,136,54&CRS=CRS:84&INFO_FORMAT=text/html&format=image/png&width=500&height=300&styles=" />
</p>
