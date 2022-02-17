// kelas yang digunakan untuk mengimplementasikan product
class Product {
    // private atribute dari kelas product
    private int price;
    private int idProduct;

    // konstrutor
    Product() {
    }

    // mengeset nilai atribut price
    public void setPrice(int price) {
        this.price = price;
    }

    // mengembalikan nilai atribut price
    public int getPrice() {
        return this.price;
    }

    // mengeset nilai atribut idProduct
    public void setIdProduct(int idProduct) {
        this.idProduct = idProduct;
    }

    // mengembalikan nilai atribut idProduct
    public int getIdProduct() {
        return this.idProduct;
    }

    // menampilkan atribut product
    public void printProduct() {
        System.out.println("Id Product : " + getIdProduct());
        System.out.println("Price : " + getPrice());
    }
}
