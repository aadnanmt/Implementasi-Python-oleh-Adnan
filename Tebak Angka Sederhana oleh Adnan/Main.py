import random

angka_rahasia = random.randint(1, 100)

print("Selamat datang di permainan Tebak Angka sederhana oleh @aadnanmt!")
print("--------------------------------")
while True:
    tebakan = int(input("Masukkan Tebakan Kalian:"))
    print("--------------------------------")

    if tebakan == angka_rahasia:
        print(f"Selamat, yaa! Kamu sudah berhasuil menebak angka dengan benar!")
        break
    elif tebakan < angka_rahasia:
        print("Yahh, angka yang kamu tebak itu masih terlalu kecil")
    else:
        print("Yahh, angka yang kamu tebak itu masih terlalu besar")

print(f"Yahh, gamenya berakhir! Angka yang benar adalah {angka_rahasia}")

print("Adnan mengucapkan terima kasih banyak sudah bermain di game sederhanaini!")
