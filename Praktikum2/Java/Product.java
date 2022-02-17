class Product {
    private int price;
    private int idProduct;

    Product() {
    }

    public void setPrice(int price) {
        this.price = price;
    }

    public int getPrice() {
        return this.price;
    }

    public void setIdProduct(int idProduct) {
        this.idProduct = idProduct;
    }

    public int getIdProduct() {
        return this.idProduct;
    }

    public void printProduct() {
        System.out.println("Id Product : " + getIdProduct());
        System.out.println("Price : " + getPrice());
    }
}
