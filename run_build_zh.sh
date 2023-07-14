
make gettext

sphinx-intl update -p _build/gettext -d webgis-src/locales -l zh

make -e SPHINXOPTS="-Dlanguage='zh'" html