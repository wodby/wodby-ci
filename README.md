# Wodby CI

Copyable CI/CD examples for Wodby 2.0, covering Wodby CI, GitHub Actions, GitLab CI, and CircleCI.

For Wodby 1.0, see the [1.0 branch](https://github.com/wodby/wodby-ci/tree/1.0). The complete Wodby CI reference is in the
[Wodby documentation](https://wodby.com/docs/2.0/cicd/wodby-ci).

## Choose an example

The full provider matrices cover the reusable build patterns shared by most application stacks.

| Build pattern | Wodby CI | GitHub Actions | GitLab CI | CircleCI | Post-deployment |
| --- | --- | --- | --- | --- | --- |
| PHP multi-image | [Pipeline](php/wodby/pipeline.yml) | [Workflow](php/github-actions/wodby.yml) | [Pipeline](php/gitlab-ci/.gitlab-ci.yml) | [Config](php/circleci/config.yml) | [Runtime check](php/wodby/post-deployment.yml) |
| Node.js server | [Pipeline](node/wodby/pipeline.yml) | [Workflow](node/github-actions/wodby.yml) | [Pipeline](node/gitlab-ci/.gitlab-ci.yml) | [Config](node/circleci/config.yml) | [Runtime check](node/wodby/post-deployment.yml) |
| Static frontend to Nginx | [Pipeline](static/wodby/pipeline.yml) | [Workflow](static/github-actions/wodby.yml) | [Pipeline](static/gitlab-ci/.gitlab-ci.yml) | [Config](static/circleci/config.yml) | [Nginx check](static/wodby/post-deployment.yml) |
| Python custom Dockerfile | [Pipeline](python/wodby/pipeline.yml) | [Workflow](python/github-actions/wodby.yml) | [Pipeline](python/gitlab-ci/.gitlab-ci.yml) | [Config](python/circleci/config.yml) | [Application check](python/wodby/post-deployment.yml) |

The static example expects `npm run build` to write to `dist`. Change `--from dist` when the framework uses a different
output directory. The Python example follows the
[Python boilerplate](https://github.com/wodby/python-boilerplate) conventions: `uv.lock`, `pytest`, `Dockerfile`, and
the `python_boilerplate` package.

## Stack-specific Wodby CI recipes

These recipes add framework-specific build commands and safe post-deployment checks without duplicating every
third-party provider wrapper.

Laravel queue and Rails Sidekiq are service derivatives of their main runtimes. Their recipes build the application
image once; the stack reuses that image for the corresponding worker service.

| Stack | Pipeline | Post-deployment | Boilerplate or source template |
| --- | --- | --- | --- |
| Drupal | [Pipeline](drupal/wodby/pipeline.yml) | [`drush status`](drupal/wodby/post-deployment.yml) | [Drupal Vanilla](https://github.com/wodby/drupal-vanilla) or [Drupal CMS](https://github.com/wodby/drupal-cms-template) |
| WordPress | [Pipeline](wordpress/wodby/pipeline.yml) | [WP-CLI check](wordpress/wodby/post-deployment.yml) | [WordPress Vanilla](https://github.com/wodby/wordpress-vanilla) |
| Laravel | [Pipeline](laravel/wodby/pipeline.yml) | [Artisan check](laravel/wodby/post-deployment.yml) | [Laravel](https://github.com/laravel/laravel) |
| Matomo | [Pipeline](matomo/wodby/pipeline.yml) | [Console check](matomo/wodby/post-deployment.yml) | [Matomo](https://github.com/matomo-org/matomo) |
| Django | [Pipeline](django/wodby/pipeline.yml) | [System check](django/wodby/post-deployment.yml) | [Django boilerplate](https://github.com/wodby/django-boilerplate) |
| Rails | [Pipeline](rails/wodby/pipeline.yml) | [Application check](rails/wodby/post-deployment.yml) | [Rails boilerplate](https://github.com/wodby/rails-boilerplate) |
| Go | [Pipeline](go/wodby/pipeline.yml) | [Health check](go/wodby/post-deployment.yml) | [Go boilerplate](https://github.com/wodby/go-boilerplate) |
| Next.js | [Pipeline](nextjs/wodby/pipeline.yml) | [Application check](nextjs/wodby/post-deployment.yml) | [Next.js boilerplate](https://github.com/wodby/nextjs-boilerplate) |

Post-deployment jobs should be safe to retry. Use them for smoke checks and idempotent application operations, and
remember that a post-deployment failure is reported separately from the completed deployment.

## Application stack coverage

| Application stack | Recommended example |
| --- | --- |
| HTML | Static frontend to Nginx |
| PHP | PHP multi-image |
| Drupal | Drupal recipe |
| WordPress | WordPress recipe |
| Laravel | Laravel recipe |
| Matomo | Matomo recipe |
| Python | Python custom Dockerfile |
| Django | Django recipe |
| FastAPI | Python custom Dockerfile and [FastAPI boilerplate](https://github.com/wodby/fastapi-boilerplate) |
| Flask | Python custom Dockerfile and [Flask boilerplate](https://github.com/wodby/flask-boilerplate) |
| Ruby | Custom Dockerfile pattern and [Ruby boilerplate](https://github.com/wodby/ruby-boilerplate) |
| Rails | Rails recipe |
| Go | Go recipe |
| Node.js | Node.js server |
| Next.js | Next.js recipe |
| Dagster | No source-build example; the current catalog service deploys a packaged image |

Database, messaging, search, mail, observability, utility, and Kubernetes system stacks are deployable components rather
than customer source-build patterns, so they do not need CI examples here.

## Provider setup

Wodby CI installs Wodby CLI during the `Setting up build environment` step and provides `WODBY_BUILD_ID`. Wodby CI
pipelines therefore start with:

```shell
wodby ci init $WODBY_BUILD_ID
```

Third-party CI providers must install and authenticate Wodby CLI:

- GitHub Actions uses [`wodby/actions/setup-wodby-cli`](https://github.com/wodby/actions/tree/main/setup-wodby-cli).
  Configure `WODBY_API_KEY` as a repository secret and `WODBY_APP_SERVICE_ID` as a repository variable.
- GitLab CI uses `wodby/wodby-cli:2.0` with Docker-in-Docker. Configure `WODBY_API_KEY` as a masked CI/CD variable and
  `WODBY_APP_SERVICE_ID` as a CI/CD variable.
- CircleCI uses a machine executor. Configure `WODBY_API_KEY` and `WODBY_APP_SERVICE_ID` as project environment
  variables.

VM-based executors are preferable when a provider supports them. Container-only executors require
Docker-in-Docker because `wodby ci build` creates Docker images.

## Build behavior

The common pipeline flow is:

1. Initialize the build with `wodby ci init`.
2. Install dependencies or run tests with `wodby ci run`.
3. Build one or more service images with `wodby ci build`.
4. Push the built images with `wodby ci release`.
5. Trigger deployment with `wodby ci deploy`.

If no service is supplied, `wodby ci build` builds all configured image targets. Use a service name to build selectively:

```shell
wodby ci build node
```

For static assets, select the source and destination:

```shell
wodby ci build nginx --from dist --to /var/www/html
```

For a custom Dockerfile:

```shell
wodby ci build python -f Dockerfile
```

See the [CI build documentation](https://wodby.com/docs/2.0/cicd/build) for Dockerfile resolution, build arguments, and
cache backends.

## Boilerplates

- [PHP](https://github.com/wodby/php-package-boilerplate)
- [Drupal Vanilla](https://github.com/wodby/drupal-vanilla)
- [Drupal CMS](https://github.com/wodby/drupal-cms-template)
- [WordPress Vanilla](https://github.com/wodby/wordpress-vanilla)
- [Laravel source template](https://github.com/laravel/laravel)
- [Matomo source template](https://github.com/matomo-org/matomo)
- [Python](https://github.com/wodby/python-boilerplate)
- [Django](https://github.com/wodby/django-boilerplate)
- [FastAPI](https://github.com/wodby/fastapi-boilerplate)
- [Flask](https://github.com/wodby/flask-boilerplate)
- [Ruby](https://github.com/wodby/ruby-boilerplate)
- [Rails](https://github.com/wodby/rails-boilerplate)
- [Go](https://github.com/wodby/go-boilerplate)
- [Node.js (Express.js)](https://github.com/wodby/expressjs-boilerplate)
- [Next.js](https://github.com/wodby/nextjs-boilerplate)
- [React](https://github.com/wodby/react-boilerplate)

## Validation

Run the repository checks with:

```shell
python3 -m pip install -r scripts/requirements.txt
python3 scripts/validate_examples.py
```

The pull-request workflow also runs `actionlint` against the nested GitHub Actions examples and checks README links.
