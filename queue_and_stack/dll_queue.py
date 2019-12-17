import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    #LILO 
        #the last item in a queue is the last item
        # to leave the queue
    #FIFO
        # first item in line will be the first out
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        #have to add to tail in queue
        self.size += 1

    def dequeue(self):
        #REMOVE
        if self.len() > 0:
            value = self.storage.remove_from_head()
            self.size -= 1
            return value
        else:
            return None

    def len(self):
        return self.size




'''
[enqueue adding 1]->   [2][3][4]   <-[dequeue removing]

'''
