# 4.1 Operator Aritmatika
"""
Contoh studi kasus: 
Untuk memperingati ulang tahun ke-33 Matahari Mall, sedang diadakan diskon besar-besaran untuk beberapa item tertentu. 
Bantulah Yaya yang merupakan seorang kasir baru di Matahari Mall, dengan membuat program untuk menghitung total harga belanjaan 
seorang pembeli dengan masing-masing diskon senilai 60%: 
- Kaos Greenlight = Rp250.000 
- Sepatu Nike = Rp920.000
"""
print("=====PROGRAM KASIR MATAHARI MALL=====")
kaos = float(input("Harga kaos = "))
sepatu = float(input("Harga sepatu = "))
total = (kaos-(kaos*0.6)) + (sepatu-(sepatu*0.6))
print("Total harga = Rp" + str(total))
print('')

# 4.4 Operator Logika
"""
Contoh Studi kasus:
Untuk mendapatkan indeks A, seorang mahasiswa harus bisa mendapatkan nilai lebih dari sama dengan 80 
untuk mata kuliah Kalkulus dan Matdis. 
Buatkan program yang dapat mengetahui apakah mahasiswa dapat mendapatkan indeks A.
"""
print('=====PROGRAM INPUT NILAI====')
kalkulus = int(input("Nilai Kalkulus = "))
matdis = int(input("Nilai matdis ="))
nilai = kalkulus>=80 and matdis>=80
print("Indeks nilai A : " + str(nilai))
print("")

# 4.5 Operator Keanggotaan
#in = mengembalikan nilai true apabila sebuah nilai terdapat pada sequence
nama = "Ananda Viamianni"
print("na" in nama)
print("Na" in nama)
print("")

#not in = mengembalikan nilai true apabila sebuah nilai tidak terdapat pada sequence
nama = "Ananda Viamianni"
print("Anan" not in nama)
print("anan" not in nama)
print("")

# 4.6 Operator Keanggotaan
# is = Mengembalikan nilai True apabila variable adalah objek yang sama
x = 15
y = 10
z = 15
print(x is y)
print(x is z)
print("")

#is not = Mengembalikan nilai True apabila kedua variable bukanlah objek yang sama
x = 15
y = 10
z = 15
print(x is not y)
print(x is not z)
print(x is not x)
print("")