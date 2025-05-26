<?php
$x = $_GET['x'];
$y = $_GET['y'];
$z = $_GET['z'];
$command = escapeshellcmd("python3 /var/www/html/process_input.py $x $y $z");
$output = shell_exec($command);
echo $output;
?>
