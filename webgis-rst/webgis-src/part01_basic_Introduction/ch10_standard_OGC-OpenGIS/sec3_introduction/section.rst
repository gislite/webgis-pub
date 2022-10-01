.. Author: Bu Kun
.. Title: Principle of Geographic Web Service

# Geographic Web service

Web service is a major progress in the development of WebGIS, and it is the core technology and important symbol of modern WebGIS. It combines the advantages of GIS, program components and the Internet, and profoundly changes the way GIS is developed and applied. It bypasses the complex links of local data conversion and local software installation, enables different computer systems and different departments to integrate at the Web service level, provides a new basic module for software application development, and a new way for cross-departmental coordination and cooperation, provide a technical framework for the National Spatial Data Infrastructure (NSDI).

More and more organizations are publishing and sharing their own data and functions as Web services for their own organization and often other organizations. These services can then be combined into other WebGIS applications.

Focus on the basics of web services, including the concept, impact, role and advantages of web services, SOAP and REST-style web services, web services related standards such as WMS, WFS, WCS, CSW, GML, KML and GeoRSS, and Optimization of Web Services.

## From Web site to Web service


### Emergence and advantages of Web Service

WebGIS developed rapidly after its emergence in the early 1990s, but the early Web application systems and software, including WebGIS, were mostly websites that could only be used independently. This system gradually shows its limitations in both internal structure and external opening, and it is difficult to give full play to the potential of WebGIS.

> Limitation 1
>
> Lacks of good interoperability between systems,each WebGIS is an isolated and closed system, different systems cannot call each other's functions and share information, and cannot interoperate.
> Suppose that a certain function of system A is exactly what system B needs, but because system A is closed and does not provide a Web-based programming interface,
neither the client or the server of system B can call the functions of system A. And vice versa, system A cannot call system B either.

> Limitation 2

> The internal coupling of the system is strong, and the application mode is not flexible enough. Each system is opened as an “independent solution”, the interface between the various modules in the system is tight and local.
> When the system needs to be improved, this highly coupled structure is expensive in source program changes and system maintenance, and is not flexible enough.

With the development of the information society, more and more practical applications need to call, combine, or nest the functions and information provided by other WebGIS systems. Therefore, how to make WebGIS open so that different systems can communicate with each other call becomes very important. 

In the late 1990s, this was not only the problem and demand faced by the WebGIS field, but also the demand of the entire information technology industry. At that time, Microsoft, Oracle, IBM, World Wide Web Consortium (W3C) and other institutions all launched explorations in this area, research and release Web service technology.

In recent years, the technology of web services has continued to improve, and its definition has also changed. The definitions of early Web services mostly involve SOAP, XML and WSDL technologies. Now SOAP is no longer the only way to implement Web services. REST-style Web services extend the concept of Web services.

A web service is a program running on a web server that has a programming interface that can be invoked by other programs via Internet protocols (mainly HTTP). Web services technology represents an important advance in distributed computing, which replaces functions on a local computer with functions on a remote server.

Web services can be understood this way: desktop software consists of a series of co-running local programs, which are assumed to be distributed and run on different Web servers, but still able to communicate with each other and work as a whole - this is the original intention of Web services.

A comparison of web pages and web services helps to understand web services. Web services are different from normal web pages:

- A web page is for human understanding and reading, mainly in HTML format, it contains content and style (font size and color, page layout...), etc.
 
- A Web service is a Web-based programming component that is invoked by client computer programs.
    Its results are mainly in a format that can be automatically parsed by computer programs such as XML or JSON, rather than directly readable by humans.

The complete Web service system has three parts: provider, user and portal. The service provider and the user do not have to be aware of each other's existence. 
Providers can register their Web service information in the portal, and users can query the portal, find the services they need, and then use these services (below).

![Three components of Web Service system and their relationship](imgvze23.png)

Web services inherit the characteristics of both Web programs and development interfaces. Compared with traditional computing methods, Web services have the following advantages:

(1) Openness

