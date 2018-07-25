# Examples to help you set up CI/CD workflow on Wodby 

## Third-party CI

### Build node application (managed HTML stack)

The following example
1. Installs your dependencies from `package.json`
2. Runs build
3. Builds and pushes a docker image (HTTP server) with contents of `./build`
4. Deploys this image to your HTML app instance

Example files:

* CircleCI: [`.circleci/config.yml`](html/circleci.yml)
* TravisCI: [`.travis.yml`](html/travis.yml)
* BitBucket pipelines: [`bitbucket-pipelines.yml`](html/bitbucket.yml)
* Custom shell script: [`custom.sh`](html/custom.sh)

### Build composer-based application (managed PHP-based stack)

The following example
1. Installs your dependencies from `composer.json`
2. Builds and pushes default images with contents of the current directory `./`
3. Deploys build to your app instance

Example files:

* CircleCI: [`.circleci/config.yml`](php/circleci.yml)
* TravisCI: [`.travis.yml`](php/travis.yml)
* BitBucket pipelines: [`bitbucket-pipelines.yml`](php/bitbucket.yml)
* Custom shell script: [`custom.sh`](php/custom.sh)

## Wodby CI 

Coming soon...