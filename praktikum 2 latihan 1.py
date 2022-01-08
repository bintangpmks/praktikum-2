# -*- coding: utf-8 -*-
"""

@materi : algoritma dan pemograman
@judul : Menghitung segitiga sama kaki,sisi,sembarang dan bukan segitiga
@hari/tanggal : Senin, 20211004
@nim : 065002100023
@author : Tri Bintang Pamungkas
"""


print("menentukan sebuah segitiga")

sisi1 = int(input("masukan sisi A: "))
sisi2  = int(input("masukan sisi B: "))
sisi3  = int(input("masukan sisi c: "))


if sisi1 and sisi2 == sisi3:
    print("ini merpakan segitiga sama kaki")

elif(sisi1 == sisi2 or sisi1 == sisi2 or sisi2 == sisi3) :
    print("ini merupakan segitiga sama sisi")

elif((sisi1 + sisi2 <= sisi3) or (sisi1 + sisi3 <= sisi2) or (sisi1 + sisi3 <= sisi2)):
    print("ini merupakan bukan sebuah segitiga")

elif(sisi1 and sisi2 and sisi3):
    print("ini merupakan sebuah segitiga sembarang")