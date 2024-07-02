#!/usr/bin/python3

# KATA KATA MUTIARA
# Kesimpulan
# Keren sekali! Di bab ini sudah banyak yang anda pelajari, di antaranya:

# PERBANDINGAN

# 2 != 1
# "Python" > "Java"
# Operator Boolean:

# True and False
# False or not (5*5 == 25)
# Pengkondisian:

# if poin > 10:
#   print "Naik ke level atas.."
# elif poin > 5:
#   print "Tetap di level ini.."
# else:
#   print "Turun ke level bawah.."
# Jangan sampai lupa ya, ini akan sangat berguna sekali bagi seorang coder. Sekarang mari kita ke soal pamungkas!

#  Instruksi:
# Mari kita bermain tebak angka!

# Buatlah dua variabel yaitu tebakan dan angka. Berikan keduanya nilai bertipe angka (integer).
# Lakukan if yang akan memeriksa jika tebakan lebih kecil dibandingkan angka, maka code anda akan mencetak "Tebakan terlalu rendah!".
# Berikutnya lakukan elif yang akan memeriksa jika tebakan lebih besar dibandingkan angka, maka code akan mencetak "Tebakan terlalu tinggi!".
# Terakhir else yang akan mencetak "Tebakan anda tepat".
# Bermain-main lah, ubah nilai dari angka dan tebakan dan lihat outputnya berubah saat anda jalankan.


# Jika anda sudah belajar sejauh ini, anda hebat!

tebakan = 200
angka = 300

# jika tebakan (200) kurang dari angka (300) maka outputnya
if tebakan < angka:
  print("Tebakan terlalu rendah!")
# jika tebakan (200) Lebih dari angka (300) maka outputnya
elif tebakan > angka:
  print("Tebakan terlalu tinggi!")
# jika tebakan selain keduanya alias tidak ada angka berapapun selain
# 300 itu sendiri tebakan anda benar atau variable tebakan bernilai 300
else:
  print("Tebakan anda tepat") 