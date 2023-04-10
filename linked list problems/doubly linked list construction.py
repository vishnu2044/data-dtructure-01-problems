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


mylist = DoubleLinkedList()
mylist.linked_list_traverse()
print()
mylist.linked_list_reverse()