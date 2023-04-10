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

    def add_val_end(self, data):
        newnode =Node(data)
        if self.head == None:
            self.head = newnode
        else:
            element = self.head
            while element.refer != None:
                element = element.refer
            element.refer = newnode

    def list_to_linked_list(self):
        lst = [1, 2, 3, 4, 5]
        for i in lst:
            mylist.add_val_end(i)

mylist = LinkedList()
mylist.list_to_linked_list()
mylist.print_linked_list()