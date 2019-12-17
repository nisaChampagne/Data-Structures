import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    #FILO
        #The first  object in a stack is the last object to leave
    #LIFO
        # LAST IN FIRST OUT- LAST TO BE ADDED, FIRST REMOVED
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()

    def push(self, value):
        #adds an element to the top of the stack
        self.storage.add_to_head(value)
        ##have to add to head with stack
        self.size += 1

    def pop(self):
        #removes an element at the top of a stack
        if self.len() > 0:
            value = self.storage.remove_from_head()
            self.size -= 1
            return value
        else:
            return None

    def len(self):
        return self.size


'''
pop (remove from head)[6] <- [] <-  [6] push (add to head)

                             [5]
                             [4]
                             [3]
                             [2]
                             [1]
'''