Web services can interact with other computer software on the Web for other systems to call, exchange and share functions and information, breaking the limitations of isolated and closed early Web applications.

(2) Independent of programming language and operating system

The Web service is based on the Web platform and is called remotely using the HTTP protocol. It is not compiled with the client program that invokes it. 

A web service no matter what programming language is used (such as Java, .NET or C++, etc.), what operating system is deployed on (such as Windows, Linux or MacOS, etc.), and what kind of web application server ( such as IIS or Apache/Tomcat, etc.), can be called by the client in the same way. 
The client is not bound to any programming language when calling a Web service, and developers can freely choose a development language such as .NET, Java, Python, JavaScript, Flex or Silverlight.

(3) Loosely coupled integratability

The client software and the Web service it calls do not have to run on one machine, and the two do not necessarily depend on each other to exist.

When a client is dissatisfied with a Web service or the Web service cannot be used, the client can replace it with other Web services. 

As long as the interfaces of the two Web services are the same, the client only needs to point to the URL of the new Web service, and no other changes are required. 

From the perspective of the Web service provider, which can change or update the Web service, such as migrating from J2EE to .NET or vice versa. As long as the interface of the Web service remains unchanged, these changes are transparent to the caller. It does not need to make any changes (Chai Xiaolu, 2002). The loosely coupled feature facilitates flexible combination and nesting to meet user business needs.

(4) Uniformity of releases and updates

When a web service is updated or a new version is released, it only needs to be updated on the server side, and each client program calls the latest web service, so it is not necessary to install and update the software package separately on each client. This is an important aspect of Web services over desktop component technology.

## Impact of Geospatial Web Services


At present, Web service has become the core of GIS, and its appearance has had a great impact on the geospatial industry, providing an excellent solution for the realization of geospatial information sharing, interoperability and cross-department collaboration.

(1) It is an accelerator for WebGIS product differentiation and new market formation

With web services as the center, the geographic information community has released new products or new functions to realize a series of workflow such as the production of Geographic Resources (author), the publication of services (publish), the discovery and use of services.

![Web service is the core of WebGIS. WebGIS products are divided into a variety of products that support the creation, distribution, registration, query and use of geospatial Web services.](imgvze24.png)

On the server side: if you have a lot of data, you can be a provider of data and map services. If you have unique analytical models, you can publish them as professional geoprocessing services. These services can be free or pay-per-use.

On the client side: If you are good at development, you can choose to develop a desktop client or a mobile client for Web services, showing your advantages in terms of supported service types or availability.
 
In the aspect of portal website: you can collect certain areas, certain topics or Web services that meet certain standards, catalogue and publish these information, and allow people who need these services to query.

(2) It is the basic component of GIS integration into mainstream information systems

Before geographic Web services, the integration of GIS and other information systems was often implemented “locally”, that is, the geographic data was copied to the local, the GIS software was installed locally, and the invocation of GIS functions was very complicated and limited. These reasons have limited GIS to a small circle for many years, hindering the seamless integration of GIS with mainstream information systems. 

Geographic Web services hide the above-mentioned complexities, and other information systems, such as enterprise resource planning (ERP) and customer relationship management (CRM) systems, can flexibly and easily invoke and integrate remote geographic Web services to obtain maps, data and geographic Analysis function. The openness and flexibility of Web services will greatly expand the market of GIS.

(3) It is a new way to achieve interoperability

One of the challenges of GIS application is how to realize interoperability, that is, to make the products of different GIS software manufacturers work together.
Before web service technology, interoperability was mainly completed at the data format level, that is, the exchange format formulated by the standard organization was adopted.

Software from different manufacturers needs to be able to input and output these formats or directly read and write these data formats.

This method often involves data replication and local software installation, which is disjointed and inflexible.

Web services enable the GIS community to elevate interoperability to a Web services-based level, go beyond data transformation and installation of transformation tools at these levels (Bacharach, 2005). Geographic information standards bodies, such as the Open Geospatial Consortium (OGC) and the International Organization for Standardization (ISO), have kept pace with the times and have developed a series of Web service standards. 

