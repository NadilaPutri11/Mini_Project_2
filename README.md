# Mini_Project_2
nama : Nadila Putri nim: 2409116052

# FlowChart
![Minpro2SUK](https://github.com/user-attachments/assets/fa102296-f51f-46f6-a56f-89b9cb860a8f)

# Penjelasan Program dan Output

1. Keterangan untuk sistem perhitungan gaji dan list karyawan
   ![Cuplikan layar 2024-10-14 210248](https://github.com/user-attachments/assets/84c9e492-4cfb-41f0-9e58-fe7989aeb0ca)
Penjelasan: 
- di line 1 ada fungsi untuk mengimpor-memanggil library PrettyTable
- line 3-4 menampilkan perrnyataan mengenai bagaimana gaji dihitung
- line 5-8 adalah list dari karyawan yang didalamnya terdapat beberapa dictionary
2. Fungsi-fungsi untuk CRUD Admin
3. Fungsi Create pertama ada tambah_karyawan
   ![Cuplikan layar 2024-10-14 205845](https://github.com/user-attachments/assets/7b8418ba-faad-4d78-a5c8-ebbe41efbcf6)
Penjelasan: 
- line 12 membuat fungsi def tambah_karyawan()
- line 13 menuliskan variable global yang bisak diakses dari semua fungsi untuk karyawan list yang akan ditambah nanti (karena jika logout dari akun admin dan login kembali sebagai karyawan data yang telah ditambah akan hilang tanpa variable global)
- line 14-32 berisi perintah2 yang harus dijalankan jika admin memilih fungsi tambah_karyawan().
    - line 14-20 untuk input dari admin dan rumus perhitungan gaji.
    - line 22-29 untuk membuat dictionary berdasarkan input admin di line 14-20
    - line 30 perintah untuk menambahkan dictionary karyawan ke karyawan list
    - line 31 menampilkan statement bahwa "karyawan telah ditambahkan"
4. Fungsi Read kedua ada menampilkan data_karyawan
   ![Cuplikan layar 2024-10-14 210622](https://github.com/user-attachments/assets/7a9067f3-b33a-41ac-ade9-fbc6a72e14e6)
Penjelasan: 
- line 35 membuat fungsi def data_karyawan()
- line 36-37 mengecek apakah datasa kosong, jika kosong maka program akan menampilkan "Belum ada data karyawan."
- line 38 jika program memiliki isi maka line 39-52 akan dijalankan
  - line 39 membuat variable untuk PrettyTablenya
  - line 40 membuat nama-nama untuk kolom
  - line 41 mengiterasi elemen di karyawan_list bersamaan dengan indeksnya
  - line 42 menambahkan baris untuk table dari data yang ada di karyawan_list
  - line 43-51 isi dari baris yang dibuat sesuai dengan data yang ada di karyawan list
  - line 52 perintah untuk menampilkan tabel yang telah dibuat
5. Fungsi Update ketiga ada edit_data_karyawan
   ![Cuplikan layar 2024-10-14 220833](https://github.com/user-attachments/assets/e7f25d9a-cf38-4f74-829d-65d1e04815af)
Penjelasan: 
- line 55 membuat fungsi def edit_data_karyawan()
- line 56 memanggil fungsi data_karyawan()
- line 57 meminta input dari admin mengenai data di indeks berapa yang ingin di edit
- line 58 membuat kondisi untuk index yang dimasukkan oleh pengguna masih dikisaran index yang ada
- line 59-76 menjalankan perintah untuk kondisi lagi jika kondisi index terpenuhi
  - line 59 menampilkan pilihan yang ingin diubah admin sperti 1. Nama 2. Jam Kerja Normal 3. Jam Lembur
  - line 60 meminta input dari admin apa yang ingin diubah
  - line 61-63 jika admin memilih pilihan no 1, maka akan diminta input untuk nama baru dan menjalankan perintah untuk mengubah data nama_karyawan sesuai dengan input nama baru
  - line 64-69 jika admin memilih pilihan no 2, maka akan diminta input untuk jam kerja normal yang baru dan menjalankan perintah untuk mengubah data jam_kerja sesuai dengan input jam kerja normal yang baru. Selain jam kerja normal, pilihan ini juga akan mengubah gaji pokok dan total gaji sesuai dengan rumus perintah ketentuan gajinya
  - line 70-75 jika admin memilih pilihan no 3, maka akan diminta input untuk jam lembur yang baru dan menjalankan perintah untuk mengubah data jam_lembur sesuai dengan input jam lembur yang baru. Selain jam kerja normal, pilihan ini juga akan mengubah gaji lembur dan total gaji sesuai dengan rumus perintah ketentuan gajinya
  - line 76 dari masing2 pilihan itu akan menampilkan statement "Data karyawan telah diperbarui." jika data berhasil diperbarui
- line 77-78 jika input tidak memenuhi kondisi indeks yang ada maka akan menampilkan statement "Index tidak valid."

6. Fungsi Delete keempat ada hapus_karyawan()
   ![Cuplikan layar 2024-10-14 222345](https://github.com/user-attachments/assets/bdb71624-ff64-4b8b-8bba-b04c10e827ba)
Penjelasan: 
- line 81 membuat fungsi def hapus_karyawan()
- line 82 memanggil fungsi data_karyawan()
- line 83 meminta input dari admin index baris brp yang ingin dihapus
- line 84 memeriksa apakah no indesk yang di input ada dalm data atau tidak, line 85 membuat variable untuk indeks yang dihapus. line 86 menampilkan nama karyawan yang telah dihapus
- line 87-88 jika input tidak memenuhi kondisi indeks yang ada maka akan menampilkan statement "Index tidak valid."
7. Fungsi untuk menu admin
   ![Cuplikan layar 2024-10-14 222417](https://github.com/user-attachments/assets/ec801259-1a2b-49b5-a032-663de135b102)
Penjelasan: 
- line 91 membuat fungsi def admin_menu()
- line 93-94 variable untuk username dan password admin
- line 96-98 untuk input user login sebagai admin
- line 101-121 jika user memenuhi kondisi dimana input username dan passwordnya sesuai dengan value dari variable line 93-94 maka akan diarahkan ke while True dimana program akan terulang selama bernilai benar
Contoh Output:
![Cuplikan layar 2024-10-15 003011](https://github.com/user-attachments/assets/15e573db-e049-40b4-8f86-f7c944b185c8)
  - line 107 untuk user menginput pilihan dari menu yang ada
  - line 109-110 jika user memilih no 1 maka akan diarahkan ke tambah_karyawan()
Contoh Output:
![Cuplikan layar 2024-10-15 003449](https://github.com/user-attachments/assets/d6bbe50e-f926-4599-8c10-bfd50938801b)
  - line 111-112 jika user memilih no 2 maka akan diarahkan ke data_karyawan()
Contoh Output:
![Cuplikan layar 2024-10-15 003600](https://github.com/user-attachments/assets/849abe5a-bcd8-4c1f-a4a3-9335774ae6e3)
  - line 113-114 jika user memilih no 3 maka akan diarahkan ke edit_data_karyawan()
Contoh Output:
![Cuplikan layar 2024-10-15 003743](https://github.com/user-attachments/assets/01bca62f-2aac-49be-ae3a-baa123a093e6)
data yang saya edit hannya nama jadi hanya nama yang berubah, jika memilih jam kerja maka gaji pokok dan total gaji akan berubah, jika merubah jam lembur maka gaji pokok dan gaji lembur lalu ada total gaji yang akan berubah
  - line 115-116 jika user memilih no 4 maka akan diarahkan ke hapus_karyawan()
Contoh Output:
![Cuplikan layar 2024-10-15 003855](https://github.com/user-attachments/assets/2a142abe-3dac-4208-8586-b513f0e82c13)
cukup mengisi nomor index yang ingin dihapus maka 1 baris dari indeks yang ingin dihapus akan terhapus
  - line 117-118 jika user memilih no 5 maka akan muncul statement "Anda telah keluar dari Menu Admin."
Contoh Output:
![Cuplikan layar 2024-10-15 003954](https://github.com/user-attachments/assets/933df00d-0c1e-4752-aa5e-8ec5225b2e14)
  - line 119 break untuk menghentikan perulangan line 107, user akan kembali ke fungsi utama
  - line 120-121 jika user menginput angka selain dari 1-5 maka akan muncul statement "Pilihan tidak valid. Silahkan masukkan pilihan yang benar." dan akan kembali ke line 107
    Contoh Output:
![Cuplikan layar 2024-10-15 004214](https://github.com/user-attachments/assets/f7bb259b-7f77-497c-b7a1-d66e1492a3c3)
- line 122-123 jika user tidak memenuhi kondisi dimana input useername dan passwordnya harus sesuai dengan value dari variable line 93-94 maka akan muncul "Username atau password Anda salah. Silahkan coba lagi." dan user akan kembali ke fungsi utama
Contoh Output:
![Cuplikan layar 2024-10-15 004449](https://github.com/user-attachments/assets/c5bbe899-3a2a-476f-92fe-8abfc890667b)


8. Fungsi untuk menu karyawan
  ![Cuplikan layar 2024-10-14 233012](https://github.com/user-attachments/assets/c321aa56-157d-417d-a9ce-0ab68a4d86ae)
Penjelasan: 
- line 126 membuat fungsi def karyawan_menu()
- line 128 untuk user menginput namanya juga ditambahkan method lower agar walaupun user menginput dengan kapital, data yang masuk akan diubah menjadi huruf kecil
- line 129-133 untuk memeriksa inputan user apakah namanya ada di karyawan_list atau tidak
- line 135-160 jika nama user ada di karyawan_list maka user berhasil login dan menu karyawan akan muncul
  - line 141 meminta input dari user apakah ingin melihat data diri ata keluar dari program
  - line 143-155 jika user memilih no 1 maka table data diri user yang login sebagai karyawan tersebut akan muncul dalam bentuk table
  Contoh Output:
  ![Cuplikan layar 2024-10-15 004717](https://github.com/user-attachments/assets/24c48c8a-74f7-43fc-a0d4-1027c97bb285)
  - line 156-157 jika user memilih no 2 maka akan muncul statement "Anda telah keluar dari Menu Karyawan."
  - line 158 break untuk menghentikan perulangan dan user akan kembali ke fungsi utama
  Contoh Output:
  ![Cuplikan layar 2024-10-15 004834](https://github.com/user-attachments/assets/1cce5dd9-58f6-4702-896c-ff26e0057a92)
- line 161-162 jika nama user tidak ada di karyawan_list maka akan muncul "Nama karyawan tidak ditemukan. Silahkan coba lagi." dan kembali ke line 128
Contoh Output:
![Cuplikan layar 2024-10-15 004958](https://github.com/user-attachments/assets/d947f9f6-f784-4c52-be29-b77f887ba351)

 9. Fungsi utama
    ![Cuplikan layar 2024-10-14 235553](https://github.com/user-attachments/assets/82ec6ea8-56ea-4821-83eb-1dc4a63eccc0)
Penjelasan: 
- line 165 membuat fungsi def main()
- line 166 membuat while True dimana program akan terulang selama bernilai benar
- line 170 untuk user mengisi inputan ingin login sebagai apa
Contoh Output:
![Cuplikan layar 2024-10-15 002651](https://github.com/user-attachments/assets/33d9157f-663e-4952-95f4-5e2ccecc0d5b)
- line 172-173 jika user memilih no 1 maka user akan diarahkan ke login admin di admin_menu()
Contoh Outputada di bagian admin_menu
- line 174-176 jike user memilih no 2 maka user akan ditanya apakah ingin 1. login karyawan atau 2. keluar
  - line 178 program untuk user menginput pilihannya
  - line 180-181 jika user memilih no 1 maka akan diarahkan ke karyawan_mmenu()
  - line 182-184 jika user memilih no 2 maka akan muncul "Anda telah keluar dari program Karyawan." dan perulangan berhenti karena break, anda akan kembali ke line 170
  Contoh Outputada di bagian karyawan_menu
  - line 185-186 jika user menginput selain 1 atau 2 maka akan muncul "Pilihan tidak valid. Silahkan masukkan pilihan yang benar."
- line 187-189 jike user memilih no 3 maka user akan keluar dari seluruh program, break di line 189 akan menghentikan program perulangan seluruhnya dan memunculkan statement "Terima kasih telah menggunakan program ini."
Contoh Output:
![Cuplikan layar 2024-10-15 005457](https://github.com/user-attachments/assets/9e64e09d-ecd8-4cad-8c7e-f185876c45e7)

- line 190-191 jika user menginput nomor selain 1,2,3 maka akan muncul statement "Pilihan tidak valid. Silahkan masukkan pilihan yang benar." dan program akan kembali ke line 170
![Cuplikan layar 2024-10-15 005554](https://github.com/user-attachments/assets/52473dcb-2a68-4af9-87d7-f4aba58f54c8)

    
10. Memanggil fungsi utama
    ![Cuplikan layar 2024-10-15 001558](https://github.com/user-attachments/assets/590b3320-5061-4470-8702-2a1c8f5df499)
Penjelasan: 
- line 194-195 memanggil-menjalankan logika utama program
