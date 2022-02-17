
/*Saya Muhammad Azar Nuzy 2004191 mengerjakan Latihan 2 C1 dalam 
mata kuliah DPBO untuk keberkahanNya maka saya tidak melakukan kecurangan
seperti yang telah dispesifikasikan. Aamiin*/
// mengimport kelas utility
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // variabel untuk masukan
        Scanner sc = new Scanner(System.in);
        // instansiasi
        Memory comp1 = new Memory();
        // variabel untuk masukan
        String brand = "", model = "", frequency = "", supportsCuda = "";
        int price = 0, idProduct = 0, memorySize = 0;

        // input untuk setiap atribut yang ada
        System.out.println("Input: ");
        try {
            System.out.print("Id Product: ");
            idProduct = sc.nextInt();
        } catch (Exception e) {
        }
        try {
            System.out.print("Price: ");
            price = sc.nextInt();
        } catch (Exception e) {
        }
        try {
            System.out.print("Brand: ");
            brand = sc.next();
        } catch (Exception e) {
        }
        try {
            System.out.print("Model: ");
            model = sc.next();
        } catch (Exception e) {
        }
        try {
            System.out.print("Frequency: ");
            frequency = sc.next();
        } catch (Exception e) {
        }
        try {
            System.out.print("Memory Size: ");
            memorySize = sc.nextInt();
        } catch (Exception e) {
        }
        try {
            System.out.print("Supports Cuda: ");
            supportsCuda = sc.next();
        } catch (Exception e) {
        }

        // mengeset isi atribut dari kelas-kelas pada memory
        comp1.setIdProduct(idProduct);
        comp1.setPrice(price);
        comp1.setBrand(brand);
        comp1.setModel(model);
        comp1.setFrequency(frequency);
        comp1.setMemorySize(memorySize);
        comp1.setSupportsCuda(supportsCuda);

        // variabel untuk melakukan pengecekan apakah akan lanjut input atau berhenti
        System.out.println("\nOutput: ");
        comp1.printProduct();
        comp1.printHardware();
        comp1.printMemory();
    }
}