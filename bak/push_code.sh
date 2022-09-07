#!/bin/bash

git add .
git commit -a -m 'mark'
git pull

git submodule foreach git checkout master
git submodule foreach git pull


git push

cd wwwpub
python3 deploy_webgis.py
