#!/usr/bin/env python3
"""Validate the structure and conventions of the published CI examples."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

import yaml


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
FULL_PROVIDER_EXAMPLES = ("php", "node", "static", "python")
STACK_RECIPES = (
    "django",
    "drupal",
    "go",
    "laravel",
    "matomo",
    "nextjs",
    "rails",
    "wordpress",
)
APPLICATION_STACKS = (
    "HTML",
    "PHP",
    "Drupal",
    "WordPress",
    "Laravel",
    "Matomo",
    "Python",
    "Django",
    "FastAPI",
    "Flask",
    "Ruby",
    "Rails",
    "Go",
    "Node.js",
    "Next.js",
    "Dagster",
)
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
            "actions/cache@v5",
            "wodby/actions/setup-wodby-cli@v1",
            "${{ secrets.WODBY_API_KEY }}",
            "${{ vars.WODBY_APP_SERVICE_ID }}",
        )
        for value in required:
            if value not in text:
                errors.append(f"{relative(path)}: missing required convention {value}")
        if "PASTE-APP_SERVICE_ID-HERE" in text:
            errors.append(f"{relative(path)}: use the WODBY_APP_SERVICE_ID variable")


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

    for recipe in STACK_RECIPES:
        for name in ("pipeline.yml", "post-deployment.yml"):
            path = REPOSITORY_ROOT / recipe / "wodby" / name
            if not path.is_file():
                errors.append(f"{relative(path)}: missing stack recipe")


def validate_readme(errors: list[str]) -> None:
    readme_path = REPOSITORY_ROOT / "README.md"
    text = readme_path.read_text()

    for stack in APPLICATION_STACKS:
        if stack not in text:
            errors.append(f"README.md: application stack coverage is missing {stack}")

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
    validate_third_party_variables(errors)
    validate_example_coverage(errors)
    validate_readme(errors)

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print("All Wodby CI examples passed validation.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
