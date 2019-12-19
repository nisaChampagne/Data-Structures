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
        # not needed but up to  to preference
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
        #not needed to pass tests
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
        # recursion calls a stack
        #not needed, interesting
        if not self:
            return
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    #iterative solution DFT:
        stack = Stack()
        stack.push(self)

        while stack.len() > 0:
            current = stack.pop()
            if current.left:
                stack.push(current.left)
            if current.right:
                stack.push(current.right)
            cb(current.value)


    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if not node:
            return
        self.in_order_print(node.left)
        print(node.value)
        self.in_order_print(node.right)
    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        #FIFO OR LILO
        #go by layer
        '''
        STEPS
        MAKE QUEUE
        PUT ROOT IN QUEUE
        WHILE  queue is not empty
            pop out front of queue
            cb print node.value
            if left:
                add left to back of queue
            if right:
                add right to back of queue
        '''
        queue = Queue()
        queue.enqueue(node)
        while  queue.len() > 0:
            node = queue.dequeue()
            print(node.value)
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        '''
        #STEPS
        make a stack
        put root in stack
        pop root out of stack
        while stack not empty
            pop root out of stack
            print(node.value)
            if left
                add left to stack
            if right:
                add right to stack
        '''
        #FILO OR LIFO
        stack = Stack()
        stack.push(node)
        while  stack.len() > 0:
            node = stack.pop()
            print(node.value)
            if node.left:
                stack.push(node.left)
            if node.right:
                stack.push(node.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        # pass
        if self.value:
            print(self.value)
            if self.left:
                self.left.pre_order_dft(self.left)
            if self.right:
                self.right.pre_order_dft(self.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        # pass
        if self.value:
            if self.left:
                self.left.post_order_dft(self.left)
            if self.right:
                self.right.post_order_dft(self.right)
            print(self.value)