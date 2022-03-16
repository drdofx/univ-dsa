# Single Linked List, terdapat 2 class: Node, LinkedList
class Node(object):
    # Each node has its data and a pointer that points to next node in the Linked List
    def __init__(self, data, next = None):
        self.data = data
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
    def length(self, node):
        count = 0
        while node:
            count +=1
            node=node.next
        return count

    # printing the data in the linked list
    def printLinkedList(self):
        temp = self.head
        while(temp):
            if (temp.next == None): 
                print(temp.data)
            else:
                print(temp.data, end=' -> ')
            temp = temp.next
            
    # inserting the node at the beginning
    def insertAtStart(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
        print(f"{data} inserted at the beginning")
        self.printLinkedList()
        print()
        
    def insertBetween(self, prevNode, data):
        temp = self.head
        while(temp.next != None):
            if(temp.data == prevNode):
                break
            temp = temp.next

        if (temp.next is None):
            if self.length(self.head) == 1:
                return self.insertAtEnd(data)

            print('Node tidak ada! Insert data gagal!\n')
            return 

        newNode = Node(data)
        newNode.next = temp.next
        temp.next = newNode
        print(f"{data} inserted between {prevNode} and {newNode.next.data}")
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
            if(temp.data == data):
                self.head = None
                return
            return False
        else:
            # if data/key is found in head node itself
            if(temp.data == data):
                self.head = temp.next
                temp = None
                return
            else:
                #  else search all the nodes
                while(temp.next != None):
                    if(temp.data == data):
                        break
                    prev = temp          #save current node as previous so that we can go on to next node
                    temp = temp.next
                
                # node not found
                if temp == None:
                    return False
                
                prev.next = temp.next
                return
            
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
        list_length = List.length(List.head)
        print()
        if (list_length):
            print(f"Linked List Length: {list_length}\n")
        else:
            print(f"Linked List Length: {list_length}\nstatus: kosong!\n")

    def insertMenu():
        print("-----PROGRAM LINKED LIST------")
        print('\n1. Print List\n2. Insert First\n3. Insert After\n4. Insert Last\n5. End\n')
        choice = int(input("Masukkan pilihan: "))
        if choice == 1:
            printMenu()
        elif choice == 2:
            data = int(input('Masukkan data: '))
            List.insertAtStart(data)
        elif choice == 3:
            data = int(input('Masukkan data: '))
            prevNode = int(input('Masukkan node sebelumnya: '))
            List.insertBetween(prevNode, data)
        elif choice == 4:
            data = int(input('Masukkan data: '))
            List.insertAtEnd(data)
        else:
            print('End')
            return 

        return insertMenu() # recursive function call selama pilihan bukan 1 sampai 4

    # call function menu pertama saat script di-run
    insertMenu()