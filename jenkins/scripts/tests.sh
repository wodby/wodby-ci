#!/bin/bash

sudo chown -R 82:82 .

docker-compose up -d mariadb
docker-compose up -d nginx

docker-compose run --user 82 php vendor/bin/phpunit -c core core/tests/Drupal/Tests/Core/Password/PasswordHashingTest.php
docker-compose run --user 82 php vendor/bin/phpunit -c core core/tests/Drupal/KernelTests/Component/Utility/SafeMarkupKernelTest.php
docker-compose run --user 82 php vendor/bin/phpunit -c core core/tests/Drupal/FunctionalTests/Breadcrumb/Breadcrumb404Test.php

sudo chown -R jenkins:jenkins .

docker-compose down --remove-orphans
