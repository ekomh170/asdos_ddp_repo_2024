# Soal 1: Bilangan Genap atau Ganjil
# Buatlah program yang meminta pengguna untuk memasukkan sebuah bilangan bulat. Program harus menentukan apakah bilangan tersebut genap atau ganjil menggunakan if dan if else.

bilangan_bulat = int(input("Masukkan bilangan bulat: "))


if bilangan_bulat % 2==0:
    print("Bilangan", bilangan_bulat, "adalah bilangan genap")
else:
    print("Bilangan", bilangan_bulat, "adalah bilangan ganjil")

# Soal 2: Nilai Ujian
# Buatlah program yang meminta pengguna untuk memasukkan nilai ujian. Jika nilai lebih besar atau sama dengan 75, cetak "Lulus". Jika tidak, cetak "Tidak Lulus". Gunakan if dan if else.

nilai_ujian_mhs = int(input("Masukkan nilai ujian: "))

if nilai_ujian_mhs >= 75:
    print("Lulus");
else:
    print("Tidak Lulus");
    
# Soal 3: Cek Usia dan Status
# Buatlah program yang meminta pengguna untuk memasukkan usia. Program harus mencetak "Dewasa" jika usia lebih besar atau sama dengan 18, dan "Anak-anak" jika kurang dari 18. Tambahkan kondisi untuk mencetak "Remaja" jika usia antara 13 dan 17 menggunakan if and.

usia = int(input("masukan Usia: "))
if usia >= 18:
    print("Dewasa")
elif usia >= 13 and usia <= 17:
    print("remaja")
else:
    print("Anak-Anak")
    
# Soal 4: Cek Keanggotaan
# Buatlah program yang meminta pengguna untuk memasukkan status keanggotaan (misalnya "gold", "silver", atau "bronze"). Jika statusnya "gold" atau "silver", cetak "Selamat! Anda mendapatkan diskon". Gunakan if or.

status_keanggotaan = input("Masukkan Status Keanggotaan :") . lower()

if status_keanggotaan =="gold" or status_keanggotaan == "silver":
    print("Selamat! Anda Mendapatkan Diskon")
else:
    print("Maaf, Anda Tidak Mendapatkan Diskon")
    
#  Soal 5: Pembelian Diskon
# Buatlah program yang meminta pengguna untuk memasukkan jumlah pembelian. Jika jumlahnya lebih dari 100, beri diskon 10% menggunakan shorthand if. Cetak total harga setelah diskon jika ada, jika tidak, cetak total harga tanpa diskon.
# example : 
# minyak 25.000, indomie 5.000, beras 75.000, gula 25.000, kopi 20.000, teh 10.000

minyak = 25000
indomie = 5000

# input
jumlah_pembelian_minyak = int(input("Masukkan jumlah pembelian minyak: "))
jumlah_pembelian_indomie = int(input("Masukkan jumlah pembelian indomie: "))

# Proses Jumlah + Harga
total_harga = (jumlah_pembelian_minyak * minyak) + (jumlah_pembelian_indomie * indomie)
diskon = 0.1

# Validasi Diskon
total_diskon = total_harga * diskon if(jumlah_pembelian_minyak + jumlah_pembelian_indomie) > 100 else 0
total_harga -= total_diskon

# Cetal Hasil
print("Diskon Yang Anda Dapatkan Sebesar 10% Rp", total_diskon if total_diskon > 0 else "Tidak Ada Diskon")
print("Total harga: Rp", total_harga)
