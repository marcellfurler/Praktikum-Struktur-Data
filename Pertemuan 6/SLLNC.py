from NodeMahasiswa import NodeMahasiswa
from NodeBasic import NodeBasic
# import File2 

class SLLNC:
    def __init__(self):
        self._head=None
        self._tail=None
        self._size=0

    def __len__(self):
        return self._size
    
    def isEmpty(self):
        return self._size==0
    
    def addElement(self, element):
        baru=NodeBasic(element,None)
        if self.isEmpty() ==True:
            self._head=baru
            self._tail=baru
            self._tail._next=None
        else:
            baru._next=self._head
            self._head=baru
        self._size+=1
        print("Data Berhasil")

    def addElementTail(self, element):
        baru=NodeBasic(element, None)
        if self.isEmpty()==True:
            self._head=baru
            self._tail=baru
            self._tail._next=None
        else:
            self._tail._next=baru
            self._tail=baru
        self._size+=1
        # print("Berhasil. yeaayy")


    def printAll(self):
        node=self._head
        while(node != None):
            print(node._element._nama)
            node=node._next


singleLinkedList=SLLNC()
print(singleLinkedList.isEmpty())
singleLinkedList.addElement( NodeMahasiswa("71220855", "Marcell", "4") )
singleLinkedList.addElement( NodeMahasiswa("71220855", "Sia", "4") )
singleLinkedList.addElement( NodeMahasiswa("71220855", "Billie Eilish", "4") )
singleLinkedList.printAll()
print()
print('Tail')
singleLinkedList.addElementTail( NodeMahasiswa("71220855", "Marcell", "4") )
singleLinkedList.addElementTail( NodeMahasiswa("71220855", "Sia", "4") )
singleLinkedList.addElementTail( NodeMahasiswa("71220855", "Billie Eilish", "4") )
singleLinkedList.printAll()