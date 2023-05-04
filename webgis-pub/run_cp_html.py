from shutil import copytree, ignore_patterns


inws = './webgis-src'
outws = './_build/html'

copytree(inws, outws, 
                ignore=ignore_patterns('*.py', '*.pyc', '*.rst', '*.jinja2', '.idea', '*.png', '*.jpg', '*.pdf', '*.md', '*.rstx', '*.jpeg', '*.txt')
                )