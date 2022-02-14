import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        DaftarTimSepakbola daftar1 = new DaftarTimSepakbola();
        String nama = "", negara = "", tahunBerdiri = "", kiper = "", bek = "", gelandang = "", penyerang = "";
        System.out.println("Masukan Input: ");
        try {
            System.out.print("Nama: ");
            nama = sc.next();
        } catch (Exception e) {
        }
        try {
            System.out.print("Negara: ");
            negara = sc.next();
        } catch (Exception e) {
        }
        try {
            System.out.print("Tahun Berdiri: ");
            tahunBerdiri = sc.next();
        } catch (Exception e) {
        }
        try {
            System.out.print("Kiper: ");
            kiper = sc.next();
        } catch (Exception e) {
        }
        try {
            System.out.print("Bek: ");
            bek = sc.next();
        } catch (Exception e) {
        }
        try {
            System.out.print("Gelandang: ");
            gelandang = sc.next();
        } catch (Exception e) {
        }
        try {
            System.out.print("Penyerang: ");
            penyerang = sc.next();
        } catch (Exception e) {
        }
        System.out.println(nama);
        System.out.println("Output: ");
        daftar1.setNama(nama);
        daftar1.setNegara(negara);
        daftar1.setTahunBerdiri(tahunBerdiri);
        daftar1.printhasil();
        System.out.print("Kiper: ");
        daftar1.getPosisi().bek(kiper);
        System.out.print("Bek: ");
        daftar1.getPosisi().bek(bek);
        System.out.print("Gelandang: ");
        daftar1.getPosisi().bek(gelandang);
        System.out.print("Penyerang: ");
        daftar1.getPosisi().bek(penyerang);
    }
}
