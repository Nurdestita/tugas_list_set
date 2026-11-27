# a. Buatlah 2 set untuk menampung pembelian berdasarkan hari pertama dan hari kedua
hari_pertama = {"keju", "tepung", "garam", "gula", "coklat"}
hari_kedua = {"garam", "gula", "coklat", "kecap"}

# b. Tambahkan "keju" pada pembelian hari kedua
hari_kedua.add("keju")

# c. Cari barang yang sama pada pembelian hari pertama dan pembelian hari kedua (Intersection)
barang_sama = hari_pertama.intersection(hari_kedua)
print("c. Barang yang sama:", barang_sama)

# d. Cari barang yang dibeli di hari pertama akan tetapi tidak dibeli pada hari kedua (Difference)
hanya_hari_pertama = hari_pertama.difference(hari_kedua)
print("d. Hanya di hari pertama:", hanya_hari_pertama)

# e. Hapus "garam" pada pembelian hari pertama
hari_pertama.remove("garam")

# f. Cari barang yang dibeli di hari kedua akan tetapi tidak dibeli pada hari pertama (Difference)
hanya_hari_kedua = hari_kedua.difference(hari_pertama)
print("f. Hanya di hari kedua:", hanya_hari_kedua)

# g. Cari barang yang tidak sama pada pembelian hari pertama dan pembelian hari kedua (Symmetric Difference)
barang_tidak_sama = hari_pertama.symmetric_difference(hari_kedua)
print("g. Barang yang tidak sama:", barang_tidak_sama)

# h. Tampilkan semua keperluan rumah tangga yang dibeli pada hari pertama
print("h. Pembelian hari pertama:", hari_pertama)

# i. Tampilkan semua keperluan rumah tangga yang dibeli pada hari kedua
print("i. Pembelian hari kedua:", hari_kedua)