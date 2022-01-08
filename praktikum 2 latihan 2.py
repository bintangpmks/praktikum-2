# -*- coding: utf-8 -*-
"""

@materi : algoritma dan pemograman
@judul : Menghitung nilai rata-rata
@hari/tanggal : Sabtu,20211009
@nim : 065002100023
@author : Tri Bintang Pamungkas
"""
import math

print("menentukan persamaan kuadrat")


pilihan1 = float(input("masukan angka yang pertama: "))
pilihan2 = float(input("masukan angka yang kedua: "))
pilihan3 = float(input("masukan angka yang ketiga: "))


if pilihan1 == 0:
    print("bukan persamaan kuadrat")

else:
    rumus = (pilihan2**2) - (4*pilihan1*pilihan3)

    if rumus > 0 :
      x1 = (-pilihan2 + math.sqrt(rumus)) / (2*pilihan1)
      x2 = (-pilihan2 - math.sqrt(rumus)) / (2*pilihan1)
      print(f"persamaan kuadrat nya adalah {pilihan1}x^2 + {pilihan2}*x + {pilihan3}")
      print("merupakan jenis akar yang berbeda")
      print("dengan determinan",rumus)
      print("jadi akar dari x1 adalah :",x1)
      print("jadi akar dari x2 adalah :",x2)



    elif rumus == 0 :
        x1 = (-pilihan2 )/ (2*pilihan1)
        x2 = (-pilihan2 )/ (2*pilihan1)
        print(f"persamaan kuadrat nya adalah {pilihan1}x^2 + {pilihan2}*x + {pilihan3}")
        print("merupakan jenis akar yang kembar")
        print("jadi persamaan kuadrat nya adalah",x1)
        print("jadi persamaan kuadrat nya adalah",x2)
        print("dengan determinan",rumus,)

    elif rumus < 0 :
        print(f"persamaan kuadrat nya adalah {pilihan1}x^2 + {pilihan2}*x + {pilihan3}")
        print("merupakan jenis akar imaginer")
        print(f"akar x1 = -{pilihan2} + akar {rumus}/{pilihan2}*{pilihan1}")
        print(f"akar x2 = -{pilihan2} - akar {rumus}/{pilihan2}*{pilihan1}")


print("Terima kasih telah menggunakan program ini :)")