// kelas yang digunakan untuk mengimplementasikan Memory dan juga turunan dari
// kelas Hardware
class Memory extends Hardware {

    // private atribute dari kelas Memory
    private String frequency;
    private int memorySize;
    private String supportsCuda;

    // konstrutor
    Memory() {
    }

    // mengeset nilai atribut frequency
    public void setFrequency(String frequency) {
        this.frequency = frequency;
    }

    // mengembalikan nilai atribut frequency
    public String getFrequency() {
        return this.frequency;
    }

    // mengeset nilai atribut memorySize
    public void setMemorySize(int memorySize) {
        this.memorySize = memorySize;
    }

    // mengembalikan nilai atribut memorySize
    public int getMemorySize() {
        return this.memorySize;
    }

    // mengeset nilai atribut supportsCuda
    public void setSupportsCuda(String supportsCuda) {
        this.supportsCuda = supportsCuda;
    }

    // mengembalikan nilai atribut supportsCuda
    public String getSupportsCuda() {
        return this.supportsCuda;
    }

    // menampilkan atribut Memory
    public void printMemory() {
        System.out.println("Frequency : " + getFrequency());
        System.out.println("Memory Size : " + getMemorySize());
        System.out.println("Support Cuda : " + getSupportsCuda());
    }
}
