# Examples 

The following examples ought to help you set up CI/CD workflow on Wodby.

See full documentation on CI/CD workflow at https://wodby.com/docs/apps/deploy/#cicd

## Third-party CI

### Static HTML with node

The following example is for managed HTML stack:
1. Installs your dependencies from `package.json`
2. Runs build
3. Builds and pushes a docker image (HTTP server) with contents of `./build`
4. Deploys this image to your HTML app instance

Example files:

* GitHub Actions: [`.github/workflows/workflow.yml`](html/github.yml)
* CircleCI: [`.circleci/config.yml`](html/circleci.yml)
* TravisCI: [`.travis.yml`](html/travis.yml)
* BitBucket pipelines: [`bitbucket-pipelines.yml`](html/bitbucket.yml)
* Custom shell script: [`custom.sh`](html/custom.sh)

### Composer-based PHP app

The following example is for managed PHP-based stacks (Drupal, WordPress, Generic PHP):
1. Installs your dependencies from `composer.json`
2. Builds and pushes default images with contents of the current directory `./`
3. Deploys build to your app instance

Example files:

* GitHub Actions: [`.github/workflows/workflow.yml`](php/github.yml)
* CircleCI: [`.circleci/config.yml`](php/circleci.yml)
* TravisCI: [`.travis.yml`](php/travis.yml)
* BitBucket pipelines: [`bitbucket-pipelines.yml`](php/bitbucket.yml)
* Custom shell script: [`custom.sh`](php/custom.sh)

## Wodby CI 

Coming soon...
