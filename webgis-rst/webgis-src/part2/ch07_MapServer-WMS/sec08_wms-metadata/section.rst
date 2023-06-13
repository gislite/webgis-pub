.. Author: Bu Kun .. Title: WMS layer metadata

WMS layer metadata
==================

Introduction
------------

OGC Web services (OWS) can combine with a given resource (WMS layer, WFS
FeatureType, WCS Coverage, SOS ObservationOffering) associated content
metadata is published to the feature document as a reference to a given
URL (i.e. an ISO metadata XML document).

MapServer supports both inline (e.g. ``wms_title`` , ``wms_abstract`` )
and URL-based (e.g. ``wms_metadataurl_href`` ) metadata publishing for
OWS functions.

MapServer OGC Service Capabilities Formal XML metadata in XML provides
value to directory services, which collect metadata to support
discovery.

MapServer 7.2 adds support for dynamic publishing of XML metadata to all
OGC web services to advertise formal layer metadata.

WMS layer metadata technical details
------------------------------------

If a layer does not pass ``ows_metadataurl_*`` metadata, MapServer
provides the metadata URL link (ie WMS MetadataURL ) in the OGC function
XML. The URL itself points to MapServer’s GetMetadata API. example:

::

   <MetadataURL type="TC211">
     <Format>text/xml</Format>
     <OnlineResource xmlns:xlink="http://www.w3.org/1999/xlink" xlink:type="simple" xlink:href="http://localhost/path/to/ows?request=GetMetadata&amp;layer=road"/>
   </MetadataURL>

Supported metadata formats
~~~~~~~~~~~~~~~~~~~~~~~~~~

MapServer’s layer API supports the ISO 19115 ISO 2003 geospatial
standard.

Graph metadata API
~~~~~~~~~~~~~~~~~~

The Layer Metadata API provides formal metadata for any layer object in
a Mapfile, with metadata values (title, abstract, keywords, spatial
attributes) derived from the Mapfile layer object definition. The
metadata response contains useful information (title, abstract,
keywords), and access links to related services (WMS, WFS, etc.).

API supports two parameters:

::

   request GetMetadata
   layer（Mandatory ）：single-level name value

Missing parameters will result in OGC ogc:ExceptionReport XML.

Request instance

::

   http://localhost/path/to/ows?request=GetMetadata&amp;layer=road

Support for layer metadata through CGI
