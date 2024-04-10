make gettext
sphinx-intl update -p _build/gettext  -d xx_rst/locales -l zh

make -e SPHINXOPTS="-Dlanguage='zh'" html