Strictly following these standards, servers and clients of different manufacturers can be used interchangeably, without having to consider which company's products released these services, or which company's clients are using these services.

(4) It is an important framework for realizing spatial data infrastructure

Spatial Data Infrastructure (SDI) refers to the general term for the technologies, policies, standards and human resources necessary for the collection, processing, storage, distribution, utilization and protection of geographic information. 
The keys to building regional, national, and global space infrastructure are standards, sharing, collaboration, and coordination.

The Web service system establishes a dynamic communication and integration method between service providers and information users, which is the key to building space infrastructure. 

Geographic data and other information can keep the data in the original unit, and they can maintain the data and share it through Web services. When the data is updated, the Web services are also updated, which ensures the current status of Web services. 

For example, a local government can continuously maintain and update its land records, while sharing this information with other units through Web services. 
A public utility department can directly use this map service as a basemap without having to copy and install the original data of its map locally. 

On the other hand, this public facilities department can also share its infrastructure information with other government departments in the form of Web services, so that the municipal government can use the information for business needs such as land use planning and approval. This collaborative approach provides a new, flexible technical framework for geographic information sharing and collaboration among different institutions (Dangermond, 2008).

## Features of Geographic Web Services

Geographic Web services can be divided into several categories such as map services, data services, analysis services and metadata services according to their functions. This section describes the capabilities of these service types.

### Map and Feature Services

Map services are the most common form of geographic Web service. It allows the client to request a map within a certain geographic range, and it returns the map to the client in an image format such as JPEG, PNG or GIF.

Maps for a map service can be dynamically made or pre-made tiles. Tile map service can greatly improve the operating efficiency of WebGIS applications and shorten the response time. It is mainly used for basic basemaps or maps with relatively static content or low update frequency.

After receiving the request from the client, the dynamic map service reads data from the database in real time to make a map, so it is especially suitable for maps with high data update frequency. 

Map services can be two-dimensional or three-dimensional. The 3D map service, also known as the Globe service, can use the ground elevation as the third dimension to show the natural terrain; it can also use the height of the building as the third dimension, add the texture model of the building surface, to express the outline of the city or the realistic street scene; 3D map Services can present topographical and urban architectural landscapes.

You can also use the value of an attribute field as a third dimension to highlight the topic. A 3D map service can also use the value of an attribute as a third dimension, highlighting the subject expressed by that attribute.

The 3D map service needs to be displayed in the 3D client, and the user can perform operations such as zooming and rotating. 

In addition to cartography, map services can often support functions such as attribute query, spatial query, and dynamic projection transformation.

Feature service allows the web client to read and write vector geographic data in the server-side geographic database, and can add, edit and delete geographic features and their coordinates in the database.

As shown in the figure, citizens can mark on the map website to indicate when and where they have found endangered birds and provide relevant information. This information is stored in the server-side geographic database to facilitate government departments to delimit ecological reserves.

Feature services allow designers to quickly sketch designs on digital maps and share their plans at the same time, allowing other colleagues to revise them, effectively supporting collaborative geographic design. Feature services also make it easier for the public to mark on web maps and share what they see and hear,

Promote public participation in the development of geographic information systems (PPGIS) and spontaneous geographic information.

The search service can index the content of GIS resources (for example, a data layer or the entire enterprise geodatabase), and allow Web users to search for the GIS resources they need by querying keywords and other methods.

The search service is different from the metadata catalog service that will be introduced later in this section. Although both can support the search and discovery of GIS resources, the former indexes the geographic data itself, especially the attribute table, while the metadata catalog service relies on the Metadata for geographic data.

Image services mainly provide raster data (such as remote sensing imagery and digital elevation) through Web services. It supports extraction, download and map making of raster data. 

For example, MapServer allows remote sensing departments to publish a large number of acquired images as image services without preprocessing, and can perform rapid real-time processing, including splicing, enhancing and deriving a variety of image products for Web clients to browse and download.

