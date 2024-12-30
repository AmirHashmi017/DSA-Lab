class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
        self.height=1
    
def Height(node):
    if(node==None):
        return 0
    return node.height

def BalanceFactor(node):
    return Height(node.left)-Height(node.right)

def RotateLeft(x):
    y=x.right
    T2=y.left

    y.left=x
    x.right=T2

    y.height=1+max(Height(y.left),Height(y.right))
    x.height=1+max(Height(x.left),Height(x.right))

    return y

def RotateRight(y):
    x=y.left
    T2=x.right

    x.right=y
    y.left=T2

    y.height=1+max(Height(y.left),Height(y.right))
    x.height=1+max(Height(x.left),Height(x.right))

    return x

def FindMinNode(node):
    current=node
    while(current.left!=None):
        current=current.left
    return current

def Insert(root,key):
    if(root==None):
        return Node(key)
    if(key<root.key):
        root.left=Insert(root.left,key)
    elif(key>root.key):
        root.right=Insert(root.right,key)
    else:
        return root
    
    root.height=1+max(Height(root.left),Height(root.right))
    balance=BalanceFactor(root)

    if(balance>1 and key<root.left.key):
        return RotateRight(root)
    
    if(balance<-1 and key>root.right.key):
        return RotateLeft(root)
    
    if(balance>1 and key>root.left.key):
        root.left=RotateLeft(root.left)
        return RotateRight(root)
    
    if(balance<-1 and key<root.right.key):
        root.right=RotateRight(root.right)
        return RotateLeft(root)
    
    return root

def Delete(root,key):
    if(root==None):
        return root
    elif(key<root.key):
        root.left=Delete(root.left,key)
    elif(key>root.key):
        root.right=Delete(root.right,key)
    else:
        if(root.left==None or root.right==None):
            if(root.left):
                temp=root.left
            elif(root.right):
                temp=root.right
            if(temp==None):
                root=None
            else:
                root=temp
        else:
            temp=FindMinNode(root.right)
            root.key=temp.key
            root.right=Delete(root.right,temp.key)

    if(root==None):
        return root
    
    root.height=1+max(Height(root.left),Height(root.right))
    balance=BalanceFactor(root)

    if(balance>1 and BalanceFactor(root.left)>=0):
        return RotateRight(root)
    
    if(balance<-1 and BalanceFactor(root.right)<=0):
        return RotateLeft(root)
    
    if(balance>1 and BalanceFactor(root.left)<0):
        root.left=RotateLeft(root.left)
        return RotateRight(root)
    
    if(balance<-1 and BalanceFactor(root.right)>0):
        root.right=RotateRight(root.right)
        return RotateLeft(root)
    
    return root

def Search(root,key):
    if(root==None):
        return None
    elif(key==root.key):
        return root.key
    elif(key<root.key):
        return Search(root.left,key)
    elif(key>root.key):
        return Search(root.right,key)
    else:
        return None
       

def PreOrder(node):
    if(node!=None):
        print(node.key,end=" ")
        PreOrder(node.left)
        PreOrder(node.right)

def InOrder(node):
    if(node!=None):
        InOrder(node.left)
        print(node.key,end=" ")
        InOrder(node.right)

def PostOrder(node):
    if(node!=None):
        PostOrder(node.left)
        PostOrder(node.right)
        print(node.key,end=" ")

# Driver code
root = None

root = Insert(root, 9)
root = Insert(root, 5)
root = Insert(root, 10)
root = Insert(root, 0)
root = Insert(root, 6)
root = Insert(root, 11)
root = Insert(root, -1)
root = Insert(root, 1)
root = Insert(root, 2)

print("Preorder traversal of the "
      "constructed AVL tree is")
PreOrder(root)
print(f"\nSearching for 10, {Search(root,10)} found.")
root = Delete(root, 10)

print("\nPreorder traversal after"
          " deletion of 10")
PreOrder(root)
print(f"\nSearching for 10, {Search(root,10)} found.")
print("\nInorder traversal: ")
InOrder(root)
print("\nPostorder traversal: ")
PostOrder(root)


    