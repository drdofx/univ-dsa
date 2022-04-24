# Linked List and Node can be accomodated in separate classes for convenience
class Node(object):
    # Each node has its data and a pointer that points to next node in the Linked List
    def __init__(self, nama, nilai, next = None):
        self.nama = nama
        self.nilai = nilai
        self.next = next
        
    # function to set data
    def setData(self, data):
        self.data = data
        
    # function to get data of a particular node
    def getData(self):
        return self.data
    
    # function to set next node
    def setNext(self, next):
        self.next = next
        
    # function to get the next node
    def getNext(self):
        return self.next
    
class LinkedList(object):
    # Defining the head of the linked list
    def __init__(self):
        self.head = None
        
    # print linked list length   
    def length(self):
        node = self.head
        count = 0
        while node:
            count +=1
            node=node.next
        return count

    # printing the data in the linked list
    def printLinkedList(self):
        temp = self.head
        while(temp): 
            print(temp.nama + '-' + temp.nilai + ' -> ')
            temp = temp.next
            
    # inserting the node at the beginning
    def insertAtStart(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
        print(f"{data} inserted at the beginning")
        self.printLinkedList()
        print()
        
    # inserting the node in between the linked list (after a specific node)
    # def insertBetween(self, previousNode, data):
    #     if (previousNode.next is None):
    #         print('Previous node should have next node!')
    #     else:
    #         newNode = Node(data)
    #         newNode.next = previousNode.next
    #         previousNode.next = newNode
    def insertBetween(self, name, data):
        temp = self.head
        while(temp.next != None):
            if(temp.data['nama'] == name):
                break
            temp = temp.next

        if (temp.next is None):
            print('Node tidak ada! Insert data gagal!')
            print()
            return 

        newNode = Node(data)
        newNode.next = temp.next
        temp.next = newNode
        print(f"{data} inserted between {name} and {newNode.next.data['nama']}")
        self.printLinkedList()
        print()
            
    # inserting at the end of linked list
    def insertAtEnd(self, data):
        newNode = Node(data)
        temp = self.head
        if (temp == None):
            return self.insertAtStart(data)
        while(temp.next != None):         # get last node
            temp = temp.next
        temp.next = newNode
        print(f"{data} inserted at the end")
        self.printLinkedList()
        print()
        
    # deleting an item based on data(or key)
    def delete(self, data):
        temp = self.head
        if (temp.next == None):
            if(temp.data['nama'] == data):
                self.head = None
                return
            return False
        else:
            # if data/key is found in head node itself
            if(temp.data['nama'] == data):
                self.head = temp.next
                temp = None
                return
            else:
                #  else search all the nodes
                while(temp.next != None):
                    if(temp.data['nama'] == data):
                        break
                    prev = temp          #save current node as previous so that we can go on to next node
                    temp = temp.next
                
                # node not found
                if temp == None:
                    return False
                
                prev.next = temp.next
                return

    def deleteLast(self):
        temp = self.head
        if (temp.next == None):
            self.head = None
            return
        while(temp.next != None):
            prev = temp
            temp = temp.next
        prev.next = temp.next

    # iterative search
    def search(self, node, data):
        if node == None:
            return False
        if node.data == data:
            return True
        return self.search(node.getNext(), data)
            
if __name__ == '__main__':
    print("original code: https://github.com/OmkarPathak/Data-Structures-using-Python/blob/master/Linked%20Lists/SinglyLinkedList.py")
    print("modified by Daffa Arviano (github.com/drdofx)\n")
    List = LinkedList()
    
    def printMenu():
        List.printLinkedList()
        print("Jumlah list: " + str(List.length(List.head)))

    def insertMenu():
        while True:
            nama = input('Masukkan nama: ')
            if (nama == '.'):
                break

            nilai = int(input("masukkan data nilai: "))

            where = int(input("masukkan letak: "))
            if (where == 1):
                List.insertAtStart({'nama': nama, 'nilai': nilai})
            elif (where == 2):
                List.insertAtEnd({'nama': nama, 'nilai': nilai})
            else:
                prevNode = input("Setelah nama siapa?: ")
                List.insertBetween(prevNode, {'nama': nama, 'nilai': nilai})

    def deleteMenu():
        data = input('Masukkan nama yang ingin dihapus: ')
        if (List.delete(data) == False):
            print("Data tidak ada!")
        else:
            print(f"{data} dihapus")

    
    choice = 1
    
    def menu(choice):
        if choice == 1:
            insertMenu()
        elif choice == 2:
            if (List.length(List.head) == 0):
                print('Tidak ada data yang bisa dihapus karena List kosong!')
            else:
                deleteMenu()
        elif choice == 3:
            printMenu()
        elif choice == 4:
            List.deleteLast()    
        
        else:
            print('Exit')
            return
        
        
        print("\n-----PROGRAM LINKED LIST------")
        print('\n1. Insert\n2. Delete\n3. Print\n4. Exit\n')
        choice = int(input('Masukkan pilihan: '))
        return menu(choice)

    menu(choice)
    # List.insertAtStart({"nama": "d", "nilai": 90})
    # print(List.length(List.head))
    # List.head = Node(1)                   # create the head node
    # node2 = Node(2)
    # List.head.setNext(node2)           # head node's next --> node2
    # node3 = Node(3)
    # node2.setNext(node3)                # node2's next --> node3
    # List.insertAtStart(4)                   # node4's next --> head-node --> node2 --> node3
    # List.insertBetween(node2, 5)     # node2's next --> node5
    # List.insertAtEnd({"nama": "d", "nilai": 5})
    # List.printLinkedList()
    # print()
    # List.delete(3)
    # List.printLinkedList()
    # # print()
    # print(List.search(List.head, 1))
    # List.printLinkedList()