### Analysis service

Geocoding Services: Geocoding is the process of converting street addresses into geographic coordinates. 

Reverse geocoding is a process of converting geographic coordinates into corresponding addresses. A geocoding service is to publish a geocoding or reverse geocoding function in the form of a web. 

Currently, there are many free geocoding services available online, such as those provided by ArcGIS Online, Google, Microsoft, and others. In some cases, such as where address data in free systems such as Google is outdated or you want to be able to match by address aliases known to locals, you can create your own geocoding service using products such as ArcGIS Sever.

Network analysis service: Geographical network here refers to the transportation network such as streets and highways, the pipeline network organized by underground pipelines, pipeline joints, valve switches, etc.

The web analytics service can provide the following functions:

1. Calculate the best path: Given a starting point and ending point, calculate the shortest or fastest path from the starting point to the ending point, or given multiple stops, calculate the shortest or fastest path that can travel through them. Routing services should take into account speed limits and turning rules, as well as factors such as traffic congestion, wait times at traffic lights, and road closures (due to construction or accidents).

2. Calculate the service area: Calculate the blocks that can be reached from a certain point or points within a certain driving time. Service area analysis can help users assess the coverage or accessibility of a location, for example, it can help city planners choose the best fire station location so that it can cover a specified area in minutes, or help retailers choose the best location. the best store address so that it can serve more potential customers.

3. Find the nearest facility: Find the facility that is closest to a point or with the least driving time. This is commonly used in location-based services (LBS), such as finding the nearest restaurant or post office to a cell phone user.

4. Geometric service: It can perform geometric transformation, buffer calculation, cartographic synthesis (element simplification), merging and cutting of geographic elements, calculation of area and length, and coordinate projection transformation.

5. Geoprocessing services: Geoprocessing services can publish a variety of user-created functions and analytical models as Web services. 

Geoprocessing services can perform functions ranging from simple buffer analysis and polygon overlay analysis to complex regression analysis and image classification, from local community planning to global climate change analysis, from modeling the past to predicting the future.

### Metadata Directory Service


Metadata is data about data that can describe GIS data and services. 

Metadata catalog services can be used to publish and search metadata, facilitating the sharing of geographic information and services. 

For example, a provider can publish metadata about their data and services, and a user can query this metadata service to find data and services that meet their needs.

## Interface types for web services


This section describes the two main interface types for web services, SOAP-style web services and REST-style web services, which are also known as SOAP API and REST API. 

It should be emphasized that Web services are not limited to these two types. Those Web programs that transmit formatted data through HTTP should be considered as Web services.

### SOAP-style web services

The original name of SOAP is Simple Object Access Protocol, which uses an encapsulated XML for information exchange. 
In 2003, it was adopted by the World Wide Web Consortium as a Recommended Standard. The full name "Simple Object Access Protocol" was thought to be misleading, so the World Wide Web Consortium gave up the full name in 2007, and now people just use the acronym SOAP. 

SOAP-style Web services use HTTP Post and SOAP-encapsulated XML to send requests and deliver results between client and server.

![SOAP-based Web services rely on HTTP Post and SOAP encapsulated XML to send requests and pass results between the client and the server](imgvze28.png)

SOAP-based Web services encapsulate the XML message body in another XML document. This "XML-in-XML" format is inconvenient for people to manually create SOAP requests and parse SOAP results, so it is difficult to invoke SOAP services. Of course, there are tools to simplify the invocation of SOAP services. SOAP-based Web services generally have WSDL (Web Service Description Language), that is, Web Service Description Language. 

It describes the specific programming interface provided by a Web service in XML format, which is convenient for developers to understand and use this Web service.

### REST-style Web Services

REST (representational state transfer) is an architectural style proposed by Roy Fielding in his doctoral dissertation in 2000. Roy Fielding has participated in the formulation of the HTTP specification. He believes that SOAP does not make full use of the advantages of HTTP. The REST-style architecture he proposed can give full play to the advantages of HTTP, reduce the complexity of development, and improve the scalability of the system (Richardson and Ruby, 2007). 

