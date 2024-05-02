class LinkedList:



    class Node:
        def __init__(self, data=0):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None
        self.s = set()




    def insert(self, data):

        new_node = self.Node(data)

        if not self.head:
            self.head = new_node
            self.s.add(new_node)
        
        else:

            curr = self.head

            while curr.next:
                curr = curr.next
            
            self.s.add(new_node)
            curr.next = new_node

    
    def printData(self):

      


        curr = self.head

        while curr:
            print(curr.data)
            curr = curr.next
        
        print()


    def reverse(self):
        prev = None
        curr = self.head 

        while curr:
            temp  = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        #print(f"new head data = {prev.data}")
      #  print()
        print(id(prev))
        self.head = prev
        

        

ll = LinkedList()

ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.insert(5)
ll.insert(6)


ll.printData() 

ll.reverse()

ll.printData()







    
