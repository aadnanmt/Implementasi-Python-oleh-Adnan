# Program Buku Kontak Sederhana oleh @aadnanmt
# Maaf, ini masih belum sempurna atau masih belum bekerja secara maksimal, ya
# Tapi, Adnan akan terus belajar dan memperbaiki program ini, ya [tebak kondisi Adnan saat itu dah]
# Semoga program ini bermanfaat bagi kamu, ya

kontak = {}

# Ini adalah pilihan dari buku kontak yang akan diinputkan oleh user
def tampilkan_menu():
    """UNTUK MENAMPILKAN MENU UTAMA"""
    print("\n=== BUKU KONTAK ===\n")
    print("1. Tambah Kontak")
    print("2. Lihat Semua Kontak")
    print("3. Cari Kontak")
    print("4. Hapus Kontak")
    print("5. Keluar")
    print("==================")

# Ini adalah fungsi untuk menambahkan kontak baru
def tambah_kontak():
    """UNTUK MENAMBAHKAN KONTAK BARU"""
    nama = input("Masukkan nama kontak: ")
    nomor = input("Masukkan nomor telepon: ")
    
# ini untuk memeriksa apakah nama kontak sudah ada atau sudah terdaftar
    if nama in kontak:
        pilihan = input(f"Kontak dengan nama {nama} sudah ada. Ingin memperbarui? (y/n): ")
        if pilihan.lower() != 'yes':
            print("Yah, penambahan kontak dibatalkan deh.")
            return
    
    kontak[nama] = nomor
    print(f"Yeyy, kontak {nama} berhasil ditambahkan dong!")

# Ini adalah fungsi untuk menampilkan semua kontaknya
def lihat_kontak():
    """UNTUK MENAMPILKAN SEMUA KONTAK"""
    if not kontak:
        print("Buku kontak masih kosong nih, tambahkan kontak dulu ya.")
        return
    
    print("\n=== DAFTAR DI DALAM BUKU KONTAK ===\n")
    for nama, nomor in kontak.items():
        print(f"Nama: {nama} \t| Nomor: {nomor}")
    print("=====================")

# ini untuk mencari kontak yang sudah ada dibuku kontak
def cari_kontak():
    """UNTUK MENCARI KONTAK BERDASARKAN NAMA"""
    if not kontak:
        print("Buku kontak masih kosong nih, tambahkan kontak dulu ya.")
        return
    
    nama = input("Masukkan nama kontak yang dicari: ")
    
    if nama in kontak:
        print(f"Nama: {nama} \t| Nomor: {kontak[nama]}")
    else:
        print(f"Yah gimana nih, kontak dengan nama {nama} tidak ditemukan.")

# Ini untuk menghapus kontak yang ada, ya
def hapus_kontak():
    """UNTUK MENGHAPUS KONTAK BERDASARKAN NAMA"""
    if not kontak:
        print("Buku kontak masih kosong nih, tambahkan kontak dulu ya.")
        return
    
    nama = input("Masukkan nama kontak yang akan dihapus: ")
    
    if nama in kontak:
        konfirmasi = input(f"Sudah yakin ingin menghapus kontak {nama}? (yes/no): ")
        if konfirmasi.lower() == 'yes':
            del kontak[nama]
            print(f"Kontak {nama} berhasil dihapus.")
        else:
            print("Loh kenapa kamu pilih no, penghapusan kontak dibatalkan.")
    else:
        print(f"Yah, Kontak dengan nama {nama} tidak ditemukan.")

def main():
    """UNTUK FUNGSI UTAMA PROGRAM"""
    while True:
        tampilkan_menu()
        
        pilihan = input("Pilih dan ketik menu (1-5): ")
        
        if pilihan == '1':
            tambah_kontak()
        elif pilihan == '2':
            lihat_kontak()
        elif pilihan == '3':
            cari_kontak()
        elif pilihan == '4':
            hapus_kontak()
        elif pilihan == '5':
            print("Terima kasih telah menggunakan program Buku Kontak Sederhana buatan @aadnanmt")
            break
        else:
            print("Heii!Pilihan kamu tidak valid. Silakan pilih dan ketik (1-5) kembali.")

# Ini adalah program utama yang akan dijalankan, ya
if __name__ == "__main__":
    main()