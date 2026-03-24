# Wodby CI

The following examples ought to help you set up CI/CD workflow on Wodby 2.0 using Wodby CI.

For Wodby 1.0 please see [1.0 branch](https://github.com/wodby/wodby-ci/tree/1.0).

See full documentation on Wodby CI at https://wodby.com/docs/2.0/cicd/wodby-ci.

## Examples

### PHP app

The following example is for simple PHP stack:

1. Installs your composer dependencies from `composer.json`
2. Builds docker images for php and nginx services with contents of the current directory `./` (optionally you can specify docroot directory for nginx image to omit `vendor` directory)
3. Caches contents of `~/.composer` directory and restores during the next build based on `composer.lock` checksum
4. Pushes images to associated docker registry (Wodby registry by default)
5. Triggers deployment of the new build to your app instance

Put the following files inside `.wodby` directory of your git repository that you connected to your PHP app:

* Pipeline: [`.wodby/pipeline.yml`](php/pipeline.yml)
* Post-deployment scripts (optional): [`.wodby/post-deployment.yml`](php/post-deployment.yml)

### Node app

The following example is for simple Node stack:

1. Installs your node dependencies from `package.json`
2. Builds docker images for node service with contents of the current directory `./`
3. Caches contents of `node_modules` directory and restores during the next build based on `package-lock.json` checksum
4. Pushes images to associated docker registry (Wodby registry by default)
5. Triggers deployment of the new build to your app instance

Put the following files inside `.wodby` directory of your git repository that you connected to your Node app:

* Pipeline: [`.wodby/pipeline.yml`](node/pipeline.yml)
* Post-deployment scripts (optional): [`.wodby/post-deployment.yml`](node/post-deployment.yml)

## Boilerplates

You can also find boilerplate for build templates for the following stacks: 

- [Drupal Vanilla](https://github.com/wodby/drupal-vanilla)
- [WordPress Vanilla](https://github.com/wodby/wordpress-vanilla)
- [Next.js](https://github.com/wodby/nextjs-boilerplate)
- [Node.js (Express.js)](https://github.com/wodby/expressjs-boilerplate)
- [React](https://github.com/wodby/react-boilerplate)

## Third-party CI

You can use Wodby 2.0 with third-party CI services like GitHub Actions, GitLab CI, CircleCI, etc. by using Wodby CLI. We recommend using VM-based (over docker-based) environment to avoid issues related to using docker-in-docker in the build process (since we are building docker images).

## Custom Dockerfile

You can use custom Dockerfile to build your services. Just specify the path to your Dockerfile `-f Dockerfile` in the pipeline configuration.
