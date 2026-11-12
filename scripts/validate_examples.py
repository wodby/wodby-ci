#!/usr/bin/env python3
"""Validate the structure and conventions of the published CI examples."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

import yaml


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
FULL_PROVIDER_EXAMPLES = (
    "angular",
    "aspnetcore",
    "astro",
    "django",
    "drupal",
    "fastapi",
    "flask",
    "go",
    "html",
    "java",
    "kotlin",
    "laravel",
    "matomo",
    "nextjs",
    "node",
    "nuxt",
    "php",
    "python",
    "rails",
    "react",
    "ruby",
    "rust",
    "spring-boot",
    "static",
    "strapi",
    "sveltekit",
    "symfony",
    "tanstack-start",
    "vue",
    "wordpress",
)
# Wodby build boilerplates offered by the catalog services. The README must link each
# of them, so a new boilerplate cannot be added to the catalog without an example here.
BOILERPLATE_REPOSITORIES = (
    "wodby/angular-boilerplate",
    "wodby/aspnetcore-boilerplate",
    "wodby/astro-boilerplate",
    "wodby/django-boilerplate",
    "wodby/drupal-cms-template",
    "wodby/drupal-vanilla",
    "wodby/expressjs-boilerplate",
    "wodby/fastapi-boilerplate",
    "wodby/flask-boilerplate",
    "wodby/go-boilerplate",
    "wodby/html-boilerplate",
    "wodby/java-boilerplate",
    "wodby/kotlin-boilerplate",
    "wodby/laravel-boilerplate",
    "wodby/matomo-boilerplate",
    "wodby/nextjs-boilerplate",
    "wodby/nuxt-boilerplate",
    "wodby/php-package-boilerplate",
    "wodby/python-boilerplate",
    "wodby/rails-boilerplate",
    "wodby/react-boilerplate",
    "wodby/ruby-boilerplate",
    "wodby/rust-boilerplate",
    "wodby/spring-boot-boilerplate",
    "wodby/strapi-boilerplate",
    "wodby/sveltekit-boilerplate",
    "wodby/symfony-boilerplate",
    "wodby/tanstack-start-boilerplate",
    "wodby/vue-boilerplate",
    "wodby/wordpress-vanilla",
)
APPLICATION_STACKS = (
    "HTML",
    "Angular",
    "React",
    "Vue",
    "PHP",
    "Drupal",
    "WordPress",
    "Laravel",
    "Symfony",
    "Matomo",
    "Python",
    "Django",
    "FastAPI",
    "Flask",
    "Ruby",
    "Rails",
    "Go",
    "Rust",
    "Java",
    "Spring Boot",
    "Kotlin",
    "ASP.NET Core",
    "Node.js",
    "Next.js",
    "Nuxt",
    "SvelteKit",
    "Astro",
    "TanStack Start",
    "Strapi",
    "Dagster",
)
EXPECTED_PROVIDER_COMMANDS = {
    "angular": (
        "wodby ci run -i wodby/node -- npm ci",
        "wodby ci run -i wodby/node -- npm test",
        "wodby ci run -i wodby/node -- npm run build",
        "wodby ci build angular --from dist/angular-boilerplate/browser",
    ),
    "aspnetcore": (
        "wodby ci run -i wodby/dotnet:10.0-dev -- dotnet test --solution App.slnx",
        "wodby ci build aspnetcore -f Dockerfile",
    ),
    "astro": (
        "wodby ci run -s astro -- npm ci",
        "wodby ci build astro",
    ),
    "django": (
        "wodby ci run -s django -- uv run --frozen pytest",
        "wodby ci build django -f Dockerfile",
    ),
    "drupal": (
        "wodby ci run -s php -- composer install --prefer-dist -n --no-ansi",
        "wodby ci build",
    ),
    "fastapi": (
        "wodby ci run -s fastapi -- uv run --frozen ruff check .",
        "wodby ci run -s fastapi -- uv run --frozen ruff format --check .",
        "wodby ci run -s fastapi -- uv run --frozen pytest",
        "wodby ci build fastapi -f Dockerfile",
    ),
    "flask": (
        "wodby ci run -s flask -- uv run --frozen ruff check .",
        "wodby ci run -s flask -- uv run --frozen ruff format --check .",
        "wodby ci run -s flask -- uv run --frozen pytest",
        "wodby ci build flask -f Dockerfile",
    ),
    "go": (
        "wodby ci run -s go -- go test ./...",
        "wodby ci build go -f Dockerfile",
    ),
    "html": ("wodby ci build nginx --from public",),
    "java": (
        "wodby ci run -s java -- sh ./mvnw -B -ntp test",
        "wodby ci build java -f Dockerfile",
    ),
    "kotlin": (
        "wodby ci run -s kotlin -- sh ./gradlew --no-daemon --console=plain test",
        "wodby ci build kotlin -f Dockerfile",
    ),
    "laravel": (
        "wodby ci run -s php -- composer install --prefer-dist -n --no-ansi",
        "wodby ci build php",
        "wodby ci build nginx",
    ),
    "matomo": ("wodby ci build matomo",),
    "nextjs": (
        "wodby ci run -s nextjs -- npm ci",
        "wodby ci build nextjs -f Dockerfile",
    ),
    "node": (
        "npm ci",
        "wodby ci build",
    ),
    "nuxt": (
        "wodby ci run -s nuxt -- npm ci",
        "wodby ci build nuxt",
    ),
    "php": (
        "wodby ci run -- composer install --prefer-dist -n --no-ansi",
        "wodby ci build",
    ),
    "python": (
        "wodby ci run -s python -- uv run --frozen pytest",
        "wodby ci build python -f Dockerfile",
    ),
    "rails": ("wodby ci build rails -f Dockerfile",),
    "react": (
        "wodby ci run -i wodby/node -- npm ci",
        "wodby ci run -i wodby/node -- npm test",
        "wodby ci run -i wodby/node -- npm run build",
        "wodby ci build react --from dist",
    ),
    "ruby": ("wodby ci build ruby -f Dockerfile",),
    "rust": (
        "wodby ci run -s rust -- cargo fmt --check",
        "wodby ci run -s rust -- cargo clippy --locked --all-targets -- -D warnings",
        "wodby ci run -s rust -- cargo test --locked",
        "wodby ci build rust -f Dockerfile",
    ),
    "spring-boot": (
        "wodby ci run -s spring-boot -- sh ./mvnw -B -ntp test",
        "wodby ci build spring-boot -f Dockerfile",
    ),
    "static": (
        "wodby ci run -i wodby/node:24 -- npm ci",
        "wodby ci run -i wodby/node:24 -- npm run build",
        "wodby ci build nginx --from dist",
    ),
    "strapi": (
        "wodby ci run -s strapi -- npm ci",
        "wodby ci build strapi",
    ),
    "sveltekit": (
        "wodby ci run -s sveltekit -- npm ci",
        "wodby ci build sveltekit",
    ),
    "symfony": (
        "wodby ci run -s php -- composer install -n --no-ansi --prefer-dist --optimize-autoloader",
        "wodby ci build php",
        "wodby ci build nginx",
    ),
    "tanstack-start": (
        "wodby ci run -s tanstack-start -- npm ci",
        "wodby ci build tanstack-start",
    ),
    "vue": (
        "wodby ci run -i wodby/node -- npm ci",
        "wodby ci run -i wodby/node -- npm test",
        "wodby ci run -i wodby/node -- npm run build",
        "wodby ci build vue --from dist",
    ),
    "wordpress": (
        "wodby ci run -s php -- composer install --prefer-dist -n --no-ansi",
        "wodby ci build",
    ),
}
MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def relative(path: Path) -> str:
    return path.relative_to(REPOSITORY_ROOT).as_posix()


def validate_yaml(errors: list[str]) -> None:
    yaml_files = sorted(
        path
        for path in REPOSITORY_ROOT.rglob("*")
        if path.suffix in {".yml", ".yaml"} and ".git" not in path.parts
    )
    for path in yaml_files:
        try:
            list(yaml.compose_all(path.read_text()))
        except yaml.YAMLError as exc:
            errors.append(f"{relative(path)}: invalid YAML: {exc}")


def validate_wodby_pipelines(errors: list[str]) -> None:
    pipelines = sorted(REPOSITORY_ROOT.glob("*/wodby/pipeline.yml"))
    for path in pipelines:
        text = path.read_text()
        try:
            data = yaml.safe_load(text)
        except yaml.YAMLError:
            continue

        if not isinstance(data, dict) or str(data.get("version")) != "0.1":
            errors.append(f"{relative(path)}: expected pipeline version 0.1")
        if "wodby ci init $WODBY_BUILD_ID" not in text:
            errors.append(f"{relative(path)}: missing Wodby build initialization")
        if "api.wodby.com/v1/get/cli" in text:
            errors.append(f"{relative(path)}: Wodby CI already installs Wodby CLI")


def validate_github_examples(errors: list[str]) -> None:
    for path in sorted(REPOSITORY_ROOT.glob("*/github-actions/*.yml")):
        text = path.read_text()
        required = (
            "actions/checkout@v6",
            "wodby/actions/setup-wodby-cli@v1",
            "${{ secrets.WODBY_API_KEY }}",
            "${{ vars.WODBY_APP_SERVICE_ID }}",
        )
        for value in required:
            if value not in text:
                errors.append(f"{relative(path)}: missing required convention {value}")
        if "PASTE-APP_SERVICE_ID-HERE" in text:
            errors.append(f"{relative(path)}: use the WODBY_APP_SERVICE_ID variable")


def validate_circleci_examples(errors: list[str]) -> None:
    for path in sorted(REPOSITORY_ROOT.glob("*/circleci/config.yml")):
        text = path.read_text()
        required = (
            "wodby: wodby/setup-wodby-cli@1",
            "- wodby/setup:",
            "app-service-id: $WODBY_APP_SERVICE_ID",
        )
        for value in required:
            if value not in text:
                errors.append(f"{relative(path)}: missing required convention {value}")
        for value in (
            "api.wodby.com/v1/get/cli",
            "- run: wodby ci init $WODBY_APP_SERVICE_ID",
        ):
            if value in text:
                errors.append(f"{relative(path)}: orb setup replaces {value}")


def validate_automatic_cache_examples(errors: list[str]) -> None:
    forbidden = (
        "/home/node/.npm",
        "/home/wodby/.composer",
        "/home/wodby/.bundle/cache",
        "/home/wodby/.cache/uv",
        ".wodby-cache/",
        "WODBY_CI_CACHE_DIR",
        "NPM_CONFIG_CACHE",
        "COMPOSER_CACHE_DIR",
        "BUNDLE_USER_CACHE",
        "UV_CACHE_DIR",
    )
    for path in sorted(REPOSITORY_ROOT.rglob("*.yml")):
        text = path.read_text()
        for value in forbidden:
            if value in text:
                errors.append(
                    f"{relative(path)}: cache profile should be managed automatically, found {value}"
                )

    native_paths = {
        "angular": "~/.npm",
        "astro": "~/.npm",
        "django": "~/.cache/uv",
        "drupal": "~/.composer/cache",
        "fastapi": "~/.cache/uv",
        "flask": "~/.cache/uv",
        "laravel": "~/.composer/cache",
        "nextjs": "~/.npm",
        "node": "~/.npm",
        "nuxt": "~/.npm",
        "php": "~/.composer/cache",
        "python": "~/.cache/uv",
        "react": "~/.npm",
        "static": "~/.npm",
        "strapi": "~/.npm",
        "sveltekit": "~/.npm",
        "symfony": "~/.composer/cache",
        "tanstack-start": "~/.npm",
        "vue": "~/.npm",
        "wordpress": "~/.composer/cache",
    }
    for example, expected in native_paths.items():
        for provider_path in ("wodby/pipeline.yml", "circleci/config.yml"):
            path = REPOSITORY_ROOT / example / provider_path
            if expected not in path.read_text():
                errors.append(f"{relative(path)}: missing cache path {expected}")

    dind_profiles = {
        "angular": "npm",
        "astro": "npm",
        "django": "uv",
        "drupal": "composer",
        "fastapi": "uv",
        "flask": "uv",
        "laravel": "composer",
        "nextjs": "npm",
        "node": "npm",
        "nuxt": "npm",
        "php": "composer",
        "python": "uv",
        "react": "npm",
        "static": "npm",
        "strapi": "npm",
        "sveltekit": "npm",
        "symfony": "composer",
        "tanstack-start": "npm",
        "vue": "npm",
        "wordpress": "composer",
    }
    for example, profile in dind_profiles.items():
        path = REPOSITORY_ROOT / example / "gitlab-ci/.gitlab-ci.yml"
        expected = f".wodby-ci-cache/{profile}"
        if expected not in path.read_text():
            errors.append(f"{relative(path)}: missing DinD cache path {expected}")

    if ".wodby-ci-cache/" not in (REPOSITORY_ROOT / ".gitignore").read_text():
        errors.append(".gitignore: missing .wodby-ci-cache/")


def validate_third_party_variables(errors: list[str]) -> None:
    for pattern in ("*/gitlab-ci/*.yml", "*/circleci/*.yml"):
        for path in sorted(REPOSITORY_ROOT.glob(pattern)):
            text = path.read_text()
            if "$WODBY_APP_SERVICE_ID" not in text:
                errors.append(f"{relative(path)}: missing WODBY_APP_SERVICE_ID")
            if "PASTE-APP_SERVICE_ID-HERE" in text:
                errors.append(
                    f"{relative(path)}: configure WODBY_APP_SERVICE_ID in the provider"
                )


def validate_example_coverage(errors: list[str]) -> None:
    provider_paths = (
        "wodby/pipeline.yml",
        "wodby/post-deployment.yml",
        "github-actions/wodby.yml",
        "gitlab-ci/.gitlab-ci.yml",
        "circleci/config.yml",
    )
    for example in FULL_PROVIDER_EXAMPLES:
        for provider_path in provider_paths:
            path = REPOSITORY_ROOT / example / provider_path
            if not path.is_file():
                errors.append(f"{relative(path)}: missing canonical provider example")

    # An example directory that is not listed above would skip the per-example checks.
    for path in sorted(REPOSITORY_ROOT.glob("*/wodby/pipeline.yml")):
        example = path.parent.parent.name
        if example not in FULL_PROVIDER_EXAMPLES:
            errors.append(f"{relative(path)}: add {example} to FULL_PROVIDER_EXAMPLES")


def validate_provider_commands(errors: list[str]) -> None:
    provider_paths = (
        "wodby/pipeline.yml",
        "github-actions/wodby.yml",
        "gitlab-ci/.gitlab-ci.yml",
        "circleci/config.yml",
    )
    for example, commands in EXPECTED_PROVIDER_COMMANDS.items():
        for provider_path in provider_paths:
            path = REPOSITORY_ROOT / example / provider_path
            if not path.is_file():
                continue
            text = path.read_text()
            for command in commands:
                if command not in text:
                    errors.append(f"{relative(path)}: missing command {command}")


def validate_readme(errors: list[str]) -> None:
    readme_path = REPOSITORY_ROOT / "README.md"
    text = readme_path.read_text()

    for stack in APPLICATION_STACKS:
        if stack not in text:
            errors.append(f"README.md: application stack coverage is missing {stack}")

    for repository in BOILERPLATE_REPOSITORIES:
        if f"https://github.com/{repository})" not in text:
            errors.append(f"README.md: boilerplate coverage is missing {repository}")

    for example in FULL_PROVIDER_EXAMPLES:
        if f"]({example}/wodby/pipeline.yml)" not in text:
            errors.append(f"README.md: example table is missing {example}")

    for raw_target in MARKDOWN_LINK.findall(text):
        target = raw_target.strip()
        if (
            not target
            or target.startswith(("#", "http://", "https://", "mailto:"))
        ):
            continue
        target = unquote(target.split("#", 1)[0])
        if not (REPOSITORY_ROOT / target).exists():
            errors.append(f"README.md: relative link target does not exist: {target}")


def main() -> int:
    errors: list[str] = []
    validate_yaml(errors)
    validate_wodby_pipelines(errors)
    validate_github_examples(errors)
    validate_circleci_examples(errors)
    validate_automatic_cache_examples(errors)
    validate_third_party_variables(errors)
    validate_example_coverage(errors)
    validate_provider_commands(errors)
    validate_readme(errors)

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print("All Wodby CI examples passed validation.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
