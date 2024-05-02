class BST:

    class Node:

        def __init__(self,data: int ) -> None:
            self.data = data
            self.left = None
            self.right = None
    
    #create a root and set to Null
    def __init__(self) -> None:
        self.root = None


    def insert(self, data: int ) -> None:

        #want to crete instnace of node
        new_node = self.Node(data)

        #if the root is null then make newnode root 

        if self.root is None:
            self.root = new_node
        else:
            #now we need to iterate to left if val < curr
            #iterate towards right if data > curr 
            # if data == curr.data then we need to return an error "val already inserted "

            curr = self.root
            while True:

                if data > curr.data:
                    if curr.right is None:
                        curr.right = new_node
                        break
                    else:
                        curr = curr.right
                elif data < curr.data:
                    if curr.left is None:
                        curr.left = new_node
                        break
                    else:
                        curr = curr.left
                # this is in test case we have dup data val
                else:
                    break
    def printTree(self) -> None:
        self._printInOrder(self.root)


        
    def _printInOrder(self, root) -> None:
        if not root:
            return
        else:
            self._printInOrder(root.left)
            print(root.data)
            self._printInOrder(root.right)



# create an instance of BST

bst = BST()
bst.insert(5)
bst.insert(6)
bst.insert(7)
bst.insert(4)
bst.insert(1)

bst.printTree()

       
           



                


