# Examples 

The following examples ought to help you set up CI/CD workflow on Wodby.

See full documentation on CI/CD workflow at https://wodby.com/docs/apps/deploy/#cicd

## Dependency caches

Wodby CLI automatically configures npm, Composer, Bundler, and uv caches for supported Wodby and official images.
Native Docker environments use the package managers' conventional user cache paths. Docker-in-Docker jobs stage
persistent data under `.wodby-ci-cache/<profile>` in the CI context, import it into their cache volume during
`wodby ci init`, and export it after each cache-enabled `wodby ci run`.

Use `--cache` to select a profile explicitly for another image or `--no-cache` to disable automatic caching.

## Third-party CI

### Next.js app

The following example is for custom Next.js stack:
1. Installs your dependencies from `package.json`
2. Builds and pushes default images with contents of the current directory `./`
3. Deploys build to your app instance

Example files:

* GitHub Actions: [`.github/workflows/workflow.yml`](nextjs/github.yml)
* Stack template: [`stack.yml`](nextjs/stack.yml) to create custom stack
* Dockerfile to build nextjs app: [`Dockerfile`](nextjs/Dockerfile), put in your git repository root

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
* GitLab CI: [`.gitlab-ci.yml`](php/gitlab.yml)
* BitBucket pipelines: [`bitbucket-pipelines.yml`](php/bitbucket.yml)
* Custom shell script: [`custom.sh`](php/custom.sh)
