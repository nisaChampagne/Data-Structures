from doubly_linked_list import DoublyLinkedList
# import collections


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):

        self.limit = limit
        self.size = 0
        # dict() order can change so combo with DLL helps with that
        self.storage = dict() # quickly grab key from any part of list
        self.order = DoublyLinkedList() # easier to navigate versus SLL

        #OR

        # self.limit = limit
        # self.cache = collections.OrderedDict()
        # ^
        # |
        #This implementation is pretty clean as all the order bookkeeping is handled by the OrderDict now
        #  For each get and set operation, we first pop the item, then insert back to update its timestamp. 
        # The element in the head of sequence is the least-used-item, thus the candidate to expire
        #  if the maximum capacity is reached.



    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        #referencing a value
        if key in self.storage:
            node = self.storage[key]
            self.order.move_to_front(node)
            #node.value[0] is the key, so [1] would be the value
            return node.value[1]
        else:
            return None

        #OR

        # try:
        #     value = self.cache.pop(key)
        #     self.cache[key] = value
        #     return value
        # except KeyError:
        #     return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    #set first so we have something to get
    def set(self, key, value):
        # need to access the key to remove it later
        if key in self.storage:
            node = self.storage[key]
            node.value = (key, value)
            self.order.move_to_front(node)
            return
        else:
            if self.size == self.limit:
                #shouldnt be greater than capacity
                del self.storage[self.order.tail.value[0]]
                self.order.remove_from_tail() #LRU
                self.size -= 1

        #defining head as most recent and tail as oldest
        self.order.add_to_head((key, value)) #node becomes MRU
        self.storage[key] = self.order.head #the node
        self.size += 1

        #OR

        # try:
        #     self.cache.pop(key)
        # except KeyError:
        #     if len(self.cache) >= self.limit:
        #         self.cache.popitem(last=False)
        # self.cache[key] = value

list1 = LRUCache()

list1.set("item1", "12")
list1.set("item2", "11")
list1.set("item3", "10")
list1.get("item1")
print(list1.get("item1"))
print(list1.get("item2"))