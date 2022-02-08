<?php

class DaftarMahasiswa
{
    private $NIM = "";
    private $nama = "";
    private $jenisKelamin = "";
    private $prodi = "";
    private $semester = "";

    public function __construct($NIM = "", $nama = "", $jenisKelamin = "", $prodi = "", $semester = "")
    {
        $this->NIM = $NIM;
        $this->nama = $nama;
        $this->jenisKelamin = $jenisKelamin;
        $this->prodi = $prodi;
        $this->semester = $semester;
    }

    public function setNIM($NIM)
    {
        $this->NIM = $NIM;
    }

    public function getNIM()
    {
        return $this->NIM;
    }

    public function setNama($nama)
    {
        $this->nama = $nama;
    }

    public function getNama()
    {
        return $this->nama;
    }

    public function setJenisKelamin($jenisKelamin)
    {
        $this->jenisKelamin = $jenisKelamin;
    }

    public function getJenisKelamin()
    {
        return $this->jenisKelamin;
    }

    public function setProdi($prodi)
    {
        $this->prodi = $prodi;
    }

    public function getProdi()
    {
        return $this->prodi;
    }

    public function setSemester($semester)
    {
        $this->semester = $semester;
    }

    public function getSemester()
    {
        return $this->semester;
    }

    public function printHasil()
    {
        return "NIM: " . $this->getNIM() . "<br/>" . "Nama: " . $this->getNama() . "<br/>" . "Jenis Kelamin: " . $this->getJenisKelamin() . "<br/>" . "Program Studi: " . $this->getProdi() . "<br/>" . "Semester: " . $this->getSemester() . "<br/>";
    }
}
