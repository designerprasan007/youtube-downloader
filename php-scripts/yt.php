<?php
	$data = $_GET['v_name'];
    $command = escapeshellcmd('python3 ../python-scripts/yt.py ' . $data);
    $output = shell_exec($command);
    echo $output;
?>