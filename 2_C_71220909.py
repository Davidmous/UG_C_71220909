kecepatan = int(input("Masukan Kecepatan Tempuh:"))
waktu = int(input("Masukan Waktu:"))
#rumus
jarak = kecepatan*waktu
bensin = (jarak//10)
biaya = 15000*bensin
print("Teman anda mengisi bensin sebanyak",bensin,"liter")
print("Biaya yang dikeluarkan untuk mengisi bensin adalah","Rp.",biaya)
