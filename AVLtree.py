class TreeNode(object):
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        self.height=1
class AVLtree(object):
    def insert(self,root,key):
        if root is None:
            return TreeNode(key)
        if key < root.val:
            root.left=self.insert(root.left,key)
        elif key>root.val:
            root.right=self.insert(root.right,key)
        root.height=1+max(self.getheight(root.left),self.getheight(root.right))

        balance=self.getbalance(root)
        if balance>1 and key<root.left.val:
            return self.rightRotation(root)
        if balance<-1 and key>root.right.val:
            return self.leftRotation(root)
        if balance>1 and key>root.left.val:
            root.left=self.leftRotation(root.left)
            return self.rightRotation(root)
        if balance<-1 and key<root.right.val:
            root.right=self.rightRotation(root.right)
            return self.leftRotation(root)
        return root

    def leftRotation(self,z):
        y=z.right
        t2=y.left
        y.left=z
        z.right=t2
        z.height=1+max(self.getheight(z.left),self.getheight(z.right))
        y.height=1+max(self.getheight(y.left),self.getheight(y.right))
        return y
    def rightRotation(self,z):
        y=z.left
        t3=y.right
        y.right=z
        z.left=t3
        z.height=1+max(self.getheight(z.left),self.getheight(z.right))
        y.height=1+max(self.getheight(y.left),self.getheight(y.right))
        return y
    
    def getheight(self,root):
        if not root:
            return 0
        return root.height
    def getbalance(self,root):
        if not root:
            return
        return self.getheight(root.left)-self.getheight(root.right)
    def preOrder(self,root):
        if not root:
            return 0
        print("{0}".format(root.val),end=" ")
        self.preOrder(root.left)
        self.preOrder(root.right)
        
myTree=AVLtree()
root=None
root=myTree.insert(root,12)
root=myTree.insert(root,5)
root=myTree.insert(root,45)
root=myTree.insert(root,30)
print("Preorder traversal of constructed AVL tree is")
myTree.preOrder(root)
print()
    
        
    
        
        
        
