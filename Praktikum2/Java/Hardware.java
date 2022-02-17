class Hardware extends Product {
    public void setBrand(String brand) {
        this.brand = brand;
    }

    public String getBrand() {
        return this.brand;
    }

    public void setModel(String model) {
        this.model = model;
    }

    public String getModel() {
        return this.model;
    }

    public void printHardware() {
        System.out.println("Brand : " + this.brand);
        System.out.println("Model : " + this.model);
    }
}
