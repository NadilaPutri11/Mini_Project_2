from prettytable import PrettyTable

print("Gaji karyawan Rp 300.000/jam, jika lembur dibayar gaji jam normal + 1/2 kali lipat fari gaji normal unutuk perjam lemburnya, jadi dibayar Rp 450.000/jam untuk jam lembur")
karyawan_list = [
    {"ID": 1122, "Nama": "nana", "Jam Kerja Normal" : 40, "Gaji Pokok" : 12000000, "Jam Lembur": 0, "Gaji Lembur" : 0, "Total Gaji" : 12000000 },
    {"ID": 2233, "Nama": "rene", "Jam Kerja Normal" : 35, "Gaji Pokok" : 10500000, "Jam Lembur": 0, "Gaji Lembur" : 0, "Total Gaji" : 10500000 },
]

# Fungsi-fungsi untuk CRUD Admin ke karyawan_list
# Fungsi untuk menambah karyawan
def tambah_karyawan():
    global karyawan_list
    id_karyawan = input("Masukkan ID karyawan:")
    nama_karyawan = input("Masukkan Nama karyawan:")
    jam_kerja = int(input("Masukkan Jam Kerja Normal:"))
    gaji_pokok = jam_kerja * 300000
    jam_lembur = int(input("Masukkan Jam Lembur:"))
    gaji_lembur = jam_lembur * 450000
    total_gaji = gaji_pokok + gaji_lembur

    karyawan = {
        "ID": id_karyawan,
        "Nama": nama_karyawan,
        "Jam Kerja Normal": jam_kerja,
        "Gaji Pokok": gaji_pokok,
        "Jam Lembur": jam_lembur,
        "Gaji Lembur": gaji_lembur,
        "Total Gaji": total_gaji,
    }
    karyawan_list.append(karyawan)
    print("Data karyawan baru telah ditambahkan")

# Fungsi untuk menampilkan data karyawan
def data_karyawan():
    if not karyawan_list:
        print("Belum ada data karyawan.")
    else:
        table = PrettyTable()
        table.field_names = ["Index", "ID", "Nama", "Jam Kerja Normal", "Gaji Pokok", "Jam Lembur", "Gaji Lembur", "Total Gaji"]
        for i, karyawan in enumerate(karyawan_list):
            table.add_row([
                i, 
                karyawan['ID'], 
                karyawan['Nama'], 
                karyawan['Jam Kerja Normal'], 
                karyawan['Gaji Pokok'], 
                karyawan['Jam Lembur'], 
                karyawan['Gaji Lembur'], 
                karyawan['Total Gaji'],
            ])
        print(table)

# Fungsi untuk mengedit data karyawan
def edit_data_karyawan():
    data_karyawan()
    index = int(input("Masukkan index:"))
    if 0 <= index < len(karyawan_list):
        print("Pilih data yang ingin di edit\n1. Nama\n2. Jam Kerja Normal\n3. Jam Lembur")
        pilihan = int(input("Masukkan angka:"))
        if pilihan == 1 :
            nama_baru = input("Masukkan nama baru:")
            karyawan_list[index]["Nama"] = nama_baru
        elif pilihan == 2 :
            jam_kerja_baru = int(input("Masukkan jam kerja baru:"))
            karyawan_list[index]["Jam Kerja Normal"] = jam_kerja_baru
            gaji_pokok_baru = jam_kerja_baru * 450000
            karyawan_list[index]["Gaji Pokok"] = gaji_pokok_baru
            karyawan_list[index]["Total Gaji"] = gaji_pokok_baru
        elif pilihan == 3 :
            jam_lembur_baru = int(input("Masukkan jam lembur baru:"))
            karyawan_list[index]["Jam Lembur"] = jam_lembur_baru
            gaji_lembur_baru = jam_lembur_baru * 450000
            karyawan_list[index]["Gaji Lembur"] = gaji_lembur_baru
            karyawan_list[index]["Total Gaji"] = gaji_lembur_baru + karyawan_list[index]["Gaji Pokok"]
        print("Data karyawan telah diperbarui.")
    else:
        print("Index tidak valid.")

