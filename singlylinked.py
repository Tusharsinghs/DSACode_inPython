class Node:                   
    def __init__(self,data):
        self.data=data
        self.next=None
    def __repr__(self):
        return self.data
'''class Linkedlist:              #creation of linked list
    def __init__(self):
        self.head=None
    def __repr__(self):
        node=self.head
        nodes=[]
        while node is not None:
            nodes.append(node.data)
            node=node.next
        nodes.append('None')
        return "->".join(nodes)

llist=Linkedlist()
print(llist)
o1=Node('a')
llist.head=o1
print(llist)'''

#traversing in linked list
class Linkedlist:
    def __init__(self,nodes=None):
        self.head=None
        if nodes is not None:
            node=Node(data=nodes.pop(0))
            self.head=node
            for ele in nodes:
                node.next=Node(data=ele)
                node=node.next
    def __repr__(self):
        node=self.head
        nodes=[]
        while node is not None:
            nodes.append(node.data)
            node=node.next
        nodes.append('None')
        return "->".join(nodes)
    def __iter__(self):                 #traversing over linked list
        node=self.head
        while node is not None:
            yield node
            node=node.next
    def add_first(self,node):            #inserting elements at beginning.....         
        node.next=self.head
        self.head=node
    def add_last(self,node):             #inserting elements at the end
        if self.head is None:
            self.head=node
            return
        for current_node in self:
            pass
        current_node.next=node
    def add_after(self,target_node,new_node):           #inserting after a certain node
        if self.head is None:
            raise Exception("List is empty")
        for node in self:
            if node.data==target_node:
                new_node.next=node.next
                node.next=new_node
                return
        raise Exception("Node with data %s not found"%target_node)

    def remove_node(self,target_node):           #deletion of certain node
        if self.head is None:
            raise Exception("List is empty")
        if self.head.data==target_node:
            self.head=self.head.next
            return
        previous_node=self.head
        for node in self:
            if node.data==target_node:
                previous_node.next=node.next
                return
            previous_node=node
        raise Exception("Node with data %s not found"%target_node)
        
        

llist=Linkedlist(['a','b','c','d','e'])
print(llist)
for node in llist:
    print(node)

llist=Linkedlist()
llist.add_first(Node('t'))  #elements are added in first place in t->None  format
llist.add_first(Node('r'))  #elements are added in first place in r->t->None  format
print(llist)

llist=Linkedlist(['a','b','c','d','e'])
llist.add_last(Node('m'))  #elements are added at last place
llist.add_last(Node('n'))  #elements are added at last place
print(llist)

llist=Linkedlist(['a','b','c','d','e'])    #elements are added after a certain place
llist.add_after('c',Node('s'))
print(llist)


llist=Linkedlist(['a','b','c','d','e'])    #deletion of elements
llist.remove_node('c')
print(llist)


