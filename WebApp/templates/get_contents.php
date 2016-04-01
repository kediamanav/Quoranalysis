<?php
	
	ini_set('display_errors', 1);
	$argument = $_GET['argument1'];

	// echo $argument;
	// $argu = "/var/www/html/nlp/Theme/data/"	+ $argument;
	// echo $argu;
	$fp = fopen($argument , 'r') or die('fopen failed');
	$contents = fread($fp, filesize($argument)) or die('fread failed');
	echo $contents;
	fclose($fp);
	// echo $contents;
?>