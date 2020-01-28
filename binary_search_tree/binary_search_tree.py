import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)

        elif value > self.value:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
    def contains(self, target):
        if target == self.value:
            return True

        elif target < self.value:
            try:
                return self.left.contains(target)
            except:
                return False

        elif target > self.value:
            try:
                return self.right.contains(target)
            except:
                return False
                
    def get_max(self):
        try:
            return self.right.get_max()
        except:
            return self.value
    def for_each(self, cb):
        cb(self.value)

        if self.right is not None:
            self.right.for_each(cb)

        if self.left is not None:
            self.left.for_each(cb)

    def in_order_print(self, node):

        if node.left is not None:
            node.in_order_print(node.left)
        print(node.value)
        

        if node.right is not None:
            node.in_order_print(node.right)

        return node.value

    def bft_print(self, node):
        q = Queue()
        q.enqueue(node)
        while q.size > 0:
            x = q.dequeue()
            print(x.value)

            if x.left is not None:
                q.enqueue(x.left)

            if x.right is not None:
                q.enqueue(x.right)

    def dft_print(self, node):
        stack = Stack()
        stack.push(node)
        while stack.size >0:
            x=stack.pop()
            print(x.value)
            if x.left is not None:
                stack.push(x.left)

            if x.right is not None:
                stack.push(x.right)



    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass