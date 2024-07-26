git pull

podman run --rm -it -v `pwd`:/ws node:18-alpine sh -c 'cd /ws && yarn'
podman run --rm -it -v `pwd`:/ws node:18-alpine sh -c 'cd /ws && yarn quasar build'
# podman run --rm -it -p 6792:9000 -v `pwd`:/ws node:18-alpine sh -c 'cd /ws && yarn quasar dev'


cd dist/spa/ && python3 -m http.server 6795

