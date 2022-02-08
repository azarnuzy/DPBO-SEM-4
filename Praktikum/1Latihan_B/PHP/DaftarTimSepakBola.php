<?php

class DaftarTimSepakBola
{
    private $nama = "";
    private $negara = "";
    private $tahun_berdiri = "";
    private $pemain = "";

    public function __construct($nama = "", $negara = "", $tahun_berdiri = "", $pemain = "")
    {
        $this->nama = $nama;
        $this->negara = $negara;
        $this->tahun_berdiri = $tahun_berdiri;
        $this->pemain = $pemain;
    }

    public function setNama($nama)
    {
        $this->nama = $nama;
    }

    public function getNama()
    {
        return $this->nama;
    }

    public function setNegara($negara)
    {
        $this->negara = $negara;
    }

    public function getNegara()
    {
        return $this->negara;
    }

    public function setTahunBerdiri($tahun_berdiri)
    {
        $this->tahun_berdiri = $tahun_berdiri;
    }

    public function getTahunBerdiri()
    {
        return $this->tahun_berdiri;
    }

    public function setPemain($pemain)
    {
        $this->pemain = $pemain;
    }

    public function getPemain()
    {
        return $this->pemain;
    }

    public function printHasil()
    {
        return "Nama: " . $this->getNama() . "<br/>" . "Negara: " . $this->getNegara() . "<br/>" . "Tahun Berdiri: " . $this->getTahunBerdiri() . "<br/>" . "Pemain: " . $this->getPemain() . "<br/>";
    }
}
