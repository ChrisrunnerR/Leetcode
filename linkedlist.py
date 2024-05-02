class LinkedList:

    class Node:

        def __init__(self, data):
            self.data =data
            self.next = None
    

    def __init__(self):
        self.head = None

    # take some data make a node and append to the end of the list 
    def insert(self, data):

        #create a new node
        new_node = self.Node(data)

        #if no head node then make new node head 
        if not self.head:
            self.head = new_node
            return
        else:

            current = self.head 

            while current.next != None:
                current = current.next
            current.next = new_node

    def printList(self):
        current = self.head 

        while current != None:
            print(current.data, end = " ")
            current = current.next
        print()

ll = LinkedList()

ll.insert(5)
ll.insert(6)
ll.insert(20)
ll.insert(10)
ll.insert(3)
ll.insert(2)
ll.insert(7)

ll.printList()

