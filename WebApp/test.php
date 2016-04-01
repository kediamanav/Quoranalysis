<?php
	include './Text-Statistics/src/DaveChild/TextStatistics/TextStatistics.php';
	include './Text-Statistics/src/DaveChild/TextStatistics/Text.php';
	include './Text-Statistics/src/DaveChild/TextStatistics/Syllables.php';
	include './Text-Statistics/src/DaveChild/TextStatistics/Resource.php';
	include './Text-Statistics/src/DaveChild/TextStatistics/Pluralise.php';
	include './Text-Statistics/src/DaveChild/TextStatistics/Maths.php';
	use DaveChild\TextStatistics as TS;
	$textStatistics = new TS\TextStatistics;

	$filename = './query.txt';
	$handle = fopen($filename,"r");
	$contents = fread($handle, filesize($filename));
	fclose($handle);

	$text = $contents;
	$text1 = $contents;


	$msg =  $textStatistics->fleschKincaidReadingEase($text);
	$msg1 = $textStatistics->fleschKincaidReadingEase($text1);
	$final = ($msg+$msg1)/2;

	$fp = fopen('./readability.txt',"w");
	fwrite($fp,$final);
	fclose($fp);
?>