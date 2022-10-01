Use of WCS in MapServer
=======================

WFS publishes vector data service on the Web, while for raster data
service, OGC formulates WCS (Web Coverage Services, network coverage
service). The raster data set obtained through WCS service is called
overlay, where the coverage is generally raster data, but also includes
TIN and so on. The data returned by the WCS service can be used as input
parameters for analysis and modeling operations. This is in sharp
contrast to the OGC WMS service, which only returns pictures of the
data.

There is no built-in support for WCS in the front-end libraries Leaflet
and OpenLayers. If you are a service / data provider and the coverage
data is two-dimensional, you can consider the WMS that provides the data
at the same time. If you are not a service provider and you have only
one WCS endpoint to use, you will not be able to write your own code.
Similarly, if you have multidimensional coverage and want to provide
two-dimensional data, you have to do the same. Examples can be found on
the Internet.








.. toctree::
   :maxdepth: 2

   sec01_wcs/section
