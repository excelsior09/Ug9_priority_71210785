from dllnc_ import DLLNC

progam = DLLNC()
pil = 0
while pil != "6":
       print("MENU:")
       print("1. Tambah Depan")
       print("2. Tampilkan")
       print("3. Hapus Depan")
       print("4. Tambah Belakang")
       print("5. Filter Huruf")
       print("6. Exit")
       pil = input("Pilihan : ")

       if pil == "1":
              kode = input("Masukan Kode : ")
              judul = input("Masukan Judul : ")
              progam.tambahDepan(kode,judul)
       elif pil == "2":
              progam.tampil()
       elif pil == "3":
              progam.hapusDepan()
       elif pil == "4":
              kode = input("Masukan Kode : ")
              judul = input("Masukan Judul : ")
              progam.tambahBelakang(kode,judul)
       elif pil == "5":
              huruf = input("Masukan huruf depan")
              progam.tampilFilter(huruf)
       elif pil == "6":
              print("Program Selesai")