.. Author: Bu Kun
.. Title: Geographic Web Service Standard

# Interoperability and geospatial Web service standards


Interoperability is often involved in large projects or national information platforms. Interoperability is to allow software and data from different manufacturers to work together, and the main way to achieve interoperability is to formulate standards. In essence, the standard of Web service is to specify the specific format of request and response, for example, which parameters are included in the request, what type of each parameter is, and what result is included in the returned information of the response. Web map service standards defined by OGC, including WMS, WMTS, WFS, WCS, WPS, CSW and Web service-related standards, as well as KML and GeoRSS.

The meanings of the three most commonly used geo-reference information models are as follows:

- Web Map Server (WMS)
- Web Feature Server (WFS)
- Web Coverage Server (WCS)


### Interoperability based on Web Services


Interoperability is to allow software and data from different manufacturers to work together. In layman's terms, I can call your data and functions, and you can call my data and functions. The realization technology of GIS interoperability has gone through many stages, and the technology of implementing GIS interoperability has mainly gone through the stages of file format conversion, direct reading plug-ins and Web service standards.

    |----------------------|     |--------------------------|     |---------------------|
    |File format conversion| --> |Plugins for direct reading| --> |Standard Web Services|
    |----------------------|     |--------------------------|     |---------------------|


Early interoperability often involves data conversion, for example, converting the data of one software product into the data format of another software product, or defining a standard file format. Different software products need to be able to input and output this format. The plug-in can be used to directly read and write data in one of the software plug-ins, that is, it can be used to directly read and write data in another software plug-in.
In recent years, the interoperability technology has gradually shifted to the level of Web service standards. This method not only avoids the export and import of data formats, but also avoids the trouble of installing plug-in tools locally. Different manufacturers can independently develop their own products according to the industry's Web service standards.
As long as the Web service interface of their products conforms to certain industry standards, the data and functions of their software can be called with each other through Web services to achieve interoperability (Figure 3.12).

![Interoperability depends on standards](imgvze35.jpeg)

There are mainly the following standardization organizations about geospatial web services.


Taking OGC's WMS standard as an example, a WMS online map service published by MapServer or GeoServer can be used not only by Esri products, but also by clients that support WMS standards such as Google Earth, NASA WorldWind, OpenLayers, and Gaia. Each client knows what parameters should be sent in the request, and can expect the server to respond in what format.


## Standards for Web services


