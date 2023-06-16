make gettext
sphinx-intl update -p _build/gettext -l  zh


make -e SPHINXOPTS="-D language='zh'" html


