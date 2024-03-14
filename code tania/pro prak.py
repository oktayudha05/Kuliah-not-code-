
import suhu
from suhu import myclass
biar_ada_if = True
while True:
    satuan_suhu = ['Celcius','Fahrenheit','Reamur','Kelvin']
    print(" ")
    print("=============== \033[1mKONVERSI SUHU\033[0m ===============")
    angka = 1
    for i in range(len(satuan_suhu)):
        for j in range(len(satuan_suhu)):
            if i == j:
                continue
            else:
                print(f"{angka}. {satuan_suhu[i]} ke {satuan_suhu[j]}")
                angka += 1

    print("====================================================")
    n = int(input("Pilih rumus konversi suhu(1/2/3/4/5/7/8/9/10/11/12): "))
    if biar_ada_if == True:
        if n == 1:
            b = float(input("Masukan nilai satuan celcius: "))
            o = myclass.cel_fahrenheit(b)
            print(f"Hasil : {o}" )

        elif n == 2:
            c = float(input("Masukan nilai satuan celcius: "))
            p = myclass.cel_reamur(c)
            print(f"Hasil : {p}")

        elif n == 3:
            d = float(input("Masukan nilai satuan celcius: "))
            q = myclass.cel_kelvin(d)
            print(f"Hasil : {q}")

        elif n == 4:
            e = float(input("Masukan nilai satuan fahrenheit: "))
            r = myclass.fah_cel(e)
            print(f"Hasil : {r}")

        elif n == 5:
            f = float(input("Masukan nilai satuan fahrenheit: "))
            s = myclass.fah_re(f)
            print(f"Hasil : {s}")

        elif n == 6:
            j = float(input("Masukan nilai satuan fahrenheit: "))
            t = myclass.fah_kel(j)
            print(f"Hasil : {t}")

        elif n == 7:
            g = float(input("Masukan nilai satuan reamur: "))
            u = myclass.re_cel(g)
            print(f"Hasil : {u}")

        elif n == 8:
            h = float(input("Masukan nilai satuan reamur: "))
            v = myclass.re_fah(h)
            print(f"Hasil : {v}")

        elif n == 9:
            k = float(input("Masukan nilai satuan reamur: "))
            w = myclass.re_kel(k)
            print(f"Hasil : {w}")

        elif n == 10:
            i = float(input("Masukan nilai satuan kelvin: "))
            x = myclass.kel_celcius(i)
            print(f"Hasil : {x}")

        elif n == 11:
            l = float(input("Masukan nilai satuan kelvin: "))
            y = myclass.kel_fah(l)
            print(f"Hasil : {y}")

        elif n == 12:
            m =  float(input("Masukan nilai satuan kelvin: "))
            z = myclass.kel_rea(m)
            print(f"Hasil : {z}")

        else:
            print("ERROR: Jawaban yang anda masukan tidak valid\nMasukan jawaban (1/2/3/4/5/6/7/8/9/10/11/12)")


        atur_suhu =input ("Ingin melakukan konversi yang lain? (YA/NO): ")
        if atur_suhu == "NO":
            print("PROGRAM SELESAI")
            break

