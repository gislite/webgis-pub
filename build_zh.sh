make gettext
sphinx-intl update -p _build/gettext -l  zh -d webgis-src/locales


make -e SPHINXOPTS="-D language='zh'" html


