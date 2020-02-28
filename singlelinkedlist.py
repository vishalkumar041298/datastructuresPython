#implementing linked list and doing functions in that
class Node:
    def __init__(self,data): #initialising node : node has two parts
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):          #initialising linked list : which as head as empty
        self.head=None          

    def insert(self,newnode): #inserting new element
        if self.head is None:  #checking if head node is empty and making a new node as head
            self.head=newnode
        else:
            currentnode=self.head   #if head node is not empty take head node as current node 
            while 1:                   # check current node's next is empty then make current nodes next as new node break
                if currentnode.next is None:
                    currentnode.next=newnode
                    break
                else:                           #current node's new node is not empty  make current nodes next node as current node and repeat while loop
                    currentnode=currentnode.next
    def printll(self):               #printing everynode's data
        currentnode=self.head
        if self.head is None:
            print("list is empty")
        else:
            while 1:
                if currentnode.next !=None:
                    print (currentnode.data)
                    currentnode=currentnode.next
                else:
                    print(currentnode.data)    
                    break
    def insertnewhead(self,newnode): #interchanging with headnode and new node
    
        newnode.next=self.head
        self.head=newnode   
    def insertbet(self,newnode,s1,s2): #insert newnode inbetween given value of nodes
        currentnode=self.head
        while 1:
            
            if currentnode.data==s1 and currentnode.next.data==s2:
                temp=currentnode.next

                
                currentnode.next=newnode
                newnode.next=temp
                del temp
                break
            currentnode=currentnode.next

    def insertAt(self,newnode,position): #insert newnode at position
        currentnode=self.head
        previousnode=currentnode
        count=0
        while 1:
            if position==0:
                self.insertnewhead(newnode)
                break
            elif  count==position:
                previousnode.next=newnode
                newnode.next=currentnode
                break
            else:
                count+=1
                previousnode=currentnode
                currentnode=currentnode.next
    def length(self):  #finding length of the list
        count=1
        currentnode=self.head
        while 1:
            if currentnode.next is None:
                break           
            currentnode=currentnode.next
            count+=1 
        return count 
    def deleteend(self):
        currentnode=self.head
        previousnode=currentnode
        while 1:
            if currentnode.next is None:
                previousnode.next=None
                # del currentnode ==> deletes but reference is there so we should put previous node next as node
                break
            previousnode=currentnode
            currentnode=currentnode.next
    def deletehead(self):
        currentnode=self.head   #deleting head node
        self.head=currentnode.next
        del currentnode      
    def deletebet(self,s1):
        currentnode=self.head  #deleting inbetween node
        previousnode=currentnode
        nextnode=currentnode.next
        while 1:
            if currentnode.data==s1:
                nextnode=currentnode.next
                previousnode.next=currentnode.next
                currentnode.next=None
                break
            previousnode=currentnode
            currentnode=currentnode.next   
             

firstnode=Node("vishal")
ll=LinkedList()
ll.insert(firstnode)

secondnode=Node("kumar")
th=Node("S")
ll.insert(secondnode)
ll.insert(th)
newhead=Node("new head")

ll.insertnewhead(newhead)
ll.insertnewhead(Node("new new head"))
op=Node("betweeweeeeeen")
ll.insertbet(op,"vishal","kumar")
at=Node("atttttttttttttttt")
ll.insertAt(at,2)

ll.printll() 
print(ll.length())
ll.deleteend()  
ll.printll()  
print(ll.length())
ll.deletehead()           
ll.printll()
ll.deletebet("vishal")
ll.printll()
print(ll.length())