import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Memory comp1 = new Memory();
        String brand = "", model = "", frequency = "", supportsCuda = "";
        int price = 0, idProduct = 0, memorySize = 0;

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

        comp1.setIdProduct(idProduct);
        comp1.setPrice(price);
        comp1.setBrand(brand);
        comp1.setModel(model);
        comp1.setFrequency(frequency);
        comp1.setMemorySize(memorySize);
        comp1.setSupportsCuda(supportsCuda);

        System.out.println("\nOutput: ");
        comp1.printProduct();
        comp1.printHardware();
        comp1.printMemory();
    }
}