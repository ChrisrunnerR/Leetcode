
class LinkedList:

    class Node:

        def __init__(self, data):
            self.data = data
            self.next = None



    def __init__(self):
        self.dup = set()
        self.head = None


    # we want to insert data by create a new node 
    def insert(self, data):

        #not allowing duplicate data just use set 

        if data in self.dup:    
           print(f"This data {data} has already been passed in")
           return

        #create  new node 
        new_node = self.Node(data)

        #if ! head new node = head 

        if not self.head:
            self.head = new_node
            self.dup.add(data)
        
        else:
            #head isn't null then we need to find 
            curr = self.head 

            while curr.next:
                curr = curr.next
            curr.next = new_node
            self.dup.add(data)
    
    def printVals(self):

        curr = self.head 

        while curr:
            print(curr.data)
            curr = curr.next

ll = LinkedList()

ll.insert(5)
ll.insert(6)
ll.insert(7)
ll.insert(8)
ll.insert(9)
ll.insert(10)
ll.insert(5)


ll.printVals()



    
