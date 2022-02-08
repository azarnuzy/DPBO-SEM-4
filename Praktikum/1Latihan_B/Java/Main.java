import java.util.*;

public class Main {
    public static void main(String[] args) {
        DaftarTimSepakbola daftar1 = new DaftarTimSepakbola();
        daftar1.setNama("Barcelona");
        daftar1.setNegara("Spanyol");
        daftar1.setTahunBerdiri("1887");
        daftar1.setPemain("Sergio Ramos");
        daftar1.printhasil();
        System.out.println();

        DaftarTimSepakbola daftar2 = new DaftarTimSepakbola("Manchester United", "England", "1847", "Wayne Rooney");
        daftar2.printhasil();

    }
}
