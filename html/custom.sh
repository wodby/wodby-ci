#!/usr/bin/env bash

# The following example
# 1. Installs your dependencies from package.json
# 2. Runs build
# 3. Builds and pushes a docker image (HTTP server) with contents of the build (./build)
# 4. Deploys this image to your HTML app instance

wget -qO- https://api.wodby.com/api/v1/get/cli | sh
wodby ci init $WODBY_INSTANCE_UUID
wodby ci run -i wodby/node:8 -- yarn install
wodby ci run -i wodby/node:8 -- yarn run build
wodby ci build --from ./build
wodby ci release
wodby ci deploy