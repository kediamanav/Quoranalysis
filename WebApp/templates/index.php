<?php
	//echo $_POST["msg"];
	// putenv('PYTHONPATH=/usr/lib/python2.7/dist-packages:');
	$argument = $_POST["msg"];

	
	echo "string";
	

	// putenv("PYTHONPATH=['/var/www/html/nlp/Theme/codes', '/usr/local/lib/python2.7/dist-packages/setuptools-12.2-py2.7.egg', '/usr/local/lib/python2.7/dist-packages/pip-6.0.8-py2.7.egg', '/usr/local/lib/python2.7/dist-packages/networkx-1.9.1-py2.7.egg', '/usr/local/lib/python2.7/dist-packages/decorator-3.4.0-py2.7.egg', '/usr/local/lib/python2.7/dist-packages/gensim-0.10.3-py2.7-linux-x86_64.egg', '/usr/lib/python2.7', '/usr/lib/python2.7/plat-x86_64-linux-gnu', '/usr/lib/python2.7/lib-tk', '/usr/lib/python2.7/lib-old', '/usr/lib/python2.7/lib-dynload', '/home/sunman/.local/lib/python2.7/site-packages', '/usr/local/lib/python2.7/dist-packages', '/usr/lib/python2.7/dist-packages', '/usr/lib/python2.7/dist-packages/PILcompat', '/usr/lib/python2.7/dist-packages/gtk-2.0', '/usr/lib/pymodules/python2.7', '/usr/lib/python2.7/dist-packages/ubuntu-sso-client']");
	echo getenv("PYTHONPATH"); // NOTHING
	$fp = fopen('./data/answer.txt', 'w') or die('fopen failed');
	fwrite($fp, $argument) or die('fwrite failed');
	fclose($fp);

	$output_humor = system("/usr/bin/python2.7 /var/www/html/nlp/Theme/codes/test.py", $ret_val);
	echo"sing_sang";
	echo $ret_val;
	echo $output_humor;
	echo "string2";
	$myfile = fopen("/var/www/html/nlp/Theme/data/humor.txt", "w") or die("Unable to open file!");
	fwrite($myfile, $output_humor);
	fclose($myfile);
	// $output_humor = shell_exec("python /var/www/html/predict.py");
	// //echo $output;
	// $myfile = fopen("./humor.txt", "w") or die("Unable to open file!");
	// fwrite($myfile, $output_humor);
	// fclose($myfile);
	// $output_humor = shell_exec("python /var/www/html/predict.py");
	// //echo $output;
	// $myfile = fopen("./humor.txt", "w") or die("Unable to open file!");
	// fwrite($myfile, $output_humor);
	// fclose($myfile);
	// $output_humor = shell_exec("python /var/www/html/predict.py");
	// //echo $output;
	// $myfile = fopen("./humor.txt", "w") or die("Unable to open file!");
	// fwrite($myfile, $output_humor);
	// fclose($myfile);

?>