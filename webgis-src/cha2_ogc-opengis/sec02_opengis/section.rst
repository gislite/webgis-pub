.. Author: gislite
.. Title:  OpenGIS Specification

================================================
OpenGIS map service specification
================================================

OGC and OpenGIS
============================================

The OGC is made up of members from a variety of sectors including business sectors,
government agencies, users, and data providers for the largest interoperability in the geographic information processing market.
The purpose of OGC is to integrate geospatial data resources into mainstream computing technologies
through an information infrastructure,
and to promote the widespread application of interoperable commercial geographic information processing software.
The OpenGIS specification provides geographic information and processing standards,
and each system developed according to the specification can freely exchange geographic information and processing functions.

OGC members mainly include GIS-related computer hardware and software manufacturers
(including ESRI, Intergraph, Maplnfo and other well-known GIS software developers), data producers,
as well as some colleges and universities, government departments, etc.,
their technical committees are responsible for the formulation of specific standards.

Open Geospatial Consortium - Open Geospatial Consortium,
a non-profit voluntary international standardization organization,
leading the development of spatial geographic information standards and basic positioning services.
Currently in the field of spatial data interoperability, the interoperability method
based on the public interface access mode is a basic method of operation.
Through the International Organization for Standardization (ISO/TC211)
or technical alliance (such as OGC), the interface specification
for spatial data interoperability is formulated, and GIS software vendors develop spatial data read
and write functions that follow this interface specification,
which can realize the interoperability of heterogeneous spatial databases.
Spatial data interoperability based on http (Web) XML is a very popular research direction,
mainly involving related technologies of Web Service.
OGC and ISO/TC211 jointly launched the Web Service (XML)-based
spatial data interoperability implementation specification Web Map Service,
Web Feature Service, Web Coverage Service and geographic information markup language GML
for spatial data transmission and transformation.

OpenGIS (Open Geodata Interoperation Specification) was proposed by the American OGC
(OpenGeospatial Consortium, OpenGIS Association) DOGC is a non-profit organization,
the purpose is to promote the use of new technologies and business methods
to improve the interoperability of geographic information processing(Interoperability),
which seeks to eliminate the gap between geographic information applications
(such as geographic information systems, remote sensing, land information systems,
automatic mapping/facility management (AM/FM) systems) and between geographic applications
and other information technology applications.
build a "borderless", distributed, component-based geographic data interoperability environment.

OpenGIS refers to a geographic information system established according to industry standards
and interfaces in the computer and communication environment.
It enables data not only to flow within application systems, but also between systems.
OpenGIS is to enable good interoperability between different geographic information system software,
as well as a way to realize information sharing in heterogeneous distributed databases.
The OpenGIS specification is a series of open standards and interfaces developed
by the Open Geographic Information Systems Consortium (OGC).

The goal of OpenGIS is to develop a specification that enables application developers
to use any geographic data and geoprocessing distributed over the Internet
in a single environment and a single workflow.
It is committed to establishing a "borderless", distributed,
and component-based geographic data interoperability environment.
Compared with traditional geographic information processing technology,
GIS software based on this specification will have good scalability and upgradeability,
portability, openness, interoperability and ease of use.

OpenGIS has the following characteristics: 

- Interoperability: The connection and information exchange between different GIS software are barrier-free.
- Scalability: The hardware can run on computers of different software and grades;
  the software adds new geospatial data and geoscience data processing functions.
- Openness: Technology openness is mainly open to users, and the disclosure of source code
  and specification is an important way.
- Portability: Independent of software, hardware and network environment,
  it can run on different computers without modification.

In addition, features such as compatibility, achievability, and synergy.
 
OGC facilitates the interoperability of GIS. It changes the way geographic data
and its services are processed by specification, and integrates them
through an interoperable open system, so that information can be directly obtained
from heterogeneous information through a distributed platform in the Intnmet/Internet environment.
OGC facilitates the alliance between geographic data providers, vendors and service providers.
Promotes the standardization process on a global scale and broadens the geographic data service market.
OpenGIS technology will keep GIS in an organized and open state,
truly become an industry serving the whole society
and realize the global sharing and interoperability of geographic information,
which is the inevitable trend of GIS technology development in the future network environment.

OpenGIS related definitions
===================================================

OpenGIS defines a set of data-based services, and the basis of the data is the feature (Feature).
The so-called feature is simply an independent object,
which may be represented as a polygonal building in the map, and is an independent entry in the database.
Features have two necessary components - geometric information and attribute information.

