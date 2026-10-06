# Minpro-2-DDP-PendaftaranPasienPuskesmas

Nama : Annisa Maulida Rizky<br>
NIM : 2609116061

# PENJELASAN SINGKAT
Program ini adalah sistem pendaftaran pasien di puskesmas, yang memungkinkan pengguna untuk menambah, melihat, mengubah, dan menghapus data pasien. Terdapat dua jenis pengguna, yaitu admin dan user yang memiliki akses berbeda. Dimana jika admin bisa menambah, melihat, mengubah dan menghapus data, sedangkan user hanya bisa menambah dan melihat data. Program ini dilengkapi dengan login, pengecekan input, dan tampilan tabel data pasien untuk memudahkan pengelolaan data. 

# FLOWCHART

<img width="2500" height="1890" alt="FCMINPRO2 drawio" src="https://github.com/user-attachments/assets/18278447-fd8f-423d-b082-8eb47e3456ff" />


## Penjelasan:
1. MULAI: Program dimulai
   
   Halaman login: Sistem menampilkan menu login dan meminta pengguna untuk menginput username dan password.
2. Proses Login: Sistem mengecek apakah login sebagai admin atau sebagai user. Jika username atau password salah maka           login gagal dan meminta menginput ulang. jika berhasil maka akann menampilkan 'login berhasil' dan role. 
3. Tampilkan Menu 1-5: 1. daftar pasien baru, 2. ubah pasien, 3. hapus pasien, 4. lihat pasien, dan 5. logout

   (Perulangan)
4. Input menu 1-5: user diminta menginput menu antara 1-5, jika memilih selain 1-5, maka pilihan akan tidak valid, dan          diminta untuk menginput ulang.
5. Menu 1(daftar pasien baru)

   Pada menu 1, role user dan admin sama-sama bisa menambah pasien baru dengan menginput nama, umur dan keluhannya, lalu        sistem akan menentukan poli. Jika keluhan pasien adalah 'gigi', maka akan masuk ke Poli Gigi. Jika keluhan bukan gigi,       makasistem akan mengecek umur pasien, dimana jika umur pasien kurang dari 17 tahun, maka akan masuk ke Poli Anak. Jika       keluhan bukan 'gigi' dan umur lebih dari 17 tahun, maka akan masuk ke Poli Umum. Setelah selesai, sistem akan menyimpan      data di dalam list dan akan menampilkan output bahwa pendaftaran berhasil. Dan akan mengulang ke input menu 1-5.
6. Menu 2(ubah data pasien)

   Pada menu 2, jika role adalah admin, maka bisa mengubah data pasien dengan menginput nama pasien yang ingin diubah. Jika     nama pasien tidak ditemukan, maka akan menampilkan nama atau data pasien tidak valid, dan akan kembali ke pilihan menu.      Namun jika nama pasien ditemukan, maka admin diminta untuk menginput nama baru, umur baru dan keluhan baru, lalu sistem      akan menentukan poli dengan cara yang sama seperti saat menadaftarkan pasien. Setelah selesai, sistem akan                   mengubah/mengupdate data dan menyimpannya ke dalam list dan menampilkan output bahwa data berhasil diubah. Jika role         adalah user, maka akses ditolak dan akan menampilkan "Anda tidak memiliki akses untuk mengubah data." Dan akan               mengulang ke input 1-5.

   
7. Menu 3(hapus data pasien)

   Pada menu 3, jika role adalah admin, maka bisa menghapus data pasien dengan menginput nama pasien yang ingin dihapus.        Jika nama pasien tidak ditemukan, maka akan menampilkan nama pasien tidak valid. Namun jika nama pasien ditemukan, maka      sistem akan menghapus data pasien dari list. Jika role adalah user, maka akses ditolak dan akan menampilkan "Anda tidak      memiliki akses untuk mengubah data.". Dan akan mengulang ke input 1-5

   
8. Menu 4(lihat data pasien)

    Pada menu 4, role user dan admin sama-sama bisa melihat data pasien. Jika belum ada data pasien, maka akan menampilkan       'belum ada data pasien. Namun jika sudah ada data pasien, maka data pasien akan ditampilkan dalam bentuk                     tabel(PrettyTable). Dan akan mengulang ke input 1-5
9. Menu 5(logout)

    Pada menu 5 adalah menu logout, dimana jika memilih ini maka user dan admin akan terlogout dari pilihan menu dan kembali     ke halaman login.

10. Pada halaman login, jika user mengetik keluar, maka program selesai.
11. SELESAI: Program selesai dijalankan.

# HASIL OUTPUT
## Tampilan Awal
<img width="334" height="56" alt="Screenshot 2026-10-06 153007" src="https://github.com/user-attachments/assets/8001fc9a-4501-4dd9-bdb1-6b6f7f6e0217" />

Tampilan awal pengguna akan diarahkan untuk login agar bisa masuk ke sistem. Pada menu login diberi 2 jenis username dan password yang berbeda. user dan password pertama adalah khusus admin yang bertugas untuk melihat, menambahkah, menghapus, dan update/ubah data. User yang kedua adalah user yang hanya bisa melihat dan menambah data.

## Role Admin
### Menu 1
<img width="411" height="263" alt="Screenshot 2026-10-06 153452" src="https://github.com/user-attachments/assets/dafb715e-c0df-4a7b-9360-bd99c89e2a9a" />

Pada gambar diatas admin menambahkan data pasien dengan menginput nama, umur, dan keluhan pasien. Kemudian sistem yang akan menentukan poli mana pasien masuk dan menampilkannya pada layar.

### Menu 2 
<img width="449" height="157" alt="Screenshot 2026-10-06 154135" src="https://github.com/user-attachments/assets/0f517b3b-92bb-4072-aeee-b929e296fa20" />

Pada gambar diatas admin mengubah salah satu data pasien. Pada gambar, karena nama 'Alya' tidak ada dalam data pasien, maka menampilkan "Nama atau data pasien tidak valid" dan kembali ke menu input pilihan. Jika nama ada dalam data pasien seperti nama 'Layla', maka sistem akan meminta untuk menginput nama baru, umur baru, dan keluhan baru pasien yang kemudian disimpan ke dalam data pasien. 

### Menu 3
<img width="377" height="114" alt="Screenshot 2026-10-06 154838" src="https://github.com/user-attachments/assets/2b4e6ba5-78d6-47c3-8692-c07c7a9e137a" />

Pada gambar diatas, admin menghapus salah satu data pasien. Karena nama 'Lulu' tidak ada dalam data pasien maka sistem menampilkan "Nama tidak valid" dan kembali ke menu input pilihan. Jika nama ada dalam data pasien seperti nama 'Rara', maka sistem menghapus data pasien tersebut dari data pasien. 

### Menu 4
<img width="278" height="145" alt="Screenshot 2026-10-06 155215" src="https://github.com/user-attachments/assets/a09d9e4d-f3b0-44f4-b939-cc828133289a" />

Pada gambar di atas menampilkan tabel data pasien yang telah didaftarkan sebelumnya. 

### Menu 5
<img width="299" height="72" alt="Screenshot 2026-10-06 155400" src="https://github.com/user-attachments/assets/1bf9b1fe-7fc3-468a-a1c0-3970d9c2513b" />

Pada gambar diatas, admin memilih menu 5, yaitu logout sehingga menampilkan "Logout berhasil" dan kembali ke tampilan awal(halaman login)
