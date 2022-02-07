import java.util.Scanner;

class Calculator {
    private Operasi opr;

    Calculator() {
        opr = new Operasi();
    }

    Operasi getOpr() {
        return opr;
    }

    class Operasi {
        Operasi() {
        }

        int tambah(int x, int y) {
            return (x + y);
        }

        int kurang(int x, int y) {
            return (x - y);
        }

        int kali(int x, int y) {
            return (x * y);
        }

        int bagi(int x, int y) {
            if (y > 0) {
                return (x / y);
            } else {
                return -999999;
            }
        }
    }
}

class Main {
    public static void main(String[] args) {
        int menu = 0;
        int x = 0;
        int y = 0;

        Calculator cal = new Calculator();

        System.out.println("masukan menu: ");

        Scanner sc = new Scanner(System.in);

        try {
            menu = sc.nextInt();
        } catch (Exception e) {
        }
        System.out.println("masukan x");

        try {
            x = sc.nextInt();
        } catch (Exception e) {
        }
        System.out.println("masukkan y: ");

        try {
            y = sc.nextInt();
        } catch (Exception e) {
        }

        switch (menu) {
            case 1:
                System.out.println(cal.getOpr().tambah(x, y));
                break;
            case 2:
                System.out.println(cal.getOpr().kurang(x, y));
                break;
            case 3:
                System.out.println(cal.getOpr().kali(x, y));
                break;
            case 4:
                System.out.println(cal.getOpr().bagi(x, y));
                break;
        }
    }
}