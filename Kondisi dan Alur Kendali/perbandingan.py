#!/usr/bin/python3

# KATA KATA MUTIARA
# URUTAN OPERATOR BOOLEAN
# Di sekolah anda pasti sudah belajar kalau perhitungan matematika itu mendahulukan * dan / dibandingkan + atau -. Di operator boolean pun seperti itu. Urutannya seperti ini dimulai dari yang paling penting:

# not
# and
# or
# Yup, not akan dievaluasi terlebih dahulu dan yang terakhir adalah or. Contohnya seperti ini:

# makan = True and False or not True
# Apakah anda bisa tebak apa nilai dari makan? Untuk mempermudahnya kita bisa buat seperti ini, kita mulai dari not tentunya:

# makan = True and False or (not True)
# Karena not True adalah False maka berubah seperti ini:

# makan = True and False or False
# Setelahnya kita dahulukan and menjadi seperti ini:

# makan = (True and False) or False
# True and False adalah False bukan? Yup, jadi makan akan menjadi seperti ini:

# makan = False or False
# Akhirnya bisa kita dapatkan makan adalah False.

# True and True and False
satu = False

# False or False or True
dua = True

# not False and not False
tiga = True

# True and not "CodeSaya" == "SayaCode"
empat = True

# False + True Negasi Menghasilkan True atau 1
print(satu+dua)
# False + False Negasi Menghasilkan False atau 0
print(satu+satu)