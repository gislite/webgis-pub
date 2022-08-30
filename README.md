# webgis-pub

Source Code for website //webgis.pub .




## Install and setup

Install softwares:



    sudo apt install -y apache2 php7.3 libapache2-mod-fcgid cgi-mapserver \
		mapserver-bin libapache2-mod-php
    sudo a2enmod authnz_fcgi
    sudo a2enmod cgi
    sudo service apache2 restart

Fetch the f2elib:



    git clone https://github.com/bukun/torcms_f2elib.git ./static/f2elib


Setup for Apache2:


    # Alias /owg/ "/wegis/"
    <Directory "/owg/">
      AllowOverride None
      Options Indexes FollowSymLinks Multiviews
      Require all granted
    </Directory>

    ScriptAlias /cgi-bin/ /usr/lib/cgi-bin/
    <Directory "/usr/lib/cgi-bin">
        AllowOverride None
        Options +ExecCGI -MultiViews +SymLinksIfOwnerMatch
        Require all granted
    </Directory>



Setup using shell:

    sudo ln -s `pwd`/owg /owg
    mkdir /owg/ms_tmp/
    chown -R www-data.www-data /var/www/ms_tmp/


## Deploy note:


Running via Apache2. Run the following code for deployment：


    cd /home/bk/coding/book_webgis/webgis_cases
    python3 build_site.py
    chown -R www-data.www-data owg/
