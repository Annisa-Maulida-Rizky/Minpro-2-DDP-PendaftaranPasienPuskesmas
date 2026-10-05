import pwinput
import os
from prettytable import PrettyTable

users = {
    "admin": {
        "password": "admin123",
        "role": "admin"
    },
    "user": {
        "password": "user123",
        "role": "user"
    }
}

Menu = ("1. Daftar Pasien Baru", "2. Ubah Data Pasien",
        "3. Hapus Data Pasien", "4. Lihat Data Pasien",
        "5. Logout")

Data_Pasien = []

os.system("cls" if os.name == "nt" else "clear")

def login():
    while True:
        print("==== Selamat Datang, Silahkan Login ====")

        username = input("Username (ketik keluar untuk berhenti): ")

        if username == "keluar":
            return "keluar"

        password = pwinput.pwinput("Password: ")

        if username in users:
            if password == users[username]["password"]:
                print("Login berhasil!")
                print("Role Anda:", users[username]["role"])
                return users[username]["role"]
            else:
                print("Password salah!")
                print("Silahkan coba login lagi.")
        else:
            print("Username tidak ditemukan!")
            print("Silahkan coba login lagi.")

while True:
    role = login()
    if role == "keluar":
        break

    print("Tampilan Menu: ")

    for i in Menu:
        print(i)

    while True:
        A_menu = input("Silahkan memilih Menu: ")
        if A_menu == "1":
            Nama = (input("Masukkan nama pasien: "))
            umur = int(input("Masukkan umur pasien: "))
            keluhan = (input("Masukkan keluhan pasien: "))

            if keluhan == "gigi":
                poli = "Poli Gigi"

            elif umur < 17:
                poli = "Poli Anak"

            else:
                poli = "Poli Umum"

            pasien = {
                "Nama": Nama,
                "Umur": umur,
                "Keluhan": keluhan,
                "Poli": poli
            }

            Data_Pasien.append(pasien)

            print(f"Pendaftaran pasien '{Nama}' berhasil!")
            print(f"Silahkan menuju {poli}.")
            
        elif A_menu == "2":
            if role == "admin":
                Cari_nama = (input(
                    "Masukkan nama pasien yang ingin diubah: "
                ))
                for pasien in Data_Pasien:
                    if pasien["Nama"] == Cari_nama:
                        nama_baru = (input("Masukkan nama baru pasien: "))
                        umur_baru = int(input("Masukkan umur baru pasien: "))
                        keluhan_baru = (input("Masukkan keluhan baru pasien: "))

                        if keluhan_baru == "gigi":
                            poli_baru = "Poli Gigi"

                        elif umur_baru < 17:
                            poli_baru = "Poli Anak"

                        else:
                            poli_baru = "Poli Umum"

                        pasien["Nama"] = nama_baru
                        pasien["Umur"] = umur_baru
                        pasien["Keluhan"] = keluhan_baru
                        pasien["Poli"] = poli_baru
                    
                        print("Data pasien berhasil diubah!")
                        break

                else:
                    print("Nama atau data pasien tidak valid, "
                          "silahkan memilih ulang")

            else:
                print("Anda tidak memiliki akses untuk mengubah data.")

        elif A_menu == "3":

            if role == "admin":
                Cari_nama = (input("Masukkan nama pasien yang ingin dihapus: "))

                for pasien in Data_Pasien:
                    if pasien["Nama"] == Cari_nama:
                        Data_Pasien.remove(pasien)
                        print("Pasien berhasil dihapus dari daftar")
                        break

                else:
                    print("Nama pasien tidak valid")

            else:
                print("Anda tidak memiliki akses untuk menghapus data.")

        elif A_menu == "4":

            print("Daftar data pasien:")

            if not Data_Pasien:
                print("Belum ada data pasien")

            else:
                tabel = PrettyTable()
                tabel.field_names = ["Nama", "Umur", "Keluhan", "Poli"]   

                for pasien in Data_Pasien:
                    tabel.add_row([
                     pasien["Nama"],
                     pasien["Umur"],
                     pasien["Keluhan"],
                     pasien["Poli"]    
                ])
                print(tabel)

        elif A_menu == "5":
            print("Logout berhasil.")
            break

        else:
            print(
                "Pilihan tidak valid. "
                "Harap pilih ulang sesuai menu yang disediakan."
            )