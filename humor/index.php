<?php
	echo $_POST["msg"];

	$argument = $_POST["msg"];

	$myfile = fopen("testfile.txt", "w");
	fwrite($myfile, $argument);
	fclose($myfile);
	
	//$command = escapeshellcmd('./predict.py'+$argument);
	//$output = shell_exec($command);
	//echo $output;

?>