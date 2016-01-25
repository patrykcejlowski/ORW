<?php

    $data = date('Y-M-D-H-i')."-".time();
    echo $data;
    $file = fopen('store.txt', 'a');
    fwrite($file, $data."\r\n");
    fclose($file);

?>