OpenGIS defines a set of data-based services, and the basis of the data is the feature (Feature).
The so-called feature is simply an independent object,
which may be represented as a polygonal building in the map, and is an independent entry in the database.
Features have two necessary components - geometric information and attribute information.
OpenGIS divides geometric information into four types: point, edge, polygon and geometric collection:
the familiar line (LineString) here belongs to a subclass of edge, and polygon (Polygon)
is a subclass of surface.
That is, the geometry types defined by OpenGIS are not only our common three types of points, lines and polygons.
It provides more complex and detailed definitions and enhances future scalability.
In addition, the composite mode (Composite) is used in the design of the geometric type,
the geometry collection (GeometryCollection) is also defined as a geometry type.
Similarly, a feature set (FeatureCoUection) is also a feature.
The property information is not too restrictive,
and can be set in combination with the specific implementation in the actual application.
The combination of the same geometry type and attribute type becomes a feature type,
and features of the same type can be stored in a single data source.
A data source can only have one feature type. Therefore,
a feature type can be used to describe a group of features with similar properties.

In the object-oriented model, the feature type can be understood as a class,
and the feature is an instance of the class.
The data can be retrieved from the data source through the GIS middleware
for use by the WMS server and the WFS server. The WMS server receives the request,
and can return final data in different formats according to the content of the request.
For example, WMS can return map fragments in common image formats for reading by end users (similar to GoogleMaps),
where the map is generated from a style file (SLD), which describes the map's line width, color, etc.;
WMS can also return GeoRSS and KML for interworking with other map services.
The WFS server can also receive requests, but WFS will return geographic information data in GML format.
GML is an XML-based data format, which can reproduce data completely,
and is also an important form of OpenGIS data source.
That is, the GML returned by WFS can continue as a data source.
In the WFS request, OpenGIS defines a Filter standard to filter data and make WFS more flexible.
On the other hand, WFS also supports committing client-side modifications to data via WFS-t.
Popular to say, WMS is read-only, while WFS can be read and written.


OpenGIS open mode
===========================================================

Open GIS is the transparent access to different kinds of geographic data and geographic processing methods
in the network environment.

The purpose of Open GIS is to provide a set of general components with open interface specifications,
and developers develop interactive components according to these specifications,
these components can realize transparent access between different kinds
of geographic data and geographic processing methods.

The OGIS Engineering and Technology Committee of the Open GIS Consortium,
from small industry to global spatial data infrastructure,
has completed the first part of a series of documents, including OGIS.
The first is called the “Guide to Open GIS Interactivity”,
which provides a comprehensive and in-depth description of OGIS;
the second OGIS document includes a high-level technical language,
which is a language of execution in the full sense and does not require interpretation,
Its manual is published by GIS World Ltd.

But OGIS is not the final object of OGC, and the publication of "Guide to Open GIS Interoperability"
is not the first important milestone of OGC.
The real function of OGC is to formulate a specification in the field of geographic information to unify the industry,
and to integrate the specification into a wider technical field and a larger market,
making it an inseparable part of the global information infrastructure.
The global information infrastructure is mainly an organization
that organizes world-wide activities and solves important environmental and infrastructure problems.
Similar work has been successful in other industries.

International competition is not the problem that OGC wants to solve.
What OGC wants to solve is to separate the industry from the big industry of information technology.
For a long time, GIS was little more than a “domestic handicraft”,
similar in many respects to the constraints of the mechanical industry before the Industrial Revolution,
but this has changed.

The OGIS Engineering and Technology Committee of the Open GIS Consortium,
from small industry to global spatial data infrastructure,
has completed the first part of a series of documents, including OGIS.
The first is called the “Guide to Open GIS Interoperability”.

A new concept "Information communication" in "Guide to Open GIS Interactivity" plays an important role
in the popularization of GIS.

The first version of GIS will standardize the spatial attributes
and support that almost all the information industries need.
OGIS then provides a standard method by which the information industry
(the "Technical licensor" of the entire industry) can codify notations,
develop methods and usage rights for spatial data used in their discipline or industry,
that is, because "Basic OGIS" will be augmented by the notation definitions provided
by the Academic Review Committee and the Association of Professional Organizations,
whose job it is to establish notation and compilation rules for their users,
the notation and compilation rules will determine the information industry interface
for "Basic OGIS" and other disciplines' spatial notation.