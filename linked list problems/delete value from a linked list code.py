class Node:
    def __init__(self, data):
        self.data = data
        self.refer = None

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
                element = element.refer
    def add_Val_begin(self, data):
        newnode = Node(data)
        newnode.refer = self.head
        self.head = newnode

    def del_specific_val(self, val):
        element = self.head
        if self.head == None:
            print("The linked list is empty!!!")
            return
        if self.head.data == val:
            self.head = self.head.refer

        else:
            element = self.head
            while element.refer != None:
                if element.refer.data == val:
                    break
                element = element.refer
            element.refer = element.refer.refer

mylist = LinkedList()
mylist.add_Val_begin(50)
mylist.add_Val_begin(40)
mylist.add_Val_begin(30)
mylist.add_Val_begin(20)
mylist.add_Val_begin(10)
mylist.del_specific_val(10)
mylist.print_linked_list()
