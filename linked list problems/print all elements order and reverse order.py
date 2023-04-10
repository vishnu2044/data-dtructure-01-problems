class Node:
    def __init__(self, data):
        self.data = data
        self.refer = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def linked_list_traverse(self):
        if self.head == None:
            print("The doubly linked list is empty!!")
        else:
            element = self.head
            while element != None:
                print(element.data, end=" ")
                element = element.refer

    def linked_list_reverse(self):
        if self.head == None:
            print("The doubly linked list is empty!!")
        else:
            element = self.head
            while element.refer != None:
                element = element.refer
            while element != None:
                print(element.data, end=" ")
                element = element.prev

    def add_val_end(self, data):
        newnode = Node(data)
        if self.head == None:
            self.head = newnode
        else:
            element = self.head
            while element.refer != None:
                element = element.refer
            element.refer = newnode
            newnode.prev = element



mylist = DoubleLinkedList()
mylist.add_val_end(10)
mylist.add_val_end(20)
mylist.add_val_end(30)
mylist.linked_list_traverse()
print()
mylist.linked_list_reverse()