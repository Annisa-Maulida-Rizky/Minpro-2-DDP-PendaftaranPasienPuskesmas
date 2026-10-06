# Minpro-2-DDP-PendaftaranPasienPuskesmas

Nama : Annisa Maulida Rizky<br>
NIM : 2609116061

#FLOWCHART

<img width="2432" height="1890" alt="Minpro2 drawio" src="https://github.com/user-attachments/assets/c666b140-178a-44d2-8a69-03d395979675" />

Penjelasan:
1. Start: Program dimulai
   
   Menu login: Sistem menampilkan menu login dan meminta pengguna untuk menginput username dan password.
2. Proses Login: Sistem mengecek apakah login sebagai admin atau sebagai mahasiswa. Jika username atau password salah maka        login gagal dan meminta menginput ulang. jika berhasil maka akann menampilkan 'login berhasil' dan role. 
3. Tampilkan Menu 1-5: 1. daftar pasien baru, 2. ubah pasien, 3. hapus pasien, 4. lihat pasien, dan 5. logout
4. Menu 1(daftar pasien baru)
   Pada menu 1, role user dan admin sama-sama bisa menambah pasien baru dengan menginput nama, umur dan keluhannya, lalu        sistem akan menentukan poli. Jika keluhan pasien adalah 'gigi', maka akan masuk ke Poli Gigi. Jika keluhan bukan gigi,       makasistem akan mengecek umur pasien, dimana jika umur pasien kurang dari 17 tahun, maka akan masuk ke Poli Anak. Jika       keluhan bukan 'gigi' dan umur lebih dari 17 tahun, maka akan masuk ke Poli Umum. Setelah selesai, sistem akan menyimpan      data di dalam list dan akan menampilkan output bahwa pendaftaran berhasil. 
5. Menu 2(ubah data pasien)
   Pada menu 2, jika role adalah admin, maka bisa mengubah data pasien dengan menginput nama pasien yang ingin diubah. Jika     nama pasien tidak ditemukan, maka akan menampilkan nama atau data pasien tidak valid, dan akan kembali ke pilihan menu. Namun jika nama pasien ditemukan, maka admin diminta untuk menginput nama baru, umur baru dan keluhan baru, lalu sistem akan menentukan poli dengan cara yang sama seperti saat menadaftarkan pasien. Setelah selesai, sistem akan mengubah/mengupdate data dan menyimpannya ke dalam list dan menampilkan output bahwa data berhasil diubah.
