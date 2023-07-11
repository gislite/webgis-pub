# webgis-pub


This directory is the source codes for //webgis.pub in Sphinx project structure.


## 

The idea of this website is based on https://demo.mapserver.org/tutorial/ and has undergone significant improvements.

Went through a series of refactoring.

1. Rebuild with PHP, using templates.
2. Integrated into TorCMS to serve as dynamic website.
3. Using Python to write the SSG for Mapfile processing, and using Jinja2 for webpage management.
4. Finally using Sphinx for the management of the pages. And keep the scripts for Mapfiles.

Based on MapServer, and would supply WebGIS relevant technologies.

There are a large number of historical legacy issues that need 
to be addressed during the conversion process.
All the pull requests arc welcome.




## Install and setup

Install softwares:



    sudo apt install -y apache2 php7.3 libapache2-mod-fcgid cgi-mapserver \
		mapserver-bin libapache2-mod-php
    sudo a2enmod authnz_fcgi
    sudo a2enmod cgi
    sudo service apache2 restart

Setup using shell:

    sudo ln -s `pwd`/owg /owg
    mkdir /owg/ms_tmp/
    chown -R www-data.www-data /var/www/ms_tmp/


## Deploy note:


Running via Apache2. Run the following code for deployment：

   
    sh build.sh
