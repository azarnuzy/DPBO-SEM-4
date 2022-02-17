// kelas yang digunakan untuk mengimplementasikan Hardware dan juga turunan dari
// kelas Product
class Hardware extends Product {

    // private atribute dari kelas Hardware
    private String brand;
    private String model;

    // konstruktor
    Hardware() {
    }

    // mengeset nilai atribut brand
    public void setBrand(String brand) {
        this.brand = brand;
    }

    // mengembalikan nilai atribut brand
    public String getBrand() {
        return this.brand;
    }

    // mengeset nilai atribut model
    public void setModel(String model) {
        this.model = model;
    }

    // mengembalikan nilai atribut model
    public String getModel() {
        return this.model;
    }

    // menampilkan atribut Hardware
    public void printHardware() {
        System.out.println("Brand : " + getBrand());
        System.out.println("Model : " + getModel());
    }
}
