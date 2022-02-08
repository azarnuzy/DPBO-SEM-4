<?php

include "DaftarMahasiswa.php";

$daftarMahasiswa1 = new DaftarMahasiswa();
$daftarMahasiswa1->setNIM("2004191");
$daftarMahasiswa1->setNama("Muhammad Azar");
$daftarMahasiswa1->setJenisKelamin("Laki-Laki");
$daftarMahasiswa1->setProdi("Ilmu Komputer");
$daftarMahasiswa1->setSemester("4");

echo $daftarMahasiswa1->printHasil();

$daftarMahasiswa2 = new DaftarMahasiswa("2004192", "Nuzy", "Laki-Laki", "Ilmu Komputer", "4");

echo "<br/>";

echo $daftarMahasiswa2->printHasil();
