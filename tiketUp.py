print("Kode Kota :")
print("1. Jakarta")
print("2. Yogyakarta")
print("3. Surabaya")
kota=int(input("Pilihan Kota : [1/2/3] ? "))
if (kota==1):
    print("Kode Kelas :")
    print("1. Ekonomi")
    print("2. Bisnis")
    print("3. Eksekutif")
    kelas=int(input("Pilihan Kelas [1/2/3] ?"))
    if (kelas==1) :
        diskon = 0
        harga=100000
        banyakT = int(input("Banyak Tiket :"))
    elif (kelas==2) :
        diskon = 0
        harga= 400000
        banyakT = int(input("Banyak Tiket :"))
    elif (kelas==3) :
        diskon = 0
        harga= 700000
        banyakT = int(input("Banyak Tiket :"))
    else :
        print("Pilihan Anda Salah!")
elif (kota==2) :
    print("Kode Kelas :")
    print("1. Ekonomi")
    print("2. Bisnis")
    print("3. Eksekutif")
    kelas = int(input("Pilihan Kelas [1/2/3] ?"))
    if (kelas == 1):
        harga= 200000
        banyakT = int(input("Banyak Tiket :"))
        kode=input("Kode Voucher :")
        if (kode=="PROMO"):
            diskon=0.10
        else :
            diskon=0
    elif (kelas == 2):
        diskon = 0
        harga= 500000
        banyakT = int(input("Banyak Tiket :"))
    elif (kelas == 3):
        diskon = 0
        harga= 800000
        banyakT = int(input("Banyak Tiket :"))
    else:
        print("Pilihan Anda Salah!")
elif (kota==3) :
    print("Kode Kelas :")
    print("1. Ekonomi")
    print("2. Bisnis")
    print("3. Eksekutif")
    kelas = int(input("Pilihan Kelas [1/2/3] ?"))
    if (kelas == 1):
        diskon = 0
        harga= 300000
        banyakT = int(input("Banyak Tiket :"))
    elif (kelas == 2):
        diskon = 0
        harga= 600000
        banyakT = int(input("Banyak Tiket :"))
    elif (kelas == 3):
        harga= 900000
        banyakT = int(input("Banyak Tiket :"))
        kode = input("Kode Voucher :")
        if (kode == "PROMO"):
            diskon=0.10
        else :
            diskon=0
    else:
        print("Pilihan Anda Salah!")
else :
    print("Pilihan Anda Tidak Ada!")


subtotal = harga * banyakT
diskon=subtotal*diskon
total = subtotal - diskon
print(f"Harga Tiket  : Rp. {harga:5.0f}")
print(f"Sub Total    : Rp. {subtotal:5.0f}")
print(f"Diskon       : Rp. {diskon:5.0f}")
print(f"Total Bayar  : Rp. {total:5.0f}")
