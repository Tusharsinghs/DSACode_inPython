class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
    def insert(self,data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left=Node(data)
                else:
                    self.left.insert(data)
            elif data>self.data:
                if self.right is None:
                    self.right=Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data=data

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()
    def inorderTraversal(self,root):
        res=[]
        if root:
            res=self.inorderTraversal(root.left)
            res.append(root.data)
            res=res+self.inorderTraversal(root.right)
        return res
    def delete1(root,key):
        if root==None:
            return None
        if root.left==None and root.right==None:
            if root.key==key:
                return None
            else:
                return root
        key_node=None
        q=[]
        q.append(root)
        temp=None
        while(len(q)):
            temp=q.pop(0)
            if temp.data==key:
                key_node=temp
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
        return root
    
root=Node(12)
root.insert(4)
root.insert(14)
root.insert(6)
root.printTree()
root.delete1(4)
print(root.inorderTraversal(root))
