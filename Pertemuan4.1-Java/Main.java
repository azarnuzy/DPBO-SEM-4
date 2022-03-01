import java.util.Scanner;

class Main{
    public static void main(String[] args) {
        int baris = 0, kolom=0, i=0, j=0, temp=0;

        Scanner sc = new Scanner(System.in);

        System.out.println("masukan baris");
        try{
            baris = sc.nextInt();
        }catch(Exception e){}

        System.out.println("masukan kolom");
        try{
            kolom = sc.nextInt();
        }catch(Exception e){}

        //inisialisasi matriks
        Matriks m = new Matriks(baris, kolom);
        m.setMat();
        
        //mengisi matriks
        for(i=0; i<baris; i++) {
            for(j=0; j<kolom; j++) {
                System.out.println("isikan angka:");
                try{
                    temp = sc.nextInt();
                    m.setSel(i, j, temp);
                }catch(Exception e){}
            }
        }

        //menampilkan matriks
        for(i=0; i<baris; i++) {
            for(j=0; j<kolom; j++) {
                System.out.print(m.getSel(i, j) + " ");
            }
            System.out.println("");
        }
    }
}