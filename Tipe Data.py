# 3.1 String
nama = "Ananda Viamianni"
jeniskelamin = "Perempuan"
alamat = """
    Jl. G.Obos XIII Gang. Panga Sungu No 2
    Palangka raya, Kalimantan Tengah
"""
motohidup = '''

            Asikin aja dah
'''
print(nama)
print(jeniskelamin)
print(alamat)
print(motohidup)
print(type(nama))
print(type(jeniskelamin))
print(type(alamat))
print(type(alamat))
print(type(motohidup))
print("\n")

# Mengakses String
kata = "Ananda Viamianni"
print(kata[0:6])
print(kata[0:5])
print("\n")

# Syntax khusus
kata = "Happy coding"
print("Kondisi awal kata : ")
print(kata)
print('')
print("Menggunakan uper()")
print(kata.upper())
print('')
word = "DASPRO"
print("Kondisi awal kata : ")
print(word)
print('')
print("Menggunakan lower()")
print(word.lower())

# 3.2 Bilangan(Angka)
#integer(int) atau bilangan bulat
harga = 25000
print(type(harga))
print('')

#Float atau angka desimal yang menggunakan titik(.) bukan koma(,)
jarak = 8.5
print("Jarak : ", jarak)
print("Tipe data :", type(jarak))
print("Jarak di casting menjadi Integer :", int(jarak))
print('')

# 3.3 Boolean
# tipe ini hanya memiliki dua nilai yaitu True or False atau 1 dan 0.

bergerak = True
jalan = 1
print(bergerak)
print(jalan)
print(bool(jalan))
