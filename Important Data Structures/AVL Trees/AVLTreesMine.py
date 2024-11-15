class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
        self.height=1

def height(node):
    if(node==None):
        return 0
    return node.height

def CalculateBalanceFactor(node):
    return height(node.left)-height(node.right)

def RightRotate(y):
    x=y.left
    T2=x.right

    x.right=y
    y.left=T2

    y.height=1+max(height(y.left),height(y.right))
    x.height=1+max(height(x.left),height(x.right))

    return x

def LeftRotate(x):
    y=x.right
    T2=y.left

    y.left=x
    x.right=T2

    y.height=1+max(height(y.left),height(y.right))
    x.height=1+max(height(x.left),height(x.right))

    return y

def Insert(node,key):
    if(node==None):
        return Node(key)
    elif(key<node.key):
        node.left=Insert(node.left,key)
    elif(key>node.key):
        node.right=Insert(node.right,key)
    else:
        return node
    
    node.height=1+max(height(node.left),height(node.right))
    balance=CalculateBalanceFactor(node)

    if(balance>1 and key<node.left.key):
        return RightRotate(node)
    
    if(balance<-1 and key>node.right.key):
        return LeftRotate(node)
    
    if(balance>1 and key>node.left.key):
        node.left=LeftRotate(node.left)
        return RightRotate(node)
    
    if(balance<-1 and key<node.right.key):
        node.right=RightRotate(node.right)
        return LeftRotate(node)
    
    return node

def MinValue(node):
    current=node
    while(current.left!=None):
        current=current.left
    return current

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
            temp=MinValue(root.right)
            root.key=temp.key
            root.right=Delete(root.right,temp.key)

    
    if(root==None):
        return root
    root.height=1+max(height(root.left),height(root.right))
    balance=CalculateBalanceFactor(root)
    if(balance>1 and CalculateBalanceFactor(root.left)>=0):
        return RightRotate(root)
    if(balance<-1 and CalculateBalanceFactor(root.right)<=0):
        return LeftRotate(root)
    if(balance>1 and CalculateBalanceFactor(root.left)<0):
        root.left=LeftRotate(root.left)
        return RightRotate(root)
    if(balance<-1 and CalculateBalanceFactor(root.right)>0):
        root.right=RightRotate(root.right)
        return LeftRotate(root)
    
    return root



def PreOrder(node):
    if(node!=None):
        print(node.key,end=" ")
        PreOrder(node.left)
        PreOrder(node.right)

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
root = Delete(root, 10)

print("\nPreorder traversal after"
          " deletion of 10")
PreOrder(root)





