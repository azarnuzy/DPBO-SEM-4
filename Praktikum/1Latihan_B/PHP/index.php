<?php

include "DaftarTimSepakBola.php";

$daftarTim1 = new DaftarTimSepakBola();
$daftarTim1->setNama("Barcelona");
$daftarTim1->setNegara("Spanyol");
$daftarTim1->setTahunBerdiri("1893");
$daftarTim1->setPemain("Sergio Ramos");

echo $daftarTim1->printHasil();

$daftarTim2 = new DaftarTimSepakBola("Manchester United", "England", "1878", "Wayne Rooney");

echo "<br/>";

echo $daftarTim2->printHasil();
