from modul_prak10.aritmatika_modul import *

def hitungan_aritmatika():
    print("\nPilih operasi aritmatika yang ingin dilakukan:")
    print("1. Penambahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Pangkat")
    pilihan = int(input("\nMasukkan nomor operasi aritmatika yang dipilih (1-5 ): "))

    if pilihan == 1:
        a = float(input("Masukkan angka pertama: "))
        b = float(input("Masukkan angka kedua: "))
        print("Hasil Penambahan:", tambah(a, b))
    elif pilihan == 2:
        a = float(input("Masukkan angka pertama: "))
        b = float(input("Masukkan angka kedua: "))
        print("Hasil Pengurangan:", kurang(a, b))
    elif pilihan == 3:
        a = float(input("Masukkan angka pertama: "))
        b = float(input("Masukkan angka kedua: "))
        print("Hasil Perkalian:", kali(a, b))
    elif pilihan == 4:
        a = float(input("Masukkan angka pembilang: "))
        b = float(input("Masukkan angka penyebut (tidak boleh nol): "))
        print("Hasil Pembagian:", bagi(a, b))
    elif pilihan == 5:
        a = float(input("Masukkan angka dasar: "))
        b = float(input("Masukkan pangkat: "))
        print("Hasil Eksponensial:", pangkat(a, b))
    else:
        print("Pilihan tidak valid.")

    hitungan_aritmatika()