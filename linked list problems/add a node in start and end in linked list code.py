class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_linked_list(self):
        if self.head == None:
            print("The linked list is empty!!")
        else:
            element = self.head
            while element != None:
                print(element.data)
                element = element.ref

    def add_val_begin(self, data):
        newnode = Node(data)
        newnode.ref = self.head
        self.head = newnode

    def add_val_end(self, data):
        newnode = Node(data)
        if self.head == None:
            self.head = newnode
        else:
            element = self.head
            while element.ref != None:
                element = element.ref
            element.ref = newnode


mylist = LinkedList()
mylist.add_val_begin(10)
mylist.add_val_begin(20)
mylist.add_val_end(40)
mylist.add_val_end(50)
mylist.print_linked_list()