When REST was first proposed, it did not get much attention. Its concepts and principles are relatively abstract, and different people have different interpretations. It has not been fully followed or implemented in practical applications. 

REST-style web services send data over HTTP, and the information sent is not encapsulated in SOAP. The most common implementation is to put the request parameters in the URL and send the request parameters through the URL. RESTful web services often return results to clients in JSON and XML without SOAP. 

The following figure shows the same function in the above figure in the form of REST. It can be seen that the REST interface is more concise than the SOAP interface.

![Services of the REST interface](imgvze30.png)

<!--
.. Figure::. / imgvze31.png
.. Figure::. / imgvze32.png
-->
    

It can be seen that the URL hierarchy of this directory structure is intuitive, predictable, and easy to understand, without requiring excessive documentation, and developers can easily construct these URLs to point to the web resources they need.

Web resources in REST services support specific operations. For example, a map service can perform mapping and query operations, and a single data layer in a map service can perform query operations. 

The results of these operations can be returned to the client in formats such as JSON. For example, to request a map service to make a map of the United States through the REST interface, and to return a JPEG image of ``800x500`` pixels, the URL request is roughly


    http://server.mycompany.com/ArcGIS/rest/services/QSMap/MapServer/
    export?
    bbox=-185.33, 15.20, -9 .53 , 74 .08
    &size=800 , 500
    &format=jpg
    &dpi=96
    &f=image

Using REST to query the median household income of each county in California in a map service, the request returns JSON format, and the URL request is roughly:

    http://server.mycoinpany.com/ArcGIS/rest/services/USMap/MapServer/0/query?where=STATE_NAME='California'&OutFields=MEDHINC_CY&f=pjson

It can be seen that basically all requests in REST are a URL, which is easier to understand. 

You can use many programming languages such as .NET, Java JavaScript, and Flex to generate the URL string and send the URL request. 

You can even put this URL directly into your web browser without programming, and you can see the results you want, such as the map. Therefore, REST is considered to be “The command line of the web”.

## Comparison between SOAP and REST


The following compares SOAP and REST types of web services. SOAP-type Web services are produced early, and the related technologies are relatively mature and widely used. The interface definitions are clear and rigorous, and the development environment supports them highly. 

But it is too complicated, and the programming workload and difficulty are large; it does not make full use of the advantages of HTTP, and the transmission efficiency is low; 

The encapsulation of SOAP makes the transmitted XML complex and huge, which often reduces the efficiency of information transmission and parsing and even the performance of the entire system. 

Given these realizations, people have gradually turned to REST-style web services, which are simple and efficient (Cappelaere et al., 2007). In many cases, the simplicity and efficiency of REST outweighs the rigor that comes with adopting SOAP (Fu et al., 2008).

Comparing SOAP type web services and REST type web services 

SOAP type web service    

- Transmission mode, HTTP POST
- Request parameters, placed in XML and encapsulated in SOAP
- The response result is put in XML and encapsulated in SOAP
- Advantages, early, mature, rigorous interface, powerful function
- Disadvantages, heavy, complex, high threshold; SOAP encapsulated XML information transmission efficiency and analysis efficiency is low; can not make full use of the advantages of HTTP, not rigorous enough, slightly casual.


Web services of type REST
                                            
- The main reason is that although HTTP GET; defines the semantics and usage of PUT, P0ST and DELETE, it is rarely used
- Parameters (key-value pairs) are generally placed in URL
- There are a variety of JSON, XML (not SOAP encapsulated) and binary file streams, etc.
- Light, simple, high efficiency, can make full use of Web cache and other advantages, and gradually widely used
- For service providers, it can reduce the cost of creating services and the cost of service hosting
- For developers who do application development based on Web services, it can reduce the difficulty, shorten the learning time, speed up the development speed and reduce the development cost.
- For managers, REST provides a better system architecture, which can obtain higher system response speed, higher reliability and scalability.

