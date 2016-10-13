#!/bin/bash

set -eo pipefail

######################################################################
#  Archive as tarball and upload to AWS S3
######################################################################
echo "Archiving as tarball and uploading to AWS S3..."

tar -c \
    --exclude='.git' \
    . | gzip | aws s3 cp - "s3://$AWS_S3_BUCKET/$AWS_S3_FILE_NAME-$BUILD_NUMBER.tar.gz"

echo "Archiving and uploading complete..."

######################################################################
#  Create new application instance and import a tarball from AWS S3.
######################################################################
echo "Creating new application instance and importing tarball..."

docker run --rm \
    -v "$HOME/.composer":/composer \
    -v "$PWD/scripts":/app \
    composer/composer:alpine update -n

docker run --rm \
    -v "$PWD/scripts":/app \
    -w /app \
    -e WODBY_API_TOKEN="$WODBY_API_TOKEN" \
    -e WODBY_APP_ID="$WODBY_APP_ID" \
    -e WODBY_SERVER_ID="$WODBY_SERVER_ID" \
    -e WODBY_SOURCE_INSTANCE_ID="$WODBY_SOURCE_INSTANCE_ID" \
    -e AWS_S3_BUCKET="$AWS_S3_BUCKET" \
    -e AWS_S3_FILE_NAME="$AWS_S3_FILE_NAME" \
    -e JOB_NAME="$JOB_NAME" \
    -e JOB_URL="$JOB_URL" \
    -e BUILD_NUMBER="$BUILD_NUMBER" \
    -e BUILD_URL="$BUILD_URL" \
    -e GIT_BRANCH="$GIT_BRANCH" \
    -e GIT_COMMIT="$GIT_COMMIT" \
    php:alpine php deploy-new-instance.php

echo "New application instance created."

######################################################################
#  Cleanup
######################################################################
sudo rm -rf \
    ./scripts/vendor \
    ./scripts/composer.lock