# Fungsi untuk menghapus data karyawan
def hapus_karyawan():
    data_karyawan()
    index = int(input("Masukkan index:"))
    if 0 <= index < len(karyawan_list):
        data = karyawan_list.pop(index)
        print(f"Data {data['Nama']} telah dihapus.")
    else:
        print("Index tidak valid.")

# Fungsi untuik admin
def admin_menu():
    # Username dan password admin
    username = "admin"
    password = "1111"

    print("\n=== Login Admin ===")
    iuser = input("Username: ").lower()
    ipass = input("Password: ")

    # Memeriksa apakah username dan password sesuai
    if iuser == username and ipass == password:
        print("Login berhasil.")
        while True:
            print("\n=== Menu Admin ===")
            print("1. Tambah karyawan\n2. Tampilkan semua data karyawan\n3. Update data karyawan\n4. Hapus data karyawan\n5. Keluar")

            pilihan = input("Masukkan pilihan (1,2,3,4,5): ")

            if pilihan == "1":
                tambah_karyawan()
            elif pilihan == "2":
                data_karyawan()
            elif pilihan == "3":
                edit_data_karyawan()
            elif pilihan == "4":
                hapus_karyawan()
            elif pilihan == "5":
                print("Anda telah keluar dari Menu Admin.")
                break
            else:
                print("Pilihan tidak valid. Silahkan masukkan pilihan yang benar.")
    else:
        print("Username atau password Anda salah. Silahkan coba lagi.")

# Fungsi untuk karyawan
def karyawan_menu():
    print("\n=== Login Karyawan ===")
    iuser = input("Masukkan nama karyawan: ").lower()
    karyawan = None
    for k in karyawan_list:
        if k["Nama"] == iuser:
            karyawan = k
            break
    
    if karyawan:
        print("Login berhasil.")
        while True:
            print("\n=== Menu karyawan ===")
            print("1. Lihat Data Anda\n2. Keluar")

            pilihan = input("Masukkan pilihan (1/2): ")

            if pilihan == "1":
                table = PrettyTable()
                table.field_names = ["ID", "Nama", "Jam Kerja Normal", "Gaji Pokok", "Jam Lembur", "Gaji Lembur", "Total Gaji"]
                table.add_row([
                    karyawan["ID"],
                    karyawan["Nama"],
                    karyawan["Jam Kerja Normal"],
                    karyawan["Gaji Pokok"],
                    karyawan["Jam Lembur"],
                    karyawan["Gaji Lembur"],
                    karyawan["Total Gaji"]
                ])
                print(table)
            elif pilihan == "2":
                print("Anda telah keluar dari Menu Karyawan.")
                break
            else:
                print("Pilihan tidak valid. Silahkan masukkan pilihan yang benar.")
    else:
        print("Nama karyawan tidak ditemukan. Silahkan coba lagi.")

# Fungsi utama
def main():
    while True:
        print("\n=== Selamat datang di Sistem Upah Karyawan ===")
        print("1. Admin\n2. Karyawan\n3. Keluar")

        pilihan_user = input("Silahkan Anda pilih login sebagai apa (1/2/3): ")

        if pilihan_user == "1":
            admin_menu()
        elif pilihan_user == "2":
            print("\n=== Sign In or Log out ===")
            print("1. Login\n2. Keluar")

            pilihan = input("Silahkan pilih opsi Anda (1/2): ")

            if pilihan == "1":
                karyawan_menu()
            elif pilihan == "2":
                print("Selamat menerima gaji.")
                break
            else:
                print("Pilihan tidak valid. Silahkan masukkan pilihan yang benar.")
        elif pilihan_user == "3":
            print("Terima kasih telah menggunakan program ini.")
            break
        else:
            print("Pilihan tidak valid. Silahkan masukkan pilihan yang benar.")

# Memanggil main
if __name__ == "__main__":
    main()
