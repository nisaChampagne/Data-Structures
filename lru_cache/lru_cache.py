from doubly_linked_list import DoublyLinkedList
# import collections

#NOTES ON LRU CACHE
# LRU = least recently used

#  A reasonable high performance hash table, check
# The bookkeeping to track the access, easy.

# the get and set operations are both write operation in LRU cache.

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
        self.storage = dict() # quickly grab key from any part of list
        self.order = DoublyLinkedList() # easier to navigate versus SLL

        #OR

        # self.limit = limit
        # self.cache = collections.OrderedDict()

#This implementation is pretty clean as all the order bookkeeping is handled by the OrderDict now
#  For each get and set operation, we first pop the item, then insert back to update its timestamp. 
# The element in the head of sequence is the least-used-item, thus the candidate to expire
#  if the maximum capacity is reached.

# We use two data structures to implement an LRU cache
# ? 1) Queue which is implemented using a doubly linked list. The maximum size of the queue will be equal to the total number of frames available (cache size). The most recently used pages will be near front end and least recently pages will be near the rear end.
# ? 3) A Hash with page number as key and address of the corresponding queue node as value.


    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key in self.storage:
            node = self.storage[key]
            self.order.move_to_end(node)
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
    def set(self, key, value):
        if key in self.storage:
            node = self.storage[key]
            node.value = (key, value)
            self.order.move_to_end(node)
            return
        else:
            if self.size == self.limit:
                del self.storage[self.order.head.value[0]]
                self.order.remove_from_head()
                self.size -= 1
        self.order.add_to_tail((key, value))
        self.storage[key] = self.order.tail
        self.size += 1

        #OR

        # try:
        #     self.cache.pop(key)
        # except KeyError:
        #     if len(self.cache) >= self.limit:
        #         self.cache.popitem(last=False)
        # self.cache[key] = value

