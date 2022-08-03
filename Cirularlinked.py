class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def __repr__(self):
        return self.data

class Circularlinkedlist:
    def __init__(self):
        self.head=None
    def push(self,data):
        ptr1=Node(data)
        temp=self.head
        ptr1.next=self.head
        if self.head is not None:
            while(temp.next!=self.head):
                temp=temp.next
            temp.next=ptr1
        else:
            ptr1.next=ptr1

        self.head=ptr1
    
    def printlist(self):
        temp=self.head
        if self.head is not None:
            while(True):
                print(temp.data,end=" ")
                temp=temp.next
                if(temp==self.head):
                    break

clist=Circularlinkedlist()
clist.push(12)
clist.push(34)
clist.push(56)
clist.push(83)
clist.printlist()



    
