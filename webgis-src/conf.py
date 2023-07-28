project = 'Open Source WebGIS'
copyright = 'Since 2020'
author = 'gislite'
release = 'v 0.14'

extensions = []

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'sphinx_book_theme'
html_static_path = ['_static']

html_theme_options = {
    'repository_url': 'https://github.com/gislite/webgis-pub',
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/gislite/webgis-pub",  # required
            "icon": "fa-brands fa-square-github",
            "type": "fontawesome",
        },
        {
            "name": "Stars",
            "url": "https://github.com/gislite/webgis-pub",
            "icon": "https://img.shields.io/github/stars/gislite/webgis-pub.svg",
            "type": "url",
        },
        {
            "name": "Forks",
            "url": "https://github.com/gislite/webgis-pub",
            "icon": "https://img.shields.io/github/forks/gislite/webgis-pub.svg",
            "type": "url",
        },

    ]
}

html_logo = "_static/webgis-logo.png"

locale_dirs = ['locales']
gettext_compact = True
