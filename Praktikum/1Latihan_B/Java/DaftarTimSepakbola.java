public class DaftarTimSepakbola {
    private String nama;
    private String negara;
    private String tahun_berdiri;
    private Pemain posisi;

    public DaftarTimSepakbola() {
        posisi = new Pemain();
    }

    Pemain getPosisi() {
        return posisi;
    }

    class Pemain {
        Pemain() {
        }

        String kiper(String nama) {
            return nama;
        }

        String bek(String nama) {
            return nama;
        }

        String gelandang(String nama) {
            return nama;
        }

        String penyerang(String nama) {
            return nama;
        }
    }

    public DaftarTimSepakbola(String nama, String negara, String tahun_berdiri/* , String pemain */) {
        this.nama = nama;
        this.negara = negara;
        this.tahun_berdiri = tahun_berdiri;
        // this.pemain = pemain;
    }

    public void setNama(String nama) {
        this.nama = nama;
    }

    public String getNama() {
        return this.nama;
    }

    public void setNegara(String negara) {
        this.negara = negara;
    }

    public String getNegara() {
        return this.negara;
    }

    public void setTahunBerdiri(String tahun_berdiri) {
        this.tahun_berdiri = tahun_berdiri;
    }

    public String getTahunBerdiri() {
        return this.tahun_berdiri;
    }

    /*
     * public void setPemain(String pemain) {
     * this.pemain = pemain;
     * }
     * 
     * public String getPemain() {
     * return this.pemain;
     * }
     */

    public void printhasil() {
        System.out.println("Nama : " + this.nama);
        System.out.println("Negara : " + this.negara);
        System.out.println("Tahun Berdiri : " + this.tahun_berdiri);
        // System.out.println("Pemain : " + this.pemain);
    }
}
