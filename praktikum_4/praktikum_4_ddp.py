# Buatlah program yang meminta pengguna untuk memasukkan sebuah bilangan bulat. Program harus menentukan apakah bilangan tersebut genap atau ganjil menggunakan if dan if else.
# Input
# Soal 1: Bilangan Genap atau Ganjil
bilangan = int(input("Masukkan bilangan bulat: "));
# Proses Kondisi
if bilangan % 2 == 0:
    print("Bilangan", bilangan, "adalah bilangan genap");
else:
    print("Bilangan", bilangan, "adalah bilangan ganjil");
    
# Soal 2: Nilai Ujian
# Buatlah program yang meminta pengguna untuk memasukkan nilai ujian. Jika nilai lebih besar atau sama dengan 75, cetak "Lulus". Jika tidak, cetak "Tidak Lulus". Gunakan if dan if else.
# Input
nilai = int(input("Masukkan nilai ujian: "));
# Proses Kondisi
if nilai >= 75:
    print("Lulus");
else:
    print("Tidak Lulus");

# Soal 3: Cek Usia dan Status
# Buatlah program yang meminta pengguna untuk memasukkan usia. Program harus mencetak "Dewasa" jika usia lebih besar atau sama dengan 18, dan "Anak-anak" jika kurang dari 18. Tambahkan kondisi untuk mencetak "Remaja" jika usia antara 13 dan 17 menggunakan if and.
# Input
usia = int(input("Masukkan usia: "));
# Proses Kondisi
if usia >= 18:
    print("Dewasa");
elif usia >= 13 and usia <= 17:
    print("Remaja");

# Soal 4: Cek Keanggotaan
# Buatlah program yang meminta pengguna untuk memasukkan status keanggotaan (misalnya "gold", "silver", atau "bronze"). Jika statusnya "gold" atau "silver", cetak "Selamat! Anda mendapatkan diskon". Gunakan if or.
# Input
status = input("Masukkan status keanggotaan: ");
# Proses Kondisi
if status == "gold" or status == "silver":
    print("Selamat! Anda mendapatkan diskon");
else:
    print("Maaf, Anda tidak mendapatkan diskon");

# Soal 5: Pembelian Diskon
# Buatlah program yang meminta pengguna untuk memasukkan jumlah pembelian. Jika jumlahnya lebih dari 100, beri diskon 10% menggunakan shorthand if. Cetak total harga setelah diskon jika ada, jika tidak, cetak total harga tanpa diskon.
# example : minyak 25.000, indomie 5.000, beras 75.000, gula 25.000, kopi 20.000, teh 10.000
 
# Barang
minyak = 25000
indomie = 5000

# Input
jumlah_pembelian_minyak = int(input("Masukkan jumlah pembelian minyak: "))
jumlah_pembelian_indomie = int(input("Masukkan jumlah pembelian indomie: "))

# Proses Kondisi & cetak tambahan diskonnya
total_harga = (minyak * jumlah_pembelian_minyak) + (indomie * jumlah_pembelian_indomie)
diskon = 0.1

# Cek apakah total pembelian lebih dari 100 dengan shorthand if
total_diskon = total_harga * diskon if (jumlah_pembelian_minyak + jumlah_pembelian_indomie) > 100 else 0
total_harga -= total_diskon

# Cetak hasil
print(f"Anda mendapatkan diskon sebesar 10%: Rp {total_diskon}" if total_diskon > 0 else "Tidak ada diskon yang diberikan.")
print(f"Total harga setelah diskon (jika ada): Rp {total_harga}")
