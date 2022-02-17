<?php
/* Saya Muhammad Azar Nuzy 2004191 mengerjakan Latihan 2 C1 dalam 
mata kuliah DPBO untuk keberkahanNya maka saya tidak melakukan kecurangan
seperti yang telah dispesifikasikan. Aamiin */
include("Memory.php");
# mengimport kelas Memory

#instansiasi
$comp = new Memory();

# mengeset isi atribut dari kelas-kelas pada memory
$comp->setIdProduct(1);
$comp->setPrice(1000000);
$comp->setBrand("Macbook");
$comp->setModel("Macbook Pro");
$comp->setFrequency("2.0Ghz");
$comp->setMemorySize(8);
$comp->setSupportsCuda("Intel");

# mencetak atribut ada kelas-kelas yang ada di Memory
$comp->printProduct();
$comp->printHardware();
$comp->printMemory();