This section mainly introduces the WMS, WMTS, WFS, WCS, CSW, WPS and OpenLS standards of OGC. Readers can visit the official website of OGC (http://www.opengeospatial.org) to check the detailed documents of these specifications, and check which WebGIS software has been certified by OGC and which standards are supported.

### (1) Web Mapping Service (WMS-Web Map Service)

WMS is a Web service specification developed by OGC for making maps on the Internet. The maps produced by WMS are generally presented in image formats, such as PNG, GIF or JPEG. Any web service that claims to conform to the WMS specification must support the following two necessary requests:

GetCapabitities: Return the description information of the Web service to the client. The format of the returned result is XML, which describes the service's name, introduction, keywords, coverage, which data layers are included, what coordinate system each layer is, what attributes it has, and whether it can be queried. This metadata also includes the map image file format that the service can generate, the URL of each operation that can be supported, and so on.

GetMap: Make a map according to the client's GetMap request parameters.
The parameters required in the GetMap request include which layers to display, the length and width of the map, and the spatial coordinate system.
Some WMS also support styled layer definition (styled layer descriptor, SLD), allowing users to dynamically specify the display symbols of each data layer in the URL request.
The returned results are generally images in raster formats such as PNG, GIF, and JPEG.

The WMS specification also provides several optional requests, such as

- GetFeaturelnfb: query the information of a location on a map, its typical application is that the user clicks a point on the map, and the server returns the coordinate information and attribute information of the geographical elements located at that point.

- GetLegendGraphic: the legend of the layer can be made and returned according to the layer specified by the client. The return format is generally PNG, GIF and JPEG images.

The WMS specification is widely used and adopted by many organizations. For example, the United States Geological Survey (USGS) provides a series of WMS services, including the National Big Map WMS service, the National Atlas Transportation WMS service, the National Hydrographic Dataset WMS service, and the US real-time fire (mainly refers to wildfires) WMS service .

NASA Earth Observation System (NEO, http://neo.sci.gsfc.nasa.gov/Search.html) WMS ( http://neowms.sci.gsfc.nasa.gov/wms /wms ) and other methods to dynamically provide multi-time-series images of global climate and environmental changes, including sea surface temperature, land surface temperature, vegetation index, precipitation, carbon monoxide concentration, surface cover types, and the solar radiation received by the surface amount, etc.


### (2) Web Map tile Service (WMTS-Web Map Tile Service)

WMTS is a Web service specification for publishing tile maps formulated by OGC. WMTS is different from WMS, and the two complement each other.

WMS is mainly a dynamic map service, that is, the map is generated immediately by the server every time it receives a client request, which is especially suitable for map services whose data is constantly being updated.
The map of WMTS is a tile pre-made by the server. This method can improve the performance and scalability of Web services, and is especially suitable for data whose data is relatively static and no longer updated or updated frequently.

The WMTS specification defines two necessary actions and one optional action.

- GetCapabilities: gets the metadata of the service.
- GetTile: get the tiles.
- GetFeaturelnfo: optional, get the feature information that you click on.

### (3) Web essential Services (WFS-Web Feature Service)

WFS is developed by OGC to manipulate vector geographic elements and data on the Internet.
It includes Web service specifications such as retrieval, insertion, update and deletion (OGC, 2005).
WFS defines the following main operations.

- GetCapabilities: gets the data of the service.
- DescribeFeatureType: gets the structure of the feature types supported by WFS.
- GetFeature: gets the geographic features and their attributes that match a query condition.
- LockFeature: requests the server to lock one or more geographic features during a transaction.
- Transaction: request the server to create, update, or delete geographic features.

The above operations are required and optional. According to the supported operations, WFS can be divided into the following two main categories.

- Basic WFS (Basic WFS): only GetCapabilities, DescribeFeatureType and GetFeature operations are supported
  It can only query and read elements, so it is also called read-only WFS.
- Transactional WTFS (TransactionWFS or WFS-T): supports transaction operations in addition to those supported by basic WFS.
  It can not only support the reading of geographical elements, but also support the online editing and processing of geographical features, also known as read-write WFS.

In the WFS request and response, the information transmission of geographical elements is mainly in GML format.
In 2006, OGC adopted the GML simple element specific Standard (GML Simple Features Profile) to accelerate the speed of WFS request and response and simplify the difficulty of WFS implementation.
WFS can be used not only for mapping and query, but also for geographic data cutting, projection conversion and online download.
For example, the National Weather Service Meteorological Research Laboratory provides a National Digital Weather Forecast Database (NDFD) WFS service.
The service allows the public, government agencies and enterprises to obtain data such as temperature, dew point, wind, precipitation probability and precipitation.

### (4) Web coverage Service (WCS_Web Coverage Service)

WCS is a Web service specification for publishing raster geographic data developed by OGC. The raster data it returns is raw data, such as the ground elevation value in digital elevation and the spectral value in satellite images. WMS is different because WMS returns a visualized image that has lost its original value.

The difference between WCS and WFS is that WFS is for vector data, while WCS is for raster data. The WCS specification specifies the following operations (OGC, 2006b):

- GetCapabilities: returns the metadata for the service.
- DescribeCoverage: returns the detailed description of the grid data layer in the service
  Such as time information, coverage, coordinate system and supported output format and so on.
- GetCoverage: the server operates according to the data layer, space-time range, coordinate system, output format, interpolation method and data cutting and conversion specified by the client.
  

The National Snow and Ice Data Center (NSIDC) provides WCS services for the polar cryosphere. Users can obtain data on icing areas, including monthly ocean ice and concentration areas, snow coverage, and snow depth contours. Support research on polar ice cap melting and climate change (Maurer, 2007).

### (5) Web processing Service (WPS-Web Processing Service)

WPS is a Web service specification (OGC,2007c) provided by OGC for geographic analysis on the Internet.
It defines the input and output (that is, request and response) formats of geographic analysis services, as well as how the client requests the execution of geographic analysis.
The geographic data needed by WPS can be transmitted through the Internet, or it can be the data already available on the server.
The main operations defined by WPS are GetCapabilities, DescribeProcess, and Execute.

### (6) other Web service standards

- Catalog Service for Web (CSW): Catalog Service is an important technology for sharing geospatial information. CSW supports searching and publishing of geospatial metadata, which allows users to query metadata to discover the geographic data and services they need, and allows providers to publish and update metadata. There are two types of CSW: read-only CSW and transactional CSW.
Read-only CSW supports operations such as GetCapabilities, DescribeRecord, GetRecords, GetRecordByld, and GetDomain, and only supports metadata query and reading.
Transactional CSW supports metadata reading and writing, allowing users to publish, edit, and delete metadata through ``transaction`` and ``harvest`` operations (OGC, 2007b). Products such as ArcGIS Geoportal Server provide a CSW interface.

- Open location Services (OpenLS-Open Location Service): this is a series of Web service specifications provided by OGC for location-based services (LBS; see Chapter 5).
Including yellow pages search, tracking mobile phone users' location and navigation services (OGC, 2004).

- Sensor Network Integration Framework (SWE—Sensor Web Enablement): The SWE framework includes a series of Web service standards: Sensor Observation Service (SOS), Sensor Planning Service (SPS), and Sensor Alarm Service (SAS). These standards enable users to discover and obtain sensor data from sensor networks.

## Related standards of Web services

This section mainly introduces KML specification and GeoRSS specification. KML is a mixed format of geographic data and map description.
GeoRSS can be thought of as a geographic data format.
Although they are not Web service specifications themselves, in practical applications, they are often used as a format for some Web services to return results.


### (1) KML (Keyhole Markup Language; keyhole markup language)

KML is a XML-based file format for describing geographic elements and their visualization by Google and OGC.
KML was originally created by Keyhole and is the file format adopted by its EarthViewer 3D.
Keyhole was acquired by Google in 2004 and its EarthViewer 3D was renamed Google Earth.
KML officially became an official standard of OGC in 2008.

A KML file can describe some geographical features, such as points, lines, polygons, images, 3D models, etc.，you can define their display symbols, camera positions (that is, the location and height of the observer, the direction of the line of sight, and the angle of overlooking or looking up).
KMZ files are compressed KML files, which on the one hand can reduce the size of the file.
On the other hand, you can include pictures needed for symbols and links in other types of files such as KML.
Here is a simple example of KML. It first defines a style with a specific icon
Then a place name annotation is defined and displayed with this icon.

KML is often used to publish public information. For example, the United States Geological Survey uses KML to release near real-time seismic information.
National Oceanic and Atmospheric Administration uses KML to issue weather forecast, including severe weather warnings, radar images and sensor observations.


### (2) GeoRSS

RSS is short for Really Simple Syndication, also known as rich site summary (Rich Site Summary) or RDF site summary (Resource Description Framework Site Summary).
It is a main format for publishing information on the Internet, especially effective information (such as news and fire bulletins, etc.).
The RSS family includes RSS and ATOM formats, the former in 1999 and the latter in 2003.
They are all simple XML format, with only a few tags to describe the name, summary, full-text link and release time of each message, etc., which are very easy to understand and use, and have been widely used.
Subscribers can "aggregate" multiple RSS they are interested in into RSS reader software to provide themselves with a convenient "one-stop" service without having to go to each website to see if they have been updated over and over again.

RSS is used by many news media, social networking sites and official government websites as a way to release new news.
For example, CNN, the New York Times, Reuters, Science magazine, Twitter (a Weibo site in the United States) and Y0uTube (a famous video site) all use this technology to publish information in a timely manner.
The World Health Organization (WHO) publishes the latest epidemics and infectious diseases in RSS format (http://twitter.com/statuses/user Murtimeline 14499829.RSS):
The U.S. government posted thousands of RSS; using RSS on its e-government portal (http://USA.gov), and the Federal Emergency Management Agency released news and pictures related to emergencies.
The U. S. Census Bureau releases news such as current demographics; the Centers for Disease Control and Prevention releases the latest reports on disease morbidity and mortality.

![The US government publishes thousands of RSS on its e-government portal (http://USA.gov)](imgvze39.jpeg) 

With the popularity of RSS, people want to see not only what happened, but also where it happened.
GeoRSS is a standard (OGC,2006c) for adding location information to RSS and other XML.
GeoRSS has three formats: W3C Geo, OGC GeoRSS-Simple, and GeoRSS-GMLO

- W3C Geo: only point features can be described, using WGS 84 latitude and longitude coordinates. Although this standard is still in use, it is already an outdated standard and is not recommended.
- OGC GeoRSS-Simple: ability to describe basic geometry (including points, lines, rectangles, and polygons) and their attributes (including feature types, feature names, relational labels, elevations, and radii). Worthy of the name, the design of GeoRSS-Simple is simple and clear, and its coordinate reference system is usually WGS 84 longitude and latitude.
- OGC GeoRSS-GML: supports more geographic features than GeoRSS-Simple. If the coordinate reference system is not specified, its coordinates default to WGS84 latitude and longitude, but this specification allows other coordinate systems to be defined and adopted.

Through the extension of RSS, GeoRSS has become a concise format for requesting, sharing and integrating geographic information on Web.
GeoRSS is also widely used in Mashup applications. Here are some examples of GeoRSS applications.

- Twitter provides near-real-time "who said what and where" GeoRSS information, allowing users to display these Weibo content on a map.
- Flickr online albums provide a REST interface that returns photo information for a given area in GeoRSS format. For example, http://api. Flickr. Com/services/feeds/geo/United + States/Califomia/Hollywoocl this URL can return the photo information of Holima area in the United States.
- The Global disaster Alert and Coordination system (http://www.gdacs.org) provides a near-real-time GeoRSS source for timely reporting of ongoing natural disasters around the world, such as earthquakes, tropical hurricanes and floods.
- USGS broadcasts earthquake information in GeoRSS format, among them, seismic data are updated every few minutes in California and every half an hour in other parts of the world.
- GloballncidentMap.com provides a range of real-time GeoRSS content including child abduction alerts, hazmat status, terrorism and other threats.


GloballncidentMap.com provides a series of events related to public safety and terrorist threats in GeoRSS format, and this example uses ArcGISViewer for Flex to show these events and their location.
(note: because there are too many sources of information, it is inconvenient to obtain permission. This picture is an imitation; thanks: TmnsitSecurityReport.com and the National Park Service)
    
![GloballncidentMap.com provides a collection of events on public safety and terrorist threats in GeoRSS format](imgvze40.jpeg)


### Challenges faced by standardization bodies


GIS product and application developers want standards to be simple and easy to use, but standardization bodies often need to consider a variety of situations, so that the standards developed are more inclusive, but often lead to standards that are too complex to be adopted.
OGC's Sam Bacharach (2006) used the following metaphor to explain the need to simplify the GML (Geographic markup language) standard:
"have you ever noticed how children use 64-color crayons? Some children can paint by checking out red, blue, green, yellow, black and other colors.
These colors are simple and easy to use, although not many, but they have provided a solution to the problem to depict a picture of a puppy playing in a backyard swimming pool. "

This metaphor explains not only the importance of simplifying GML, but also the challenge faced by standardizing bodies, namely, how to strike a balance between simplicity, ease of use, and completeness and comprehensiveness.

In addition, the industry hopes that standardization bodies can formulate standards as soon as possible for adoption by the industry.
The standardization body has its own careful work flow, from setting direction, inviting proposals, project team or members to submitting drafts to members' review, revision and voting, it takes a certain amount of time to develop a standard.
This often leads to the lag of standards. By the time the standard is released, different manufacturers have developed their own solutions, which are not compatible with the standard, and these manufacturers need to invest extra people.
Make some changes to the product or write some transfer programs to achieve support for standards.

The importance of standards is unquestionable, especially in government project bidding projects, the bidding products are often required to support international standards to achieve openness and scalability of the system. The OGC website lists certified product manufacturers, software names, names and versions of supported OGC standards (see ``http://www.opengeospatial.org/resource/products/compliant``).

## Optimization of Web Services


This section describes how to improve the quality of service (quality of service,QoS) of Web. The quality of service mainly includes the following important indicators.

- Performance: describes the response efficiency of the system, usually measured by response time
- Scalability: describes whether the system can maintain high performance with an increase in the number of users, usually measured by the number of users it can support at the same time
- Availability: describes how accessible and operable a system is, usually as a percentage of the system's elapsed time.
The availability of a system is ``99.99%`` Then the system can only have a maximum of 9 seconds of downtime per day (including accidental downtime caused by failure and artificial downtime required for system maintenance)
- Security: describes the confidentiality and defense capabilities of the system.

### Preprocessing (caching)

Preprocessing, also known as caching, means that the system generates maps in advance or performs other tasks, and stores the results for later use, instead of generating maps or performing tasks in real time when the system is running and receiving user requests.

As shown in the figure, if there is a cache, the Web server can quickly retrieve the results from the cache, without the need to read data from the database, and complete the mapping and other processing in real time. Cache reduces the burden of GIS server and database server, and is an effective way to improve the quality of WebGIS services.

The Web server can quickly find the results from the cache and respond to user requests quickly, thus reducing the pressure on the GIS server and database, and improving the quality of service caching technology is mainly used to generate maps.

![Web access map slices](imgvze41.png)


Map cache, also known as map tiles or slices, is scheduled to generate a series of map slices (or tiles) according to a series of scales for quick display.

![Map slicing](imgvze42.png)


The main reasons for making map caching are:

- Improve the performance, scalability and availability of the system: caching reduces the burden on the server, and users can get a quick response, thus saving users time.
- Improve the quality of mapping: advanced symbols and complex layers can be used to produce high-quality maps.
- Industry convention: caching is widely used in the current Web map application, which has become a common practice in the industry.
  It also changes users' expectations of WebGIS, and they expect all WebGIS to provide a better user experience such as caching.

Before creating a cache, some planning needs to be done, for example, which coordinate system to use and which tiling scheme to adopt. The tile scheme includes scale level, scale of each level, tile size (eg 256px x 256px), tile start coordinates, tile area and image format (eg JPEG, PNG 8, PNG 24 or PNG 32) .

If your map will be used with ArcGIS Online, Google Maps or Microsoft Bing Maps, then your map should be in the same coordinate system as them, i.e. WGS 84 Web Mercator, and your tile scheme should match them match.

The creation of the cache may take a long time to complete, depending on the complexity of the map and the tile scheme, especially the scale series and the size of the scale. The layers with the largest scale generally occupy most of the time for creating the cache.

Caching is best for maps that change infrequently, such as street maps, imagery maps, topographic maps, and other underlying basemaps. If your data changes frequently, you can regularly update the cache to ensure the tile's current status, or you can use the dynamic map method without tiles.


### Optimization of algorithm and system


WebGIS should carefully consider software algorithms and the optimization of software and hardware systems to achieve the best performance.
Each GIS task has many different implementation methods. Discovering and adopting the optimal algorithm can greatly improve the performance of the system.
For example, when map caching is not feasible or not the optimal solution, it is necessary to draw a map dynamically, but it is generally slow to generate a map dynamically.
GIS database debugging is also an important part of WebGIS.

Some basic techniques include unifying geographic data into desired projections (eg Web Mercator); creating indexes, including spatial and attribute indexes;
Maintain efficient tablespaces; clean up fragmentation of tablespaces and server drives; preload indexes and even data into memory;
Update database statistics in a timely manner (so that the database can choose the best execution path when executing queries).
The configuration plan of the system needs to consider how many users there are, how many people may be using the system at the same time, what they are doing with the system, how big the data volume of the system is, how the data volume will grow in the future, the response speed and availability required by the project How much is enough software and hardware to configure based on these factors.

### Failover and load balancing


Failover and load balancing are two deployment methods to improve system reliability and availability through redundant configuration.
Failover means that when a server fails or needs maintenance, the system can automatically or manually redirect the Web user's request to another server.
Load balancing is assigning user requests to two or more servers, allowing multiple servers to share the work of the system.
Large WebGIS systems should consider failover and load balancing.
The site uses a Web gateway to accept incoming requests and distribute these requests to multiple GIS servers to achieve load balancing.
If a GIS server computer becomes unavailable, the Web gateway can assign requests to the remaining GIS servers, creating a "high availability" architecture.

### Reduce the pressure on Internet bandwidth


The Web service receives the client's request and returns the result to the client. The data transmission between the two, especially the transmission of geographic data, often requires considerable Internet bandwidth; otherwise, the quality of the Web service will be affected. The following methods can reduce the pressure on Internet bandwidth, which can improve the quality of web services.

- Take advantage of the browser-side cache: the browser-side cache is different from the server-side cache. The server-side cache is mainly used to generate map tiles or other results in advance.
The browser-side cache mainly refers to those content that has been downloaded to the browser, do not download again.
The cache content on the browser side is often identified by URL, so the REST-style Web service makes it easy for the system to make full use of the cache on the browser side to improve the performance of the system.
- Use HTTP compression: enable the compression option of the web server, compress the request and result of the web service, and then transmit it, which can reduce the amount of data transmission by 50% and improve the transmission efficiency of the system.
- Choose the appropriate data format: for example, in many cases, JS0N and AMF are lighter than XML and easier to transmit than XML.

### Security Protection of Web Service


Many geographic Web services are public and free, but the Web services released by some enterprises and government agencies may contain content that involves the company's secrets, customer privacy or charges, and these Web services need to be protected. Here are some basic techniques for securing web services.

- Use of private network and virtual private network: In this solution, the Web service and its users are co-located in the internal network of a certain unit, and are isolated from the external network through firewalls and other methods, so that external network users cannot access. A Virtual Private Network (VPN) creates a secure tunnel on the Internet. Through the VPN, even if the client is not in the office of the unit, still can log in to the intranet and use the web services on the intranet.
- Authentication: Secure web services with user roles and permissions. User identities can be managed using Lightweight Directory Access Protocol (LDAP), Windows Active Directory, etc.
- Security token (token):-A token is an encrypted string that contains encrypted authorization information. Tokens are obtained through application or when the user logs in.
- Secure Hypertext transfer Protocol (HTTPS): HTTPS encrypts data transferred between Web services and customers to prevent information from being intercepted and tampered with.
-  Reverse proxy: use a proxy server to accept connection requests on the Internet, then forward the request to the server on the internal network, and return the result obtained from the server to the client. In this way, the proxy server can hide the GIS server in the intranet, providing a barrier between the GIS server and possible malicious attacks, providing a layer of protection.

![Geospatial Web service protection](./imgvze43.png)

Web service technology is an important progress in distributed computing and GIS, and it is the core of modern WebGIS.
Geospatial Web Services are the driving force behind the transformation of GIS applications from closed systems to open, loosely coupled architectures.
It is an important form of building components of geo-converged applications and providing services for cloud GIS.
It is the foundation of the next generation spatial data infrastructure and provides a collaborative way based on geographic information.
Governments and enterprises can provide their data and functions as Web services and build an ecosystem of Web services.
On this basis, a large number of applications with new value can be conceived.
This form of mutual cooperation can maximize the social benefits of investment in the field of geospatial.
