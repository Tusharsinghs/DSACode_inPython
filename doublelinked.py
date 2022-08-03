#doubly linkedlist
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def __repr__(self):
        return self.data

class Linkedlist:
    def __init__(self):
        self.head=None
    def __repr__(self):
        node=self.head
        nodes=[]
        while node is not None:
            nodes.append(node.data)
            node=node.next
        nodes.append("None")
        return "->".join(nodes)

    def add_first(self,new_data):
        new_node=Node(data=new_data)
        new_node.next=self.head
        new_node.prev=None
        if self.head is not None:
            self.head.prev=new_node
        self.head=new_node  #move the head to point to new node

    def add_after(self,prev_node,new_data):
        if prev_node is None:
            print("This node doesnt exist in DLL")
            return
        new_node=Node(data=new_data)
        new_node.next=prev_node.next
        prev_node.next=new_node
        new_node.prev=prev_node
        if new_node.next:
            new_node.next.prev=new_node

    def add_end(self,new_data):
        new_node=Node(data=new_data)
        last=self.head
        while last.next:
            last=last.next
        last.next=new_node
        new_node.prev=last
        return
    
        
        
        
        
        

li=Linkedlist()
print(li)
li.add_first('a')
li.add_first('s')
print(li)
li.add_after(li.head.next,'r')
print(li)
li.add_end('u')
print(li)

        
