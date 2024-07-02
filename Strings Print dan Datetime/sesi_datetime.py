#!/usr/bin/python3

# KATA KATA MUTIARA

# DATETIME
# Kita juga bisa mendapatkan jam, menit, dan detik loh dari datetime. Seperti ini caranya:

# from datetime import datetime
# n = datetime.now()

# print n.hour
# print n.minute
# print n.second
# Tidak perlu dijelaskan panjang lebar, pasti anda mengerti karena mirip sekali dengan unit-unit sebelumnya,
# hanya saja sekarang kita mengambil properti hour, minute, dan second dari now().

from datetime import datetime 
kini = datetime.now()

jam = kini.hour
menit = kini.minute
detik = kini.second

print("{0}:{1}:{2}".format(kini.hour, kini.minute, kini.second))

