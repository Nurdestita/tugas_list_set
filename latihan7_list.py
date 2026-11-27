# a. Membuat list penumpang sesuai urutan tempat duduk (index 0 s.d. 4)
penumpang = ["William", "Kate", "Anderson", "Jame", "Mady"]
print("a. List awal:", penumpang)

# b. Menambahkan "Jones" di posisi terakhir (nomor 6 / index 5)
penumpang.append("Jones")
print("b. Setelah Jones masuk:", penumpang)

# c. Mengganti "Anderson" (nomor 3 / index 2) dengan "Grace" di Ciamis
index_anderson = penumpang.index("Anderson")
penumpang[index_anderson] = "Grace"
print("c. Setelah Grace menggantikan Anderson di Ciamis:", penumpang)

# d. Mengecek apakah "Thompson" ada di list menggunakan membership (in)
ada_thompson = "Thompson" in penumpang
print("d. Apakah ada 'Thompson' di Kebumen?:", ada_thompson)

# e. Mengurutkan list sesuai abjad nama orang setelah Kebumen
penumpang.sort()
print("e. Urutan abjad setelah Kebumen:", penumpang)

# f. Menampilkan 6 penumpang yang sampai di Yogyakarta menggunakan perulangan for
print("f. Penumpang yang sampai di Yogyakarta:")
for nama in penumpang:
    print("-", nama)

# g. Mengosongkan list secara keseluruhan setelah penumpang turun
penumpang.clear()
print("g. List setelah dikosongkan:", penumpang)
