class NodeMahasiswa:
       def __init__(self, nama, ipk, n=None, p=None):
              self._element = nama
              self._ipk = ipk
              self._next = n
              self._prev = p

       def getNama(self):
              return self._element

       def getIpk(self):
              return self._ipk

       def setNama(self,nama):
              self._element = nama
       def setIpk(self,ipk):
              self._ipk = ipk

class DLLNC:
       def __init__(self):
              self.head = None
              self.tail = None
              self.size = 0

       def isEmpty(self):
              return self.size == 0

       def len(self):
              return self.size

       def addElementTail(self, nama, ipk):
              baru = NodeMahasiswa(nama,ipk)
              if self.size == 0:
                     self.head = baru
                     self.tail = baru
                     self.head.next = None
                     self.head.prev = None
                     self.tail.next = None
                     self.tail.prev = None
              else:
                     self.tail.next = baru
                     baru.prev = self.tail
                     self.tail = baru
                     self.tail.next = None
                     self.size = self.size + 1
              print("data masuk ke tail")
              

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

              print("=== Print Descending ===")
              print("="*24)
              while(bantu != None):   
                     print("Nama :",bantu.getNama())
                     print("IPK  :",bantu.getIpk())
                     bantu = bantu._prev
              print()

DLLNC = DLLNC()
DLLNC.addElementTail('Shalom',3.9)
DLLNC.addElementTail('Nabilla',3.8)
DLLNC.addElementTail('Kurniadi',3.7)
DLLNC.addElementTail('Harris',3.6)
DLLNC.printAllDescending()
DLLNC.deleteLast()
DLLNC.printDescending()
DLLNC.rataIpk()
