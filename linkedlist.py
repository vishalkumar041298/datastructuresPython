#creating linked list and printing the linked list
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
    def printll(self):
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

firstnode=Node("vishal")
ll=LinkedList()
ll.insert(firstnode)

secondnode=Node("kumar")
th=Node("S")
ll.insert(secondnode)
ll.insert(th)
ll.printll()