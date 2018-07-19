#!/usr/bin/env bash

# The following example
# 1. Installs your dependencies from composer.json
# 2. Builds and pushes default images with contents of the current directory (./)
# 3. Deploys build to your app instance

wget -qO- https://api.wodby.com/api/v1/get/cli | sh
wodby ci init $WODBY_INSTANCE_UUID
wodby ci run -v $HOME/.composer:$HOME/.composer -s php -- composer install --prefer-dist -n --no-dev
wodby ci build
wodby ci release
wodby ci deploy
