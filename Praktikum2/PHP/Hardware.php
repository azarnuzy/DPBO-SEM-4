<?php
include("Product.php");
# import class product

class Hardware extends Product
# kelas yang digunakan untuk mengimplementasikan Hardware dan juga turunan dari kelas Product
{
    # private atribute dari kelas Hardware
    private $brand = "";
    private $model = "";

    # konstrutor
    public function __construct()
    {
    }

    # mengeset nilai atribut brand
    public function setBrand($brand)
    {
        $this->brand = $brand;
    }

    # mengembalikan nilai atribut brand
    public function getBrand()
    {
        return $this->brand;
    }

    # mengeset nilai atribut model
    public function setModel($model)
    {
        $this->model = $model;
    }

    # mengembalikan nilai atribut model
    public function getModel()
    {
        return $this->model;
    }

    # menampilkan atribut Hardware
    public function printHardware()
    {
        echo "Model: " . $this->getModel() . "<br/>";
        echo "Brand: " . $this->getBrand() . "<br/>";
    }
}
