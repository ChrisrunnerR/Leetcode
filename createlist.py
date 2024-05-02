

class LinkedList:

    #create an node with data 
    class Node:
        def __init__(self, data: int ) -> None:
            self.data  = data
            self.next = None

    #make the head node = none 
    def __init__(self) -> None:
        self.head = None

    
    def insert(self, data ) -> str:

        #create an instance of node and pass in data 
        new_node = self.Node(data)

        # if the head == null then make new node head
        if self.head == None:
            self.head = new_node
        
        else:
         #crete an instance of head node and interate until next = none
            curr = self.head

            while curr.next is not None:
                curr = curr.next
            curr.next = new_node

    def printVals(self):
        curr = self.head 

        while curr is not None:
            print(curr.data)
            curr = curr.next


ll = LinkedList()
ll.insert(5)
ll.insert(6)
ll.insert(7)
ll.insert(8)
ll.insert(9)

ll.printVals()



       





