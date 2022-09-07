#!/bin/bash

git add .
git commit -a -m 'mark'
git pull
git push
/xpy/bin/python3 deploy_webgis.py
