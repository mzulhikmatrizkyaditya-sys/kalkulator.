import math

while True:
    print("\n=== KALKULATOR LENGKAP ===")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Pangkat")
    print("6. Akar Kuadrat")
    print("7. Modulus")
    print("8. Pembagian Bulat")
    print("9. Persentase")
    print("10. Luas Persegi")
    print("11. Luas Persegi Panjang")
    print("12. Luas Segitiga")
    print("13. Luas Lingkaran")
    print("14. Sinus")
    print("15. Kosinus")
    print("16. Tangen")
    print("0. Keluar")

    pilih = input("Pilih menu: ")

    if pilih == "0":
        print("Program selesai!")
        break

    elif pilih in ["1", "2", "3", "4", "5", "7", "8"]:
        a = float(input("Angka pertama: "))
        b = float(input("Angka kedua: "))

        if pilih == "1":
            hasil = a + b
        elif pilih == "2":
            hasil = a - b
        elif pilih == "3":
            hasil = a * b
        elif pilih == "4":
            hasil = a / b if b != 0 else "Tidak bisa dibagi nol"
        elif pilih == "5":
            hasil = a ** b
        elif pilih == "7":
            hasil = a % b if b != 0 else "Tidak bisa dibagi nol"
        else:
            hasil = a // b if b != 0 else "Tidak bisa dibagi nol"

        print("Hasil:", hasil)

    elif pilih == "6":
        a = float(input("Masukkan angka: "))
        print("Hasil:", math.sqrt(a) if a >= 0 else "Angka negatif!")

    elif pilih == "9":
        a = float(input("Nilai: "))
        b = float(input("Persentase: "))
        print("Hasil:", a * b / 100)

    elif pilih == "10":
        s = float(input("Sisi: "))
        print("Luas:", s ** 2)

    elif pilih == "11":
        p = float(input("Panjang: "))
        l = float(input("Lebar: "))
        print("Luas:", p * l)

    elif pilih == "12":
        a = float(input("Alas: "))
        t = float(input("Tinggi: "))
        print("Luas:", a * t / 2)

    elif pilih == "13":
        r = float(input("Jari-jari: "))
        print("Luas:", math.pi * r ** 2)

    elif pilih in ["14", "15", "16"]:
        sudut = float(input("Masukkan sudut (derajat): "))
        radian = math.radians(sudut)

        if pilih == "14":
            hasil = math.sin(radian)
        elif pilih == "15":
            hasil = math.cos(radian)
        else:
            hasil = math.tan(radian)

        print("Hasil:", round(hasil, 4))

    else:
        print("Pilihan tidak tersedia!")
