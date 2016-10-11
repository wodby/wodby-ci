#!/bin/bash

set -eo pipefail

WORKING_DIR="$WORKSPACE/scripts"

######################################################################
#  Archive as tarball and upload to AWS S3
######################################################################
echo "Archiving as tarball and uploading to AWS S3..."

tar -C "$WORKSPACE" \
	-c \
    --exclude='.git' \
    --exclude='.gitignore' \
    . | gzip | s3cmd --access_key=$AWS_ACCESS_KEY --secret_key=$AWS_SECRET_KEY put - \
    "s3://$AWS_S3_BUCKET/$AWS_S3_FILE_NAME-$BUILD_NUMBER.tar.gz"

echo "Archiving and uploading complete..."

######################################################################
#  Create new application instance and import a tarball from AWS S3.
######################################################################
echo "Creating new application instance and importing tarball..."

# Execute "compose update" twice.
(cd "$WORKING_DIR"; composer update --no-interaction)
php -f "$WORKING_DIR/deploy-new-instance.php"

echo "New application instance created."

######################################################################
#  Cleanup
######################################################################
rm -rf "$WORKING_DIR/vendor" "$WORKING_DIR/composer.lock"
