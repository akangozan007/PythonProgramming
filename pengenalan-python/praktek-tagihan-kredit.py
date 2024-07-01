#!/usr/bin/python3

# KATA KATA MUTIARA


# Mendapatkan Tagihan Bulanan
# Selamat, satu unit lagi dan anda sudah membuat sebuah program! Ketika kita bilang anda bisa membuat apa saja dengan Python, kita bersungguh-sungguh! Batas dari apa yang anda bisa bangun adalah di imajinasi anda.

# Terus belajar ke bab berikutnya dan akhirnya anda akan bisa membuat program yang lebih keren lagi!

# === INSTRUKSI === 
# Oke, sekarang kita membuat variabel total_tagihan yang merupakan jumlah dari sisa_cicilan dan jumlah_bunga.
# Setelahnya, kita buat tagihan_bulanan yang merupakan total_tagihan dibagi 12.
# Jalankan codenya dan lihat berapa tagihan bulanan anda! ^^
# Ubah angkanya sesuai yang anda mau, dan bermain-mainlah dengan apa yang telah anda pelajari.

harga_laptop = 7000000
uang_muka = 1000000

sisa_cicilan = harga_laptop - uang_muka

suku_bunga = 10 # dalam persen

jumlah_bunga = sisa_cicilan * suku_bunga / 100

total_tagihan = sisa_cicilan + jumlah_bunga

tagihan_bulanan = total_tagihan / 12

print(tagihan_bulanan)