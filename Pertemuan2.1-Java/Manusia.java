class Manusia {
    private String nama;
    private String alamat;
    private String no_ktp;
    private String no_telepon;

    Manusia() {
    }

    public void setNama(String nama) {
        this.nama = nama;
    }

    public String getNama() {
        return this.nama;
    }

    public void setAlamat(String alamat) {
        this.alamat = alamat;
    }

    public String getAlamat() {
        return this.alamat;
    }

    public void setNoKtp(String no_ktp) {
        this.no_ktp = no_ktp;
    }

    public String getNoKtp() {
        return this.no_ktp;
    }

    public void setNoTelepon(String no_telepon) {
        this.no_telepon = no_telepon;
    }

    public String getNoTelepon() {
        return this.no_telepon;
    }
}

class Karyawan extends Manusia {
    private String nomor_pegawai;
    private String jabatan;
    private String departemen;

    Karyawan() {
    }

    public void setNomorPegawai(String nomor_pegawai) {
        this.nomor_pegawai = nomor_pegawai;
    }

    public String getNomorPegawai() {
        return this.nomor_pegawai;
    }

    public void setJabatan(String jabatan) {
        this.jabatan = jabatan;
    }

    public String getJabatan() {
        return this.jabatan;
    }

    public void setDepartemen(String departemen) {
        this.departemen = departemen;
    }

    public String getDepartemen() {
        return this.departemen;
    }
}

class Main {
    public static void main(String[] args) {
        Manusia kmanusia;
        Karyawan kkaryawan;

        kmanusia = new Manusia();
        kmanusia.setNama("Gina");
        kmanusia.setAlamat("Bandung");
        kmanusia.setNoKtp("320.120.777");
        kmanusia.setNoTelepon("021123124");

        System.out.println(kmanusia.getNama());
        System.out.println(kmanusia.getAlamat());
        System.out.println(kmanusia.getNoKtp());
        System.out.println(kmanusia.getNoTelepon());
    }
}