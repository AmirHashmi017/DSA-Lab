class RBNode:
    def __init__(self,value,color='red'):
        self.value=value
        self.color=color
        self.left=None
        self.right=None
        self.parent=None
        self.size=1

    def UpdateSize(self):
        leftsize=0
        rightsize=0
        if(self.left!=None):
            leftsize=self.left.size
        if(self.right!=None):
            rightsize=self.right.size
        self.size=1+leftsize+rightsize

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
                current.size+=1
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
                
    def delete(self, value):
        node_to_remove = self.Search(value)

        if node_to_remove is None:
            return

        if node_to_remove.left is None or node_to_remove.right is None:
            self._replace_node(
                node_to_remove, node_to_remove.left or node_to_remove.right)
        else:
            successor = self.FindMinimum(node_to_remove.right)
            node_to_remove.value = successor.value
            self._replace_node(successor, successor.right)

        self.delete_fix(node_to_remove)

    def delete_fix(self, x):
        while x != self.root and x.color == 'black':
            if x == x.parent.left:
                sibling = x.sibling()
                if sibling.color == 'red':
                    sibling.color = 'black'
                    x.parent.color = 'red'
                    self.rotate_left(x.parent)
                    sibling = x.sibling()
                if (sibling.left is None or sibling.left.color == 'black') and (sibling.right is None or sibling.right.color == 'black'):
                    sibling.color = 'red'
                    x = x.parent
                else:
                    if sibling.right is None or sibling.right.color == 'black':
                        sibling.left.color = 'black'
                        sibling.color = 'red'
                        self.rotate_right(sibling)
                        sibling = x.sibling()
                    sibling.color = x.parent.color
                    x.parent.color = 'black'
                    if sibling.right:
                        sibling.right.color = 'black'
                    self.rotate_left(x.parent)
                    x = self.root
            else:
                sibling = x.sibling()
                if sibling.color == 'red':
                    sibling.color = 'black'
                    x.parent.color = 'red'
                    self.rotate_right(x.parent)
                    sibling = x.sibling()
                if (sibling.left is None or sibling.left.color == 'black') and (sibling.right is None or sibling.right.color == 'black'):
                    sibling.color = 'red'
                    x = x.parent
                else:
                    if sibling.left is None or sibling.left.color == 'black':
                        sibling.right.color = 'black'
                        sibling.color = 'red'
                        self.rotate_left(sibling)
                        sibling = x.sibling()
                    sibling.color = x.parent.color
                    x.parent.color = 'black'
                    if sibling.left:
                        sibling.left.color = 'black'
                    self.rotate_right(x.parent)
                    x = self.root
        x.color = 'black'

    def _replace_node(self, old_node, new_node):
        if old_node.parent is None:
            self.root = new_node
        else:
            if old_node == old_node.parent.left:
                old_node.parent.left = new_node
            else:
                old_node.parent.right = new_node
        if new_node is not None:
            new_node.parent = old_node.parent

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
        node.UpdateSize()
        RightChild.UpdateSize()

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
        node.UpdateSize()
        LeftChild.UpdateSize()
        


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
    
    def FindMedian(self):
        if(self.root==None):
            return None
        totalnodes=self.root.size
        if(totalnodes%2==1):
            return self.FindKth(self.root,totalnodes//2+1).value
        else:
            leftmiddle=self.FindKth(self.root,totalnodes//2).value
            rightmiddle=self.FindKth(self.root,totalnodes//2+1).value
            return (leftmiddle+rightmiddle)//2
    
    def FindKth(self,node,K):
        leftsize=0
        if(node.left!=None):
            leftsize=node.left.size
        if(leftsize==K-1):
            return node
        elif(leftsize>K-1):
            return self.FindKth(node.left,K)
        elif(leftsize<K-1):
            return self.FindKth(node.right,K-leftsize-1)


# Example driver code
if __name__ == "__main__":
    tree = RedBlackTree()
    tree.Insert(10)
    tree.Insert(20)
    tree.Insert(30)
    tree.Insert(40)
    tree.Insert(45)
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
    median = tree.FindMedian()
    print("\n Median of the Red-Black Tree:", median)
    tree.delete(20)

    print("Inorder traversal of the Red-Black Tree after deleting 20")
    tree.InOrderTraversal(tree.root)
    print()