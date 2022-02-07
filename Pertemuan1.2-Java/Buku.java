class Buku {
    private String judul;
    private String pengarang;

    Buku() {
    }

    Buku(String j, String p) {
        this.judul = j;
        this.pengarang = p;
    }

    void setJudul(String j) {
        this.judul = j;
    }

    void setPengarang(String p) {
        this.pengarang = p;
    }

    String getJudul() {
        return this.judul;
    }

    String getPengarang() {
        return this.pengarang;
    }
}

class Main {
    public static void main(String[] args) {
        Buku b1;
        Buku b2;

        b1 = new Buku();
        b1.setJudul("J2ME");
        b1.setPengarang("Orang_1");
        System.out.println(b1.getJudul());
        System.out.println(b1.getPengarang());

        b2 = new Buku("J2EE", "Orang_2");
        System.out.println(b2.getJudul());
        System.out.println(b2.getPengarang());
    }
}