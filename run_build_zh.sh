
make gettext

sphinx-intl update -p _build/gettext -d pyqgis-src/locales -l zh

make -e SPHINXOPTS="-Dlanguage='zh'" html