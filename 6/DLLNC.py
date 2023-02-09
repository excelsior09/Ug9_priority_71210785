from NodeMahasiswa import NodeMahasiswa

class DLLNC:
       def __init__(self):
              self.head = None
              self.tail = None
              self.size = 0

       def isEmpty(self):
              return self._size == 0

       def len(self):
              return self._size

       def addElementTail(self, nama, ipk):
              baru = NodeMahasiswa(nama,ipk)
              if self.size == 0:
                     self.head = baru
                     self.tail = baru
              else:
                     self.tail = baru
                     baru.prev = self.tail
                     self.tail = baru
              print("data masuk ke tail")
              self.size = self.size + 1

       def deleteLast(self):
              if self.size == 1:
                     self.head = None
                     self.tail = None
              else:
                     hapus = self.tail
                     self.tail = self.tail.prev
                     hapus._prev = None
                     self.tail.next = None
                     del hapus
              print("# data", hapus, "terhapus #")
              self.size = self.size - 1

       def printAllDescending(self):
              bantu = self.tail
              while bantu != None:
                     print("=== Print Descending ===")
                     print("="*24)
                     print("Nama :",bantu.setNama)
                     print("IPK  :",bantu.setIpk)


DLLNC.addElementTail('Shalom',3.9)
DLLNC.addElementTail('Nabilla',3.8)
DLLNC.addElementTail('Kurniadi',3.7)
DLLNC.addElementTail('Harris',3.6)
DLLNC.printDescending()
DLLNC.deleteLast()
DLLNC.printDescending()
DLLNC.rataIpk()
