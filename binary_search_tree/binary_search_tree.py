import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        ## if inserting, we must already have a tree/root
        #if value < self.value:
            #go left
            #make a new tree or node if empty
            #otherwise keep going ( recursion)

        #if value >=  self.value:
            #go right
            #make a new tree/node
            #otherwise keep going
        if value < self.value:
            if self.left == None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        elif value > self.value:
            if self.right == None:
                self.right = BinarySearchTree(value)
            else: 
                self.right.insert(value)
        elif value == self.value:
            return "Already in tree"

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if target  == self.value, return it
        # go left or right based on smaller or bigger
        if self.value == target:
            return True
        if target > self.value:
            if self.right:
                return self.right.contains(target)
            else:
                return False
        if target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False
        if not self:
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        #if right exists:
            #go right
        #otherwise:
            #return self.value
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        #recursion because sub problems
        if not self:
            return
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = Queue()
        if node:
            queue.enqueue(node.value)
        while node:
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
            queue.dequeue(0)
            if not queue:
                break
            node = queue[0]

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
