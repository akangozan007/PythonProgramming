#!/usr/bin/python3

# KATA KATA MUTIARA
# FUNGSI LANJUTAN
# Ada dua hal yang anda akan pelajari kali ini,
# yang pertama adalah menggunakan lebih dari satu parameter.
# Dan memanggil function lain di function anda sendiri, contohnya seperti ini:

# def iseng(kata, angka):
#   return kata.upper() + str(angka*2)
# wow = iseng("seru", 21)

# Apakah anda bisa menebak nilai dari wow? Tepuk pundak anda jika anda menjawab "SERU42". 
# Ya, untuk menggunakan dua parameter cukup membatasinya dengan koma , seperti ini:

# (param1, param2, param3, param4)
# Di function yang anda buat,
# anda bisa memanggil function seperti str(), len() atau 
# bahkan function yang telah anda buat sebelumnya.

# Instruksi:
# Buat sebuah function bernama pembuat_password()
# function ini menerima dua buat parameter yaitu website, dan tahun.
# Mirip seperti iseng(), tetapi alih-alih menggunakan upper(), kita menggunakan lower() di website. 
# Dan alih-alih mengalikan angka dengan 2, kita mengalikan tahun dengan 11.

# Membuat Function pembuat password 
# menambahkan 2 parameter website dan password 
def pembuat_password(website,tahun):
# mengembalikan nilai upper() dari data yang didapat param website
# mengembalikan nilai bertipe string setelah proses perkalian dari data yang didapat param tahun
    return website.upper() +" "+str(tahun*11)
# nilai yang diproses oleh function pembuat_password() disimpan ke variable wow
wow = pembuat_password("razan.id", 2022)
# mencetak nilai/data dari variable wow 
print(wow)