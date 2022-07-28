<?php

#The URL root is the AWS meta data service URL where metadata
# requests regarding the running instance can be made
$urlRoot = "http://169.254.169.254/latest/meta-data/";

# Get the instance ID from meta-data and print to the screen
$instance = file_get_contents($urlRoot . 'instance-id');

# Availability Zone
$az = file_get_contents($urlRoot . 'placement/availability-zone');

?>

<div class="text-center">
  <p class="pb-3">このアプリケーションが動作しているEC2インスタンスのID： <b><?= $instance ?></b></p>
  <p>EC2インスタンスが動作しているAZ： <b><?= $az ?></b></p>
</div>