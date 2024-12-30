class BinaryTree:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
    
    def Insert(self,value):
        if(value<self.value):
            if(self.left==None):
                self.left=BinaryTree(value)
            else:
                self.left.Insert(value)
        elif(value>self.value):
            if(self.right==None):
                self.right=BinaryTree(value)
            else:
                self.right.Insert(value)
    
    def Search(self,value):
        if(value==self.value):
            return self
        elif(value<self.value and self.left!=None):
            return self.left.Search(value)
        elif(value>self.value and self.right!=None):
            return self.right.Search(value)
        return None
    
    def FindMaximum(self):
        maximum=self
        while(maximum.right!=None):
            maximum=maximum.right
        return maximum
    
    def FindMinimum(self):
        minimum=self
        while(minimum.left!=None):
            minimum=minimum.left
        return minimum
    
    def FindSuccessor(self,Node):
        if Node.right!=None:
            return Node.right.FindMinimum()
        
        successor=None
        current=self
        while(self!=None):
            if(Node.value<current.value):
                successor=current
                current=current.left
            elif(Node.value>current.value):
                current=current.right
            else:
                break
        return successor

    def FindPredecessor(self,Node):
        if Node.left!=None:
            return Node.left.FindMaximum()
        predecessor=None
        current=self
        while(current!=None):
            if(Node.value>current.value):
                predecessor=current
                current=current.right
            elif(Node.value<current.value):
                current=current.left
            else:
                break
        return predecessor
    
    def InOrderTraversal(self):
        if(self.left!=None):
            self.left.InOrderTraversal()
        print(self.value,end=" ")
        if(self.right!=None):
            self.right.InOrderTraversal()

    def PreOrderTraversal(self):
        print(self.value,end=" ")
        if(self.left!=None):
            self.left.PreOrderTraversal()
        if(self.right!=None):
            self.right.PreOrderTraversal()

    def PostOrderTraversal(self):
        if(self.left!=None):
            self.left.PostOrderTraversal()
        if(self.right!=None):
            self.right.PostOrderTraversal()  
        print(self.value,end=" ")

    def Delete(self,value):
        if(value<self.value):
            if(self.left!=None):
                self.left=self.left.Delete(value)
        elif(value>self.value):
            if(self.right!=None):
                self.right=self.right.Delete(value)
        else:
            if(self.left==None):
                return self.right
            elif(self.right==None):
                return self.left

            successor=self.right.FindMinimum()
            self.value=successor.value
            self.right=self.right.Delete(successor.value)
        return self

if __name__ == "__main__":
    # Create the tree
    root = BinaryTree(20)
    root.Insert(10)
    root.Insert(30)
    root.Insert(5)
    root.Insert(15)
    root.Insert(25)
    root.Insert(35)
    root.Insert(17)

    # Traversals
    print("In-order Traversal:")
    root.InOrderTraversal()
    print("\nPre-order Traversal:")
    root.PreOrderTraversal()
    print("\nPost-order Traversal:")
    root.PostOrderTraversal()

    # Search for a node
    search_node = 15
    result = root.Search(search_node)
    if result:
        print(f"\n\nNode {search_node} found in the tree.")
    else:
        print(f"\n\nNode {search_node} not found in the tree.")

    # Find minimum and maximum
    print("\nMinimum value:", root.FindMinimum().value)
    print("Maximum value:", root.FindMaximum().value)

    # Find successor and predecessor
    successor = root.FindSuccessor(root.Search(15))
    if successor:
        print("\nSuccessor of 15:", successor.value)
    else:
        print("\nSuccessor of 15 does not exist.")

    predecessor = root.FindPredecessor(root.Search(15))
    if predecessor:
        print("Predecessor of 15:", predecessor.value)
    else:
        print("Predecessor of 15 does not exist.")

    # Delete a node
    print("\nDeleting 20...")
    root.Delete(20)
    print("In-order Traversal after deletion:")
    root.InOrderTraversal()     

        
    
        