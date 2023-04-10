class Node:
    def __init__(self, data):
        self.data = data
        self.refer = None

class LinkedList:
    def __init__(self):
        self.head = None

    def linked_list_traverse(self):
        if self.head == None:
            print("The linked list is empty!!!")
        else:
            element = self.head
            while element != None:
                print(element.data)
                element = element.refer

mylist = LinkedList()
first = Node(10)
second = Node(20)
mylist.head = first
first.refer = second
mylist.linked_list_traverse()