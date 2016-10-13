<?php

use \Wodby\Api\Entity;

require_once __DIR__ . '/vendor/autoload.php';

$api = new Wodby\Api(getenv('WODBY_API_TOKEN'), new GuzzleHttp\Client());

/******************************************************************************
 * Create new application instance.
 */

echo "Deploying new instance via Wodby...", PHP_EOL;

$result = $api->instance()->create(
  getenv('WODBY_APP_ID'),
  'jenkins-' . getenv('BUILD_NUMBER'),
  Entity\Instance::TYPE_DEV,
  getenv('WODBY_SERVER_ID'),
  [
    Entity\Instance::COMPONENT_DATABASE => getenv('WODBY_SOURCE_INSTANCE_ID'),
    Entity\Instance::COMPONENT_FILES => getenv('WODBY_SOURCE_INSTANCE_ID'),
  ],
  '[Jenkins] Build #' . getenv('BUILD_NUMBER')
);

/** @var Entity\Task $task */
$task = $result['task'];
/** @var Entity\Instance $instance */
$instance = $result['instance'];

$api->task()->wait($task->getId(), 600);

/******************************************************************************
 * Import codebase.
 */
$build_file_url = sprintf(
  "https://s3.amazonaws.com/%s/%s-%s.tar.gz",
  getenv('AWS_S3_BUCKET'),
  getenv('AWS_S3_FILE_NAME'),
  getenv('BUILD_NUMBER')
);

echo "Importing codebase: $build_file_url", PHP_EOL;
$result = $api->instance()->importCodebase($instance->getId(), $build_file_url);

/** @var Entity\Task $task */
$task = $result['task'];
$api->task()->wait($task->getId(), 600);

/******************************************************************************
 * Update application instance build info.
 */

echo "Updating build info...", PHP_EOL;

$api->instance()->updateProperty(
  $instance->getId(),
  Entity\Instance::PROPERTY_BUILD_INFO,
  [
    'builder' => 'Jenkins',
    'project_name' => getenv('JOB_NAME'),
    'project_url' => getenv('JOB_URL'),
    'build_number' => getenv('BUILD_NUMBER'),
    'build_url' => getenv('BUILD_URL'),
    'build_download_url' => $build_file_url,
    'git_branch' => getenv('GIT_BRANCH'),
    'git_commit' => getenv('GIT_COMMIT'),
  ]
);
