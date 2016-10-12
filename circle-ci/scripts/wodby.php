<?php
  
use \Wodby\Api\Entity;

require_once __DIR__ . '/vendor/autoload.php';

$api = new Wodby\Api($_SERVER['WODBY_API_TOKEN'], new GuzzleHttp\Client());

echo PHP_EOL;
echo "Creating instance.", PHP_EOL;
$result = $api->instance()->create(
  $_SERVER['WODBY_APP_ID'],
  'test-' . $_SERVER['CIRCLE_BUILD_NUM'],
  Entity\Instance::TYPE_DEV,
  $_SERVER['WODBY_SERVER_ID'],
  [
    Entity\Instance::COMPONENT_DATABASE => $_SERVER['WODBY_SOURCE_INSTANCE_ID'],
    Entity\Instance::COMPONENT_FILES => $_SERVER['WODBY_SOURCE_INSTANCE_ID'],
  ],
  "[CircleCI] Test Build {$_SERVER['CIRCLE_BUILD_NUM']}"
);

/** @var Entity\Task $task */
$task = $result['task'];

/** @var Entity\Instance $instance */
$instance = $result['instance'];

echo "Deploying new instance via Wodby...", PHP_EOL;
$api->task()->wait($task->getId(), 600);

$s3_bucket = $_SERVER['AWS_S3_BUCKET'];
$s3_file_name = $_SERVER['AWS_S3_FILE_NAME'] . '-' . $_SERVER['CIRCLE_BUILD_NUM'];
$build_file_url = "https://s3.amazonaws.com/$s3_bucket/$s3_file_name.tar.gz";

echo "Importing $build_file_url", PHP_EOL;
$result = $api->instance()->importCodebase($instance->getId(), $build_file_url);

/** @var Entity\Task $task */
$task = $result['task'];
$api->task()->wait($task->getId(), 600);

echo "Updating build info", PHP_EOL;
$api->instance()->updateProperty(
  $instance->getId(),
  Entity\Instance::PROPERTY_BUILD_INFO,
  [
    'builder' => 'CircleCI',
    'project_name' => $_SERVER['CIRCLE_PROJECT_REPONAME'],
    'project_url' => $_SERVER['CIRCLE_REPOSITORY_URL'],
    'build_number' => $_SERVER['CIRCLE_BUILD_NUM'],
    'build_url' => $_SERVER['CIRCLE_BUILD_URL'],
    'build_download_url' => $build_file_url,
    'git_branch' => $_SERVER['CIRCLE_BRANCH'],
    'git_commit' => $_SERVER['CIRCLE_SHA1'],
  ]
);

echo "Done!", PHP_EOL;
