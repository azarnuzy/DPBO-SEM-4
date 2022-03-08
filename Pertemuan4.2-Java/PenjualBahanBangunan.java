public class PenjualBahanBangunan {
    // kelas implementasi penjualBahanBangunan
    private String noKTP; // nomor KTP penjual
    private String nama; // nama penjual
    private int banyakToko; // banyaknya toko yang dimiliki penjual
    private Tokobangunan toko; // toko milik penjual

    PenjualBahanBangunan() {
        // konstruktor
    }

    PenjualBahanBangunan(String noKTP, String nama, int banyakToko) {
        // konstruktor
        this.noKTP = noKTP;
        this.nama = nama;
        this.banyakToko = banyakToko;
        this.toko = new TokoBangunan[banyakToko];
    }

    void setNoKTP(String noKTP) {
        this.noKTP = noKTP;
    }

    String getNoKTP() {
        return noKTP;
    }

    void setToko(TokoBangunan toko, int nomorToko) {
        this.toko[nomorToko] = toko;
    }

    TokoBangunan[] getToko() {
        return toko;
    }

    void cetakPenjual() {
        // menceteka data penjual dan semua toko bahan bangunan yang dimiliki
        System.out.println("===========================");
        System.out.println("Nama Penjual       :" + nama);
        System.out.println("No KTP Penjual     :" + noKTP);
        System.out.println("Toko yang dimiliki :");
        for (int i = 0; i < banyakToko; i++) {
            System.out.println(i);
            System.out.println("Nama Penjual       :" + nama);
            System.out.println("No KTP Penjual     :" + noKTP);
        }
    }
}
