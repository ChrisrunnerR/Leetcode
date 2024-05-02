
class BST:

    #creating a node in with left and right pointers 
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None 
    
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        #create a node instance 
        new_node = self.Node(data)
       # print(type(new_node))

        if self.root is None:
            self.root = new_node
        else:
            #set curr  to root 
            current = self.root
            while True:
                if data < current.data:
                    #check if left is null else current goes to left 
                    if current.left is None:
                        current.left = new_node
                        break
                    current = current.left
                elif data > current.data:
                    if current.right is None:
                        current.right = new_node
                        break
                    current = current.right
    def inOrder(self, node):
       if node:
           self.inOrder(node.left)
           print(node.data, end=" ")
           self.inOrder(node.right)


    def printInOrder(self):
        self.inOrder(self.root)
        print()  # For newline after the traversal


tree = BST()

tree.insert(10)
tree.insert(7)
tree.insert(13)
tree.insert(4)
tree.insert(1)
tree.insert(5)
tree.insert(8)
tree.insert(14)

tree.printInOrder()
           


       

