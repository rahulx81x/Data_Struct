# stack using linked list
from Linked_list import *


class Stack(LinkedList):
    def __init__(self):
        self.start = None

    def push(self, data):
        self.at_end(data)

    def pop(self):
        self.remove_at_end()

    def out(self):
        self.op()