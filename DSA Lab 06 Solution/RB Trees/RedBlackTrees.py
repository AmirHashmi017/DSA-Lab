class RBNode:
    def __init__(self,value,color='red'):
        self.value=value
        self.color=color
        self.left=None
        self.right=None
        self.parent=None
    
    def Sibling(self):
        if(self.parent==None):
            return None
        if(self==self.parent.left):
            return self.parent.right
        else:
            return self.parent.left
    
    def GrandParent(self):
        if(self.parent==None):
            return None
        return self.parent.parent
    
    def Uncle(self):
        if(self.parent==None):
            return None
        return self.parent.Sibling()

class RedBlackTree:
    def __init__(self):
        self.root=None
    
    def Search(self,value):
        current=self.root
        while(current!=None):
            if(value==current.value):
                return current
            elif(value<current.value):
                current=current.left
            elif(value>current.value):
                current=current.right
        return None
    
    def Insert(self,value):
        newnode=RBNode(value)
        if(self.root==None):
            self.root=newnode
        else:
            current=self.root
            while(True):
                if(value<current.value):
                    if(current.left==None):
                        current.left=newnode
                        newnode.parent=current
                        break
                    else:
                        current=current.left
                elif(value>current.value):
                    if(current.right==None):
                        current.right=newnode
                        newnode.parent=current
                        break
                    else:
                        current=current.right
        self.InsertFixes(newnode)
    

    def InsertFixes(self,newnode):
        while(newnode.parent and newnode.parent.color=="red"):
            if(newnode.parent==newnode.GrandParent().left):
                uncle=newnode.Uncle()
                if(uncle and uncle.color=="red"):
                    newnode.parent.color="black"
                    uncle.color="black"
                    newnode.GrandParent().color="red"
                    newnode=newnode.GrandParent()
                else:
                    if(newnode==newnode.parent.right):
                        newnode=newnode.parent
                        self.RotateLeft(newnode)
                    newnode.parent.color="black"
                    newnode.GrandParent().color="red"
                    self.RotateRight(newnode.GrandParent())
                
            elif(newnode.parent==newnode.GrandParent().right):
                uncle=newnode.Uncle()
                if(uncle and uncle.color=="red"):
                    newnode.parent.color="black"
                    uncle.color="black"
                    newnode.GrandParent().color="red"
                    newnode=newnode.GrandParent()
                else:
                    if(newnode==newnode.parent.left):
                        newnode=newnode.parent
                        self.RotateRight(newnode)
                    newnode.parent.color="black"
                    newnode.GrandParent().color="red"
                    self.RotateLeft(newnode.GrandParent())

        self.root.color="black"
                


    def RotateLeft(self,node):
        RightChild=node.right
        node.right=RightChild.left
        if(RightChild.left!=None):
            RightChild.left.parent=node
        RightChild.parent=node.parent
        if(node.parent==None):
            self.root=RightChild
        elif(node==node.parent.left):
            node.parent.left=RightChild
        elif(node==node.parent.right):
            node.parent.right=RightChild
        RightChild.left=node
        node.parent=RightChild

    def RotateRight(self,node):
        LeftChild=node.left
        node.left=LeftChild.right
        if(LeftChild.right!=None):
            LeftChild.right.parent=node
        LeftChild.parent=node.parent
        if(node.parent==None):
            self.root=LeftChild
        elif(node==node.parent.left):
            node.parent.left=LeftChild
        elif(node==node.parent.right):
            node.parent.right=LeftChild
        LeftChild.right=node
        node.parent=LeftChild
        


    def FindMinimum(self,node):
        while(node.left!=None):
            node=node.left
        return node
    
    def InOrderTraversal(self,node):
        if(node!=None):
            self.InOrderTraversal(node.left)
            print(node.value,end=" ")
            self.InOrderTraversal(node.right)

    def PreOrderTraversal(self,node):
        if(node!=None):
            print(node.value,end=" ")
            self.PreOrderTraversal(node.left)
            self.PreOrderTraversal(node.right)

# Example driver code
if __name__ == "__main__":
    tree = RedBlackTree()
    tree.Insert(10)
    tree.Insert(20)
    tree.Insert(30)
    tree.Insert(40)
    tree.Insert(50)
    tree.Insert(25)
    if(tree.Search(40)):
        print("40 Found")
    else:
        print("40 not found")
    print("Inorder traversal of the Red-Black Tree:")
    tree.InOrderTraversal(tree.root)
    print()
    tree.PreOrderTraversal(tree.root)

    # tree.delete(20)

    # print("Inorder traversal of the Red-Black Tree after deleting 20")
    # tree._inorder_traversal(tree.root)
    # print()