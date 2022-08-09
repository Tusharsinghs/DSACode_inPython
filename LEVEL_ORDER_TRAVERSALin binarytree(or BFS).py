class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def printlevelorder(root):
    h=height(root)
    for i in range(1,h+1):
        printcurrentorder(root,i)
def printcurrentorder(root,level):
    if root is None:
        return
    if level==1:
        print(root.val,end=" ")
    elif level>1:
        printcurrentorder(root.left,level-1)
        printcurrentorder(root.right,level-1)
def height(node):
    if node is None:
        return 0
    else:
        lheight=height(node.left)
        rheight=height(node.right)
        if lheight>rheight:
            return lheight+1
        else:
            return rheight+1

    
root=Node(1)
root.left=Node(2)
root.right=Node(6)
root.left.left=Node(23)
root.left.right=Node(67)
print("Level order traversal is")
printlevelorder(root)
