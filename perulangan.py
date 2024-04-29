#NAMA: IKHWAN MAULANA IVANSYAH
#NIM:  SI20230016


daftar_barang = {
    "Timun Mas": 10000,
    "Malin Kundang": 8000,
    "Sangkuriang": 2000,
    "Tangkuban Perahu": 15000,
    "Batu Menangis": 5000
}


print("=================================")
print("|| SELAMAT DATANG DI TOKO BUKU ||")
print("=================================")


print("Daftar Barang:")
for barang, harga in daftar_barang.items():
    print(f"=> {barang}: Rp.{harga}")


total_belanja = 0
daftar_belanja = []


jumlah_barang = int(input("\nMasukkan jumlah barang yang ingin dibeli: "))


for i in range(jumlah_barang):
    barang = input(f"Masukkan nama barang ke-{i+1}: ")
    if barang in daftar_barang:
        total_belanja += daftar_barang[barang]
        daftar_belanja.append(barang) 
    else:
        print(f"{barang} tidak ada dalam daftar barang.")


print("======================================")
print("    || Daftar Barang Yang Dibeli ||   ")
print("======================================")

for barang in daftar_belanja:
    print(f" => {barang}")
print("--------------------")
print(f"Total belanjaan Anda: Rp {total_belanja}")
