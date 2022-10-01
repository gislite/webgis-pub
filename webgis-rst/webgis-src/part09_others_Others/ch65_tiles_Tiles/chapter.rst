Map slicing technique
=====================

Map Tiles, translated into map tiles and map slices. In this book, it is
considered that map slicing pays more attention to the process of
operation, so the term “map tile” is adopted.

If you want to improve the access speed of Web maps, using map slicing
is a very effective method. Map slicing is to configure the map under
multiple scale, and then draw the map under each scale as a small
picture in advance and save it in a directory called cache on the
server. In this way, when the client accesses the map, it can directly
get the small pictures needed and splice them into the whole map,
instead of dynamically creating a picture by the server and sending it
to the client, thus greatly improving the access speed.

There are many technical solutions for map slicing, and there are many
open source tools for map slicing, which is a basic tool in all kinds of
FOSS software at present. MapServer has MapCache module, GeoServer has
GeoWebCache module to create map slices; TileMill and CartoCSS markup
languages can create map slices in a more flexible way; and there are
common gadgets such as GeoWebCach, TileCache, TileStache, Tile-Server
and MapProxy. There are other tools that people know less about.

The Mapnik library is a free and open source software written in C++
callable from Python and other languages for creating map tiles. Mapnik
is an efficient rendering engine that includes advanced drawing options
not found in common WMS layers. Although the use of Mapnik is not very
convenient, it usually requires some knowledge of Linux and some
experiments and mistakes, but for profit, Mapbox recently released an
open source program called TileMill, which can be run on Mac and
Windows, with Mapnik as the bottom layer, providing a beautiful window
interface, thus simplifying the drawing process.
