.. Author: gislite .. Title: Map and WebGIS

Map and WebGIS
==============

The role of maps
----------------

Maps have played an important role in human activities for thousands of
years. The world consists of things that have a geographic
(i.e. spatial) relationship to each other, and while a map can be an
exact replica of the world, it usually isn’t. Maps are models that
contain representations of things in the world, but those models don’t
need to be represented in a similar way to the things they represent, or
even have the same spatial relationships. The real world is the domain
of geographers and geographers, and the process of representing real
world things on this plane is cartography. Geographers live on the
surface of a large, approximately oblate ellipsoid, with topography, in
three-dimensional space; maps are where cartographers live and work, and
are small in scope and flat.


.. figure:: fig-old-map.jpg

   Map of the World

The Golden Age of Maps and Cartography corresponds to the Age of
Exploration, when maps were the key to great wealth. The tools that
propelled this golden age were compasses, sextants, and precise clocks.
Digital maps, geographic information systems (GIS), and location-based
services represent the next golden age of mapping and cartography. The
tools driving this era are computers, the Internet, and the Global
Positioning System (GPS).

In the modern world, clear and powerful messaging is essential for
business, science and political activity. All kinds of natural and human
events occur on the earth on which we live, generating trillions of
massive amounts of data every moment, and more than ``80%`` of these
data are related to spatial locations. Whether the information to be
conveyed is demographic data, weather forecasts or environmental
monitoring data, it has a geographic distribution. Just as graphs
present numerical information in an easy-to-understand manner, maps can
show more clearly than any tabular format how information relates to
location, enabling users to view that information according to its
spatial orientation. While this distribution information is implicit in
the table of numbers, it is hard to see without showing it in a map.

Geographic information science transforms the data from the original
two-dimensional character state into a spatial visualization language or
knowledge that we can easily understand by studying the collection,
storage, processing, analysis, expression and service methods of these
data that are directly or indirectly related to geographic space. , so
as to serve the environment, land, planning, water conservancy, energy,
transportation, residents’ life and other aspects.

Historically, accurate maps have been difficult to make, and once maps
are made, they are static and difficult to maintain and update. In the
absence of other competing technologies, the very nature of these
cartography limits the usefulness of paper maps. A decade ago, traffic
route maps provided a good example of the limitations of paper maps. A
lot of people keep them in their cars, even though they are always
outdated. In order to present more information in a small page, fonts
are often small, which makes them difficult to read. If you don’t want
to see the streets, but rather see the locations of restaurants in town,
you usually need to buy different types of maps. In other words, maps
are often single-purpose files for a certain topic, acting as archives
of past locations.

Application of Digital Map
--------------------------

Digital maps ensure convenient and efficient presentation of graphic
images. Therefore, they can also display current information dynamically
and in real time. However, hard copy mapping work has been (and still
is) the home page aspect of the collection and maintenance of underlying
information. In fact, the dynamic nature of digital maps exacerbates
maintenance efforts as performance and data requirements are very high.

The development of digital maps is driven by the needs of industry (eg
mining), natural resource managers and researchers for geospatial
information management. However, with the rise of the Internet and the
commoditization of hardware, digital maps have become ubiquitous.
Several digital map applications are now common, including weather maps
displayed in morning weather reports, driving instructions obtained from
GPS-enabled car navigation systems, and Internet sites that provide
street maps on demand.

However, most of these applications cannot meet the needs of mobile
users. For example, a GPS-enabled car navigation system can determine
your current location and tell you how to get elsewhere, but since it
only has access to onboard data (at best), it cannot provide services
that require real-time information. These services will include optimal
routing with congestion avoidance and real-time location-based services
(eg, the lowest fuel prices within five miles).

However, applications are being developed that are network-aware and
intelligent (ie, they are wireless and GPS-enabled). Some examples are
management tools for GPS-enabled garbage collection, systems for
providing driving instructions to emergency vehicles, and systems that
allow shippers to locate goods in transit. Mobile technologies such as
WiFi 2.5 and 3G cellular will bring new possibilities.

When wireless technology is ubiquitous and bandwidth is cheaper, what
will be the killer application? Before the internet existed, no one
would have predicted the popularity and profitability of a company like
Google — a catalog of content from tens of millions of computers on the
internet, free for anyone to use. This particular application was the
invention of two college students who had a great idea and access to
cheap technology. While I won’t try to predict what the killer mobile
app will be, the fact that it will be a mobile app suggests that the map
feature will be a necessary aid.

The role of open source GIS
---------------------------

But the problem is that if some smart college student or entrepreneur
wants to integrate killer apps and get rich, it can cost thousands of
dollars to buy the data and/or services needed to break into the
industry. Commercial proprietary technology, while powerful, is very
expensive. Whether it’s outright purchasing of proprietary software,
ordering spatial information, or outsourcing complete applications,
producing high-quality map applications using commercial software is
expensive. If there is a set of stable system requirements, some funds
of the bank, and a market opportunity suitable for you, proprietary
options may be a good choice.

However, if you are entering the market tentatively, with a dynamic set
of system requirements (or none at all); or if you are short on funding,
or just trying to use the technology, you should look into
`MapServer <https://www.%20mapserver.org/>`__ , which is the subject of
this tutorial. MapServer is a map rendering engine that can be run in a
web environment as a CGI script or as a standalone application through
an API accessible from multiple programming languages. To quote the
description from the MapServer home page, “MapServer is an OpenSource
development environment for building spatially enabled Internet Web
applications.” With help from the University of Minnesota, NASA, and the
Minnesota Department of Natural Resources, MapServer is now hosted by
nearly 20 developers from around the world.

There are many reasons why you may consider using MapServer: maybe your
boss refuses to put the map into his pet project at the price of
commercial products and tells you to find something on the Internet;
Maybe you have a dataset containing some spatial information, and you
want to share it graphically on the Internet; Maybe you want to expand
your pet project. You think providing online maps will have a great
impact; Or maybe you just like maps and think about making beautiful
maps from digital sources that make you happy. But before you look at
MapServer to see if it’s what you need, you have to understand what it’s
not. MapServer is a tool for presenting geographic data to the web - it
is not a fully functional GIS (although it can be used to build one).

Application of MapServer
------------------------

This tutorial introduces some open source GIS tools, but uses MapServer
on the server side.

The following is a brief description of the three types of applications
that can be developed using the MapServer API. (They can also be done
via CGI, but the process is slow, cumbersome, and ugly.) By adding a
MySQL database and a programming language like PHP, these applications
can provide considerable functionality without a lot of development
work, because This is difficult, the spatial awareness part is done by
MapServer. None of these are particularly innovative, but they do
demonstrate what can be done.

Real estate sales tools

By adding the latitude/longitude coordinates of each sale property to an
MLS (multiple listing service) or similar service, you can create a
spatially aware catalog that provides the functionality users expect
from a graphical interface (such as click and drag space to pop up query
and info boxes when the mouse hovers over a hotspot).

Real-time tracking and tracing

By collecting GPS locations in real-time and forwarding them back to the
host over 2.5 and 3G cellular technologies, MapServer can help you build
customer-facing applications that show the actual location of loads in
real-time. MySQL databases are great for storing this type of data.

Real-time traffic consultation and congestion avoidance

Gather traffic levels electronically or by manually entering GPS
coordinates, street addresses or intersections - MapServer can display
traffic levels in real-time, served over the web, and suggest
alternative routes.
