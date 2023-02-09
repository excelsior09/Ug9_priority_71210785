from NodeTabungan import NodeTabungan


class SLLNC:
    _size = 0
    _head = None
    _tail = None

    def init(self):
        self._size = 0
        self._head = None
        self._tail = None
    
    def len(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def insert_head(self,norek,nama,saldo):
        new_node = NodeTabungan(norek,nama,saldo)
        if(self.isEmpty()):
            self._head = new_node
            self._tail = new_node
            self._tail.next = None
        else:
            new_node.next = self._head
            self._head = new_node
        self._size += 1

    def delete(self, position):
        if self._size == 0:
            return False
        elif position == 0:
            self.delete(0)
        elif position + 1 >= self._size:
            self.delete(self._size)
        else:
            delete_node = self._head
            for i in range(position):
                delete_node = delete_node.next
            helper = self._head
            while helper.next != delete_node:
                helper = helper.next
            helper.next = delete_node.next
            del delete_node
            self._size = self._size - 1

    def print(self):
        if(not self.isEmpty()):
            bantu=self._head
            while(bantu!=None):
                print('Norek:',bantu.no_rekening)
                print('Nama:',bantu.nama)
                print('Saldo:',bantu.saldo)
                print()
                bantu=bantu.next
            
        else:
            print('Kosong!')
    
    def filter(self,min_rek):
        bantu = self._head
        for i in range(self._size):
            if bantu.saldo<=min_rek:
                self.delete(i)
                self._size-=1
            bantu=bantu.next            

    def update(self, bunga):
        if bunga>=0 and bunga<=100:
            bantu=self._head
            print('Semua saldo rekening berhasil ditambah sebanyak',bunga,'%')
            bunga=bunga/100
            for i in range(self._size):
                bantu.saldo=bantu.saldo+(bantu.saldo*bunga)
                bantu=bantu.next
        else:
            print('Maaf besaran persen harus diantara 0-100')

sllnc=SLLNC()
sllnc.insert_head(201,"Hanif", 250000)
sllnc.insert_head(110,"Yudha", 150000)
sllnc.print()
sllnc.filter(100)
sllnc.print()
sllnc.update(200)
sllnc.update(50)
sllnc.print()