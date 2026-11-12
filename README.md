# Wodby CI

Copyable CI/CD examples for Wodby 2.0, covering Wodby CI, GitHub Actions, GitLab CI, and CircleCI.

For Wodby 1.0, see the [1.0 branch](https://github.com/wodby/wodby-ci/tree/1.0). The complete Wodby CI reference is in the
[Wodby documentation](https://wodby.com/docs/2.0/cicd/wodby-ci).

Use `wodby ci push` to upload built images, then `wodby ci deploy` to deploy them.
`wodby ci release` remains a compatibility alias for `wodby ci push`. If your installed CLI
does not recognize `push`, upgrade it or continue using `release`.

## Choose an example

Every Wodby build boilerplate has an example here. Each example runs the same build as the boilerplate's
`.wodby/pipeline.yml` and includes Wodby CI, GitHub Actions, GitLab CI, and CircleCI configurations with a
post-deployment check. A repository created from a boilerplate already contains its Wodby CI files. Use these examples
to run that build in another CI provider, or to add Wodby CI to a repository you started yourself.

Commands that name a service, such as `wodby ci build php`, use the service names of the matching Wodby stack. Change
them if your stack names its services differently.

| Application stack | Boilerplate | Wodby CI | GitHub Actions | GitLab CI | CircleCI | Post-deployment |
| --- | --- | --- | --- | --- | --- | --- |
| HTML | [html-boilerplate](https://github.com/wodby/html-boilerplate) | [Pipeline](html/wodby/pipeline.yml) | [Workflow](html/github-actions/wodby.yml) | [Pipeline](html/gitlab-ci/.gitlab-ci.yml) | [Config](html/circleci/config.yml) | [Nginx check](html/wodby/post-deployment.yml) |
| Static frontend to Nginx | None | [Pipeline](static/wodby/pipeline.yml) | [Workflow](static/github-actions/wodby.yml) | [Pipeline](static/gitlab-ci/.gitlab-ci.yml) | [Config](static/circleci/config.yml) | [Nginx check](static/wodby/post-deployment.yml) |
| Angular | [angular-boilerplate](https://github.com/wodby/angular-boilerplate) | [Pipeline](angular/wodby/pipeline.yml) | [Workflow](angular/github-actions/wodby.yml) | [Pipeline](angular/gitlab-ci/.gitlab-ci.yml) | [Config](angular/circleci/config.yml) | [Smoke test](angular/wodby/post-deployment.yml) |
| React | [react-boilerplate](https://github.com/wodby/react-boilerplate) | [Pipeline](react/wodby/pipeline.yml) | [Workflow](react/github-actions/wodby.yml) | [Pipeline](react/gitlab-ci/.gitlab-ci.yml) | [Config](react/circleci/config.yml) | [Smoke test](react/wodby/post-deployment.yml) |
| Vue | [vue-boilerplate](https://github.com/wodby/vue-boilerplate) | [Pipeline](vue/wodby/pipeline.yml) | [Workflow](vue/github-actions/wodby.yml) | [Pipeline](vue/gitlab-ci/.gitlab-ci.yml) | [Config](vue/circleci/config.yml) | [Smoke test](vue/wodby/post-deployment.yml) |
| PHP | [php-package-boilerplate](https://github.com/wodby/php-package-boilerplate) | [Pipeline](php/wodby/pipeline.yml) | [Workflow](php/github-actions/wodby.yml) | [Pipeline](php/gitlab-ci/.gitlab-ci.yml) | [Config](php/circleci/config.yml) | [Runtime check](php/wodby/post-deployment.yml) |
| Drupal | [drupal-vanilla](https://github.com/wodby/drupal-vanilla), [drupal-cms-template](https://github.com/wodby/drupal-cms-template) | [Pipeline](drupal/wodby/pipeline.yml) | [Workflow](drupal/github-actions/wodby.yml) | [Pipeline](drupal/gitlab-ci/.gitlab-ci.yml) | [Config](drupal/circleci/config.yml) | [Drush status](drupal/wodby/post-deployment.yml) |
| WordPress | [wordpress-vanilla](https://github.com/wodby/wordpress-vanilla) | [Pipeline](wordpress/wodby/pipeline.yml) | [Workflow](wordpress/github-actions/wodby.yml) | [Pipeline](wordpress/gitlab-ci/.gitlab-ci.yml) | [Config](wordpress/circleci/config.yml) | [WP-CLI check](wordpress/wodby/post-deployment.yml) |
| Laravel | [laravel-boilerplate](https://github.com/wodby/laravel-boilerplate) | [Pipeline](laravel/wodby/pipeline.yml) | [Workflow](laravel/github-actions/wodby.yml) | [Pipeline](laravel/gitlab-ci/.gitlab-ci.yml) | [Config](laravel/circleci/config.yml) | [Artisan check](laravel/wodby/post-deployment.yml) |
| Symfony | [symfony-boilerplate](https://github.com/wodby/symfony-boilerplate) | [Pipeline](symfony/wodby/pipeline.yml) | [Workflow](symfony/github-actions/wodby.yml) | [Pipeline](symfony/gitlab-ci/.gitlab-ci.yml) | [Config](symfony/circleci/config.yml) | [Console check](symfony/wodby/post-deployment.yml) |
| Matomo (buildable) | [matomo-boilerplate](https://github.com/wodby/matomo-boilerplate) | [Pipeline](matomo/wodby/pipeline.yml) | [Workflow](matomo/github-actions/wodby.yml) | [Pipeline](matomo/gitlab-ci/.gitlab-ci.yml) | [Config](matomo/circleci/config.yml) | [Console check](matomo/wodby/post-deployment.yml) |
| Python | [python-boilerplate](https://github.com/wodby/python-boilerplate) | [Pipeline](python/wodby/pipeline.yml) | [Workflow](python/github-actions/wodby.yml) | [Pipeline](python/gitlab-ci/.gitlab-ci.yml) | [Config](python/circleci/config.yml) | [Application check](python/wodby/post-deployment.yml) |
| Django | [django-boilerplate](https://github.com/wodby/django-boilerplate) | [Pipeline](django/wodby/pipeline.yml) | [Workflow](django/github-actions/wodby.yml) | [Pipeline](django/gitlab-ci/.gitlab-ci.yml) | [Config](django/circleci/config.yml) | [System check](django/wodby/post-deployment.yml) |
| FastAPI | [fastapi-boilerplate](https://github.com/wodby/fastapi-boilerplate) | [Pipeline](fastapi/wodby/pipeline.yml) | [Workflow](fastapi/github-actions/wodby.yml) | [Pipeline](fastapi/gitlab-ci/.gitlab-ci.yml) | [Config](fastapi/circleci/config.yml) | [Health check](fastapi/wodby/post-deployment.yml) |
| Flask | [flask-boilerplate](https://github.com/wodby/flask-boilerplate) | [Pipeline](flask/wodby/pipeline.yml) | [Workflow](flask/github-actions/wodby.yml) | [Pipeline](flask/gitlab-ci/.gitlab-ci.yml) | [Config](flask/circleci/config.yml) | [Health check](flask/wodby/post-deployment.yml) |
| Ruby | [ruby-boilerplate](https://github.com/wodby/ruby-boilerplate) | [Pipeline](ruby/wodby/pipeline.yml) | [Workflow](ruby/github-actions/wodby.yml) | [Pipeline](ruby/gitlab-ci/.gitlab-ci.yml) | [Config](ruby/circleci/config.yml) | [Health check](ruby/wodby/post-deployment.yml) |
| Rails | [rails-boilerplate](https://github.com/wodby/rails-boilerplate) | [Pipeline](rails/wodby/pipeline.yml) | [Workflow](rails/github-actions/wodby.yml) | [Pipeline](rails/gitlab-ci/.gitlab-ci.yml) | [Config](rails/circleci/config.yml) | [Application check](rails/wodby/post-deployment.yml) |
| Go | [go-boilerplate](https://github.com/wodby/go-boilerplate) | [Pipeline](go/wodby/pipeline.yml) | [Workflow](go/github-actions/wodby.yml) | [Pipeline](go/gitlab-ci/.gitlab-ci.yml) | [Config](go/circleci/config.yml) | [Health check](go/wodby/post-deployment.yml) |
| Rust | [rust-boilerplate](https://github.com/wodby/rust-boilerplate) | [Pipeline](rust/wodby/pipeline.yml) | [Workflow](rust/github-actions/wodby.yml) | [Pipeline](rust/gitlab-ci/.gitlab-ci.yml) | [Config](rust/circleci/config.yml) | [Health check](rust/wodby/post-deployment.yml) |
| Java | [java-boilerplate](https://github.com/wodby/java-boilerplate) | [Pipeline](java/wodby/pipeline.yml) | [Workflow](java/github-actions/wodby.yml) | [Pipeline](java/gitlab-ci/.gitlab-ci.yml) | [Config](java/circleci/config.yml) | [Health check](java/wodby/post-deployment.yml) |
| Spring Boot | [spring-boot-boilerplate](https://github.com/wodby/spring-boot-boilerplate) | [Pipeline](spring-boot/wodby/pipeline.yml) | [Workflow](spring-boot/github-actions/wodby.yml) | [Pipeline](spring-boot/gitlab-ci/.gitlab-ci.yml) | [Config](spring-boot/circleci/config.yml) | [Actuator health](spring-boot/wodby/post-deployment.yml) |
| Kotlin | [kotlin-boilerplate](https://github.com/wodby/kotlin-boilerplate) | [Pipeline](kotlin/wodby/pipeline.yml) | [Workflow](kotlin/github-actions/wodby.yml) | [Pipeline](kotlin/gitlab-ci/.gitlab-ci.yml) | [Config](kotlin/circleci/config.yml) | [Health check](kotlin/wodby/post-deployment.yml) |
| ASP.NET Core | [aspnetcore-boilerplate](https://github.com/wodby/aspnetcore-boilerplate) | [Pipeline](aspnetcore/wodby/pipeline.yml) | [Workflow](aspnetcore/github-actions/wodby.yml) | [Pipeline](aspnetcore/gitlab-ci/.gitlab-ci.yml) | [Config](aspnetcore/circleci/config.yml) | [Health check](aspnetcore/wodby/post-deployment.yml) |
| Node.js | [expressjs-boilerplate](https://github.com/wodby/expressjs-boilerplate) | [Pipeline](node/wodby/pipeline.yml) | [Workflow](node/github-actions/wodby.yml) | [Pipeline](node/gitlab-ci/.gitlab-ci.yml) | [Config](node/circleci/config.yml) | [Runtime check](node/wodby/post-deployment.yml) |
| Next.js | [nextjs-boilerplate](https://github.com/wodby/nextjs-boilerplate) | [Pipeline](nextjs/wodby/pipeline.yml) | [Workflow](nextjs/github-actions/wodby.yml) | [Pipeline](nextjs/gitlab-ci/.gitlab-ci.yml) | [Config](nextjs/circleci/config.yml) | [Application check](nextjs/wodby/post-deployment.yml) |
| Nuxt | [nuxt-boilerplate](https://github.com/wodby/nuxt-boilerplate) | [Pipeline](nuxt/wodby/pipeline.yml) | [Workflow](nuxt/github-actions/wodby.yml) | [Pipeline](nuxt/gitlab-ci/.gitlab-ci.yml) | [Config](nuxt/circleci/config.yml) | [Health check](nuxt/wodby/post-deployment.yml) |
| SvelteKit | [sveltekit-boilerplate](https://github.com/wodby/sveltekit-boilerplate) | [Pipeline](sveltekit/wodby/pipeline.yml) | [Workflow](sveltekit/github-actions/wodby.yml) | [Pipeline](sveltekit/gitlab-ci/.gitlab-ci.yml) | [Config](sveltekit/circleci/config.yml) | [Health check](sveltekit/wodby/post-deployment.yml) |
| Astro | [astro-boilerplate](https://github.com/wodby/astro-boilerplate) | [Pipeline](astro/wodby/pipeline.yml) | [Workflow](astro/github-actions/wodby.yml) | [Pipeline](astro/gitlab-ci/.gitlab-ci.yml) | [Config](astro/circleci/config.yml) | [Health check](astro/wodby/post-deployment.yml) |
| TanStack Start | [tanstack-start-boilerplate](https://github.com/wodby/tanstack-start-boilerplate) | [Pipeline](tanstack-start/wodby/pipeline.yml) | [Workflow](tanstack-start/github-actions/wodby.yml) | [Pipeline](tanstack-start/gitlab-ci/.gitlab-ci.yml) | [Config](tanstack-start/circleci/config.yml) | [Health check](tanstack-start/wodby/post-deployment.yml) |
| Strapi | [strapi-boilerplate](https://github.com/wodby/strapi-boilerplate) | [Pipeline](strapi/wodby/pipeline.yml) | [Workflow](strapi/github-actions/wodby.yml) | [Pipeline](strapi/gitlab-ci/.gitlab-ci.yml) | [Config](strapi/circleci/config.yml) | [Health check](strapi/wodby/post-deployment.yml) |

The HTML example copies `public` into the Nginx image as it is. The static example expects `npm run build` to write to
`dist`; change `--from dist` when the framework uses a different output directory. The Angular, React, and Vue examples
install, test, and build in the `wodby/node` image, then copy the result into their Nginx-based service image. Angular
writes to `dist/<project name>/browser`, so replace `angular-boilerplate` in that path with your project's name.

The Python example follows the Python boilerplate conventions: `uv.lock`, `pytest`, `Dockerfile`, and the
`python_boilerplate` package.

The Symfony example installs Composer development packages too, because an environment of type `dev` runs the same image
with `APP_ENV=dev`.

The Matomo example is for the buildable Matomo stack. Its repository holds `.matomo-version` and your own Matomo
plugins. The service's Dockerfile installs that Matomo release and the plugins, so the pipeline has no dependency step.
The prebuilt Matomo stack does not build from a repository.

The ASP.NET Core service image contains only the .NET runtime, so its example runs tests in the `wodby/dotnet:10.0-dev`
SDK image.

Laravel queue and Rails Sidekiq are service derivatives of their main runtimes. Their examples build the application
image once; the stack reuses that image for the corresponding worker service.

Post-deployment jobs should be safe to retry. Use them for smoke checks and idempotent application operations, and
remember that a post-deployment failure is reported separately from the completed deployment.

## Stacks without examples

Dagster has no source-build example; the current catalog service deploys a packaged image.

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
- CircleCI uses the public [`wodby/setup-wodby-cli@1`](https://circleci.com/developer/orbs/orb/wodby/setup-wodby-cli)
  orb with a machine executor. The `wodby/setup` command installs the latest Wodby 2 CLI and runs `wodby ci init`
  when `app-service-id` is provided. Configure `WODBY_API_KEY` and `WODBY_APP_SERVICE_ID` as project environment
  variables.

The CircleCI examples declare and initialize the Orb like this:

```yaml
orbs:
  wodby: wodby/setup-wodby-cli@1

steps:
  - wodby/setup:
      app-service-id: $WODBY_APP_SERVICE_ID
```

VM-based executors are preferable when a provider supports them. Container-only executors require
Docker-in-Docker because `wodby ci build` creates Docker images.

## Build behavior

The common pipeline flow is:

1. Initialize the build with `wodby ci init`.
2. Install dependencies or run tests with `wodby ci run`.
3. Build one or more service images with `wodby ci build`.
4. Push the built images with `wodby ci push`.
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

### Dependency caches

`wodby ci run` automatically configures npm, Composer, Bundler, and uv caches for supported Wodby and official images.
Wodby images advertise their cache profile through image metadata, so application images derived from them inherit the
same behavior. Use `--cache` to force a profile for another image or `--no-cache` to disable caching. Examples that get
their dependencies from Go modules, Cargo, Maven, Gradle, or NuGet, or install them only inside a Dockerfile, have no
cache steps.

GitHub Actions cache restore and save are handled by `wodby/actions/setup-wodby-cli` when it detects a supported
lockfile. Other providers keep their native cache steps, but no longer need to pass cache volumes or package-manager
environment variables to `wodby ci run`. Native Docker environments use the package managers' conventional user cache
paths. Docker-in-Docker jobs stage persistent data under `.wodby-ci-cache/<profile>` in the CI context, import it into
their data volume during `wodby ci init`, and export it after each cache-enabled `wodby ci run`.

## Validation

Run the repository checks with:

```shell
python3 -m pip install -r scripts/requirements.txt
python3 scripts/validate_examples.py
```

The pull-request workflow also runs `actionlint` against the nested GitHub Actions examples and checks README links.
