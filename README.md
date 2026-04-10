# Wodby CI

The following examples ought to help you set up CI/CD workflows on Wodby 2.0 using Wodby CI and third-party CI providers.

For Wodby 1.0 please see [1.0 branch](https://github.com/wodby/wodby-ci/tree/1.0).

See full documentation on Wodby CI at https://wodby.com/docs/2.0/cicd/wodby-ci.

## Examples

### PHP app

The following examples are for a simple PHP stack:

1. Installs your composer dependencies from `composer.json`
2. Builds docker images for php and nginx services with contents of the current directory `./` (optionally you can specify docroot directory for nginx image to omit `vendor` directory)
3. Caches contents of `~/.composer` directory and restores during the next build based on `composer.lock` checksum
4. Pushes images to associated docker registry (Wodby registry by default)
5. Triggers deployment of the new build to your app instance

Available providers:

* Wodby CI (default):
  put these files inside the `.wodby` directory of your git repository:
  [`.wodby/pipeline.yml`](php/wodby/pipeline.yml),
  [`.wodby/post-deployment.yml`](php/wodby/post-deployment.yml) (optional)
* GitHub Actions:
  put [`.github/workflows/wodby.yml`](php/github-actions/wodby.yml) in the root of your git repository and configure `WODBY_API_KEY` and `WODBY_APP_SERVICE_ID` repository secrets.
* GitLab CI:
  uses the docker-in-docker method.
  Put [`.gitlab-ci.yml`](php/gitlab-ci/.gitlab-ci.yml) in the root of your git repository.
* CircleCI:
  put [`.circleci/config.yml`](php/circleci/config.yml) in the root of your git repository.

### Node app

The following examples are for a simple Node stack:

1. Installs your node dependencies from `package.json`
2. Builds docker images for node service with contents of the current directory `./`
3. Caches contents of `~/.npm` directory and restores during the next build based on `package-lock.json` checksum
4. Pushes images to associated docker registry (Wodby registry by default)
5. Triggers deployment of the new build to your app instance

Available providers:

* Wodby CI (default):
  put these files inside the `.wodby` directory of your git repository:
  [`.wodby/pipeline.yml`](node/wodby/pipeline.yml),
  [`.wodby/post-deployment.yml`](node/wodby/post-deployment.yml) (optional)
* GitHub Actions:
  put [`.github/workflows/wodby.yml`](node/github-actions/wodby.yml) in the root of your git repository and configure `WODBY_API_KEY` and `WODBY_APP_SERVICE_ID` repository secrets.
* GitLab CI:
  uses the docker-in-docker method.
  Put [`.gitlab-ci.yml`](node/gitlab-ci/.gitlab-ci.yml) in the root of your git repository.
* CircleCI:
  put [`.circleci/config.yml`](node/circleci/config.yml) in the root of your git repository.

## Boilerplates

You can also find boilerplate for build templates for the following stacks: 

- [PHP](https://github.com/wodby/php-package-boilerplate)
- [Drupal Vanilla](https://github.com/wodby/drupal-vanilla)
- [Drupal CMS](https://github.com/wodby/drupal-cms-template)
- [WordPress Vanilla](https://github.com/wodby/wordpress-vanilla)
- [Next.js](https://github.com/wodby/nextjs-boilerplate)
- [Node.js (Express.js)](https://github.com/wodby/expressjs-boilerplate)
- [React](https://github.com/wodby/react-boilerplate)

## Third-party CI

You can use Wodby 2.0 with third-party CI services like GitHub Actions, GitLab CI, CircleCI, etc. by using Wodby CLI.

The GitHub Actions examples in this repository use [`wodby/actions/setup-wodby-cli`](https://github.com/wodby/actions/tree/main/setup-wodby-cli) on GitHub-hosted Ubuntu runners.

You can also use any custom CI provider in a similar way with [Wodby CLI](https://github.com/wodby/wodby-cli).

GitLab CI examples in this repository use the docker-in-docker method.

For providers that support it, we recommend using a VM-based environment over a docker-based environment to avoid issues related to docker-in-docker in the build process, since we are building docker images. The CircleCI examples in this repository use the machine executor for that reason.

## Custom Dockerfile

You can use custom Dockerfile to build your services. Just specify the path to your Dockerfile `-f Dockerfile` in the pipeline configuration.
