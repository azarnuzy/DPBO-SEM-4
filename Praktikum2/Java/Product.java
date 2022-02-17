class Product {
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
        System.out.println("Id Product : " + this.idProduct);
        System.out.println("Price : " + this.price);
    }
}
