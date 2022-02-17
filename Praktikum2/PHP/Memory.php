<?php
include("Hardware.php");
# import class Hardware

class Memory extends Hardware
# kelas yang digunakan untuk mengimplementasikan Memory dan juga turunan dari kelas Hardware
{
    # private atribute dari kelas Memory
    private $frequency = "";
    private $memorySize = 0;
    private $supportsCuda = "";

    # konstrutor
    public function __construct()
    {
    }

    # mengeset nilai atribut frequency
    public function setFrequency($frequency)
    {
        $this->frequency = $frequency;
    }

    # mengembalikan nilai atribut frequency
    public function getFrequency()
    {
        return $this->frequency;
    }

    # mengeset nilai atribut memorySize
    public function setMemorySize($memorySize)
    {
        $this->memorySize = $memorySize;
    }

    # mengembalikan nilai atribut memorySize
    public function getMemorySize()
    {
        return $this->memorySize;
    }

    # mengeset nilai atribut supportsCuda
    public function setSupportsCuda($supportsCuda)
    {
        $this->supportsCuda = $supportsCuda;
    }

    # mengembalikan nilai atribut supportsCuda
    public function getSupportsCuda()
    {
        return $this->supportsCuda;
    }

    # menampilkan atribut Memory
    public function printMemory()
    {
        echo "Supports Cuda: " . $this->getSupportsCuda() . "<br/>";
        echo "Memory Size: " . $this->getMemorySize() . "<br/>";
        echo "frequency: " . $this->getFrequency() . "<br/>";
    }
}
