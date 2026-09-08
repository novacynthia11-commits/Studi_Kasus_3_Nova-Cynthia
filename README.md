# Sistem Peminjaman Buku Di Perpustakaan FT
**Nama :** Nova Cynthia <br>
**NIM :** 2609116031 <br>
**Program Studi :** Sistem Informasi <br>
**Kelas :** A 2026 <br>
**Mata Kuliah :** Dasar-Dasar Pemograman <br>

## Deskripsi
Program ini dibuat untuk melakukan proses peminjaman buku di Perpustakaan FT. <br>
Pengguna dapat memilih buku yang sudah tersedia dan memasukkan data peminjaman buku tersebut. <br>
Selain itu, pengguna juga dapat membatalkan buku yang sudah dipilih sebelumnya. <br>
Setelah selesai, program akan menunjukkan berupa bukti peminjaman yang berisi list buku yang sudah dipilih pengguna.

## Output Program
### 1. Input buku tidak sesuai list
Output program ini terjadi ketika pengguna memasukkan nama buku yang tidak sesuai dengan list buku yang sudah tersedia. Program akan menampilkan output berupa "Buku Tidak Tersedia" dan tetap melanjutkan pertanyaan buku yang ingin dipinjam. <br>
<img width="450" alt="Screenshot 2026-09-08 193331" src="https://github.com/user-attachments/assets/c28533b4-d46f-4b99-8b1a-eed56f5e15e9" />
&nbsp;
### 2. Input buku sesuai dengan list
Output program ini akan menampilkan kalimat "Buku Tersedia", lalu menampilkan kalimat ***decision*** dengan pengguna memasukkan kata "selesai" jika peminjaman buku selesai. Tapi program akan melakukan ***looping*** ketika pengguna menjawab selain kata "selesai" yaitu kembali ke pertanyaan buku yang ingin dipinjam.
#### a. Ketika pengguna memasukkan kata "selesai"
<img width="450" alt="Screenshot 2026-09-08 194534" src="https://github.com/user-attachments/assets/0fdde6cf-ed32-4446-820a-04431c24e3ee" />



#### b. Ketika pengguna memasukkan kata *selain* "selesai"
<img width="450" alt="Screenshot 2026-09-08 194612" src="https://github.com/user-attachments/assets/28a58caf-54cd-4ed2-a9d5-e12812794e7a" />



### 3. Pembatalan Peminjaman Buku
Setelah pengguna memasukkan kata "selesai", program akan dilanjutkan dengan output ***decision*** berupa pertanyaan apakah buku yang dipinjam sesuai dengan pilihan jawaban ya/tidak. Jika pengguna memasukkan kata "ya" maka output yang dihasilkan berupa daftar buku yang dipinjam, seperti digambar berikut : <br>
<br>
<img width="450" alt="Screenshot 2026-09-08 195829" src="https://github.com/user-attachments/assets/6036977a-8ed1-4636-ae15-90897bb4db38" />


Sedangkan jika pengguna memasukkan kata "tidak" maka akan menampilkan kalimat "Masukkan buku yang tidak sesuai" dengan pengguna memasukkan nama buku tersebut. Setelah itu, program akan menampilkan nama buku yang dibatalkan dan daftar buku setelah pengguna memasukkan nama buku yang dibatalkan. Program akan melakukan ***looping*** dengan pertanyaan "Apakah masih ada buku yang ingin dikembalikan?" jika pengguna memasukkan kata "ya" sampai pengguna memasukkan kata "tidak". Seperti gambar berikut : <br>
<br>
<img width="450" alt="Screenshot 2026-09-08 200123" src="https://github.com/user-attachments/assets/3b34bcfa-9a2a-4527-b6a7-ac15962b62dd" />


### 4. Bukti Peminjaman
Program ini adalah sebagai penutup dengan menampilkan buku yang dipinjam pengguna setelah melewati *verifikasi* dengan pertanyaan dan kalimat ***decision***. Output yang dihasilkan berupa daftar buku dan kalimat terima kasih sebagai penutup. Berikut gambar output "Bukti Peminjaman" <br>
<br>
<img width="450" alt="Screenshot 2026-09-08 201928" src="https://github.com/user-attachments/assets/6a022a10-0024-4b90-848b-47086de43b08" />
