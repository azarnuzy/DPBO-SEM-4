<?php
class Product
# kelas yang digunakan untuk mengimplementasikan product
{
    # private atribute dari kelas product
    private $price = 0;
    private $idProduct = 0;

    # konstrutor
    public function __construct()
    {
    }

    # mengeset nilai atribut price
    public function setPrice($price)
    {
        $this->price = $price;
    }

    # mengembalikan nilai atribut price
    public function getPrice()
    {
        return $this->price;
    }

    # mengeset nilai atribut idProduct
    public function setIdProduct($idProduct)
    {
        $this->idProduct = $idProduct;
    }

    # mengembalikan nilai atribut idProduct
    public function getIdProduct()
    {
        return $this->idProduct;
    }

    # menampilkan atribut product
    public function printProduct()
    {
        echo "Id Product: " . $this->getIdProduct() . "<br/>";
        echo "Price: " . $this->getPrice() . "<br/>";
    }
}
