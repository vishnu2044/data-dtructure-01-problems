class Node:
    def __init__(self, data):
        self.data = data
        self.refer = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_linked_list(self):
        element = self.head
        if element == None:
            print("The linked list is empty !!!")
        else:
            while element != None:
                print(element.data)
                element = element.refer

    def add_Val_begin(self, data):
        newnode = Node(data)
        newnode.refer = self.head
        self.head = newnode

    def add_val_after(self, data, val):
        element = self.head
        newnode = Node(data)
        if element == None:
            print("The linked list is empty!!")
        else:
            while element.refer != None:
                if element.data == val:
                    break
                element = element.refer
            newnode.refer = element.refer
            element.refer = newnode


    def add_val_before(self, data, val):
        element = self.head
        newnode = Node(data)
        if element == None:
            print("the linkedlist is empty!!")
            return
        if element.data == val:
            mylist.add_Val_begin(data)
        else:
            while element.refer != None:
                if element.refer.data == val:
                    break
                element = element.refer
            newnode.refer = element.refer
            element.refer = newnode

mylist = LinkedList()
mylist.add_Val_begin(40)
mylist.add_Val_begin(30)
mylist.add_Val_begin(20)
mylist.add_Val_begin(10)
mylist.add_val_after(25, 20)
mylist.add_val_before(35, 40)

mylist.print_linked_list()
