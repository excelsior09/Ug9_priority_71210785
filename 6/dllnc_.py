from Node import Node

class DLLNC:
       def __init__(self):
              self.head = None
              self.tail = None
              self.size = 0

       def tambahDepan(self, kode, judul):
              baru = Node(kode,judul)
              if self.size == 0:
                     self.head = baru
                     self.tail = baru
              else:
                     baru.next = self.head
                     self.head.prev = baru
                     self.head = baru
              print("data masuk")
              self.size = self.size + 1
       
       def hapusDepan(self):
              if self.size == 1:
                     self.head = None
                     self.tail = None
              else:
                     hapus = self.head
                     self.head = self.head.next
                     hapus.next = None
                     self.head.prev = None
                     del hapus
              print("data terhapus")
              self.size = self.size - 1

       def tambahBelakang(self, kode, judul):
              baru = Node(kode,judul)
              if self.size == 0:
                     self.head = baru
                     self.tail = baru
              else:
                     self.tail = baru
                     baru.prev = self.tail
                     self.tail = baru
              print("data masuk dari belakang")
              self.size = self.size + 1

       def tampilFilter(self, huruf):
              bantu = self.head
              while bantu != None:
                     if bantu.judul[0] == huruf:
                            print("Kode :", bantu.kode, "dan Judul :", bantu.judul)
                     bantu = bantu.next
              print("Total :", self.size)

       def tampil(self):
              bantu = self.head
              while bantu != None:
                     print("Kode :", bantu.kode, "dan Judul :", bantu.judul)
                     bantu = bantu.next
              print("Total :", self.size)

