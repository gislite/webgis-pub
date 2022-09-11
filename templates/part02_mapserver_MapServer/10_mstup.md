# Installation and configuration of MapServer

One of the ways to realize WebGIS is to use Common Gateway Interface (CGI) technology. 
On the server side, through the CGI application program to connect WebServer and GIS spatial database, 
the client only needs to use the browser to query and analyze the spatial data. 
The famous open source GIS server-side tool MapServer uses CGI technology.

Compared with the many WebGIS solutions provided by commercial enterprises, 
MapServer is an open source project. 
This means that you can use MapServer for free and have the right to modify, copy, 
and redistribute it on your own. 
It should be pointed out that MapServer, as an open source project,
is in continuous development, but in recent years, 
the function has been relatively perfect and the update is relatively small.

At present, the mainstream Linux operating systems, such as Debian, Ubuntu, Centos and so on, 
have MapServer versions above 7.0. 
The content of this book is based on MapServer version 7. 0 and later.

This chapter explains the installation and configuration of MapServer to understand basic usage and related tools,
how to generate map images, and how to access them through Web.
After you set up the MapServer, 
you need to tell it the location of all resources 
and make sure that all permissions are set correctly. 
Because more useful MapServer applications have more lines of code and contain many HTML templates, 
keep the application simple to make it easier to debug when errors occur.
