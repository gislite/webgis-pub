Use of WFS in MapServer
=======================

We can easily get the map in the specified area from the WMS server, but
we can only get the rendered map. Sometimes we want to get data such as
the geographical coordinates and attributes of a specified layer, and
further, when we need to modify the data of the data source, WMS can not
meet the needs.

However, you can also send data from the Web service to the client upon
request. As long as the server and the client follow the same
specification, the data can be in any format. In order to standardize
the process of sending vector data through Web services, OGC provides us
with another standard Web Feature Service (WFS) to meet the above
requirements.

Next, we will introduce the release, access and application of WFS and
its services.

.. toctree::
   :maxdepth: 2

   sec1_intro/section
   sec2_wfs-client/section
