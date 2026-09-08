print("=======PERPUSTAKAAN FT=======")
print("Selamat Datang di Perpustakaan FT")
print("Daftar Buku Perpustakaan:")
Buku_perpus = ("Bumi", "Bulan", "Malioboro At Midnight", "Twisted Love", "Laut Bercerita")
for i in range(len(Buku_perpus)):
    print(f"{i+1}. {Buku_perpus[i]}")

#peminjaman buku
pinjaman = []
while True:
    apinjaman = input("Buku yang ingin dipinjam: ")
    if apinjaman in Buku_perpus:
        pinjaman.append(apinjaman)
        print("Buku Tersedia")

        tanya = input("Ketik 'selesai' untuk mengakhiri peminjaman: ")
        if tanya == "selesai":
            break
        else:
            continue

    else:
        print("Buku Tidak Tersedia")

#daftar buku saat ini
print("Daftar buku yang ingin dipinjam saat ini:")
for i in range(len(pinjaman)):
    print(f"{i+1}. {pinjaman[i]}")

#buku yang ingin dihapus dari list
takun = input("Apakah semua buku sudah sesuai? (ya/tidak): ")
if takun == "ya":
    print("Terima kasih telah meminjam buku di perpustakaan kami")
else:
    while True :
        buku_dikembalikan = input("Masukkan buku yang tidak sesuai: ")
        if buku_dikembalikan in pinjaman:
            pinjaman.remove(buku_dikembalikan)
            print(f"Peminjaman {buku_dikembalikan} dibatalkan")
            for i in range(len(pinjaman)):
                print(f"{i+1}. {pinjaman[i]}")

            betakun_lagi = input("Apakah masih ada buku yang ingin dikembalikan? (ya/tidak): ")
            if betakun_lagi == "ya":
                continue
            else:
                break
        else:
            print("Buku Tidak Tersedia")

#bukti peminjaman
print("=" * 55)
print("BUKTI PEMINJAMAN".center(55))
print("=" * 55)
print("Daftar buku:")
for i in range(len(pinjaman)):
    print(f"{i+1}. {pinjaman[i]}")
print("Terima kasih telah meminjam buku di perpustakaan kami")
print("=" * 55)