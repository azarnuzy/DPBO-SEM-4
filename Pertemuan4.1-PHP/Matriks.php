<?php
class Matriks
{
    private $baris;
    private $kolom;
    private $mat;

    function __construct()
    {
    }

    function setBaris($baris)
    {
        $this->baris = $baris;
    }

    function getBaris()
    {
        return $this->baris;
    }

    function setKolom($kolom)
    {
        $this->kolom = $kolom;
    }

    function getKolom()
    {
        return $this->kolom;
    }

    function setMat($mat)
    {
        $this->mat = $mat;
    }

    function getMat()
    {
        return $this->mat;
    }

    function setSel($baris, $kolom, $nilai)
    {
        $this->mat[$baris][$kolom] = $nilai;
    }

    function getSel($baris, $kolom)
    {
        return $this->mat[$baris][$kolom];
    }
}
