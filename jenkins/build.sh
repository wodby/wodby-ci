#!/bin/bash

set -eo pipefail

# Install merge plugin.
composer update --no-interaction

# Install all requirements.
composer update --no-interaction
