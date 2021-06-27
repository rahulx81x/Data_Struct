class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.start = None
        self.end = None

    def length(self):
        count = 0
        i = self.start
        while i.next is not None:
            count += 1
            i = i.next
        return count+1
        # +1 for no. of nodes

    def at_beginning(self, data):
        node = Node(data, self.start)
        self.start = node
        if node.next is None:
            self.end = node

    def at_end(self, data):

        if self.start is None:
            self.at_beginning(data)
            return
        node = Node(data, None)
        self.end.next = node
        self.end = node

    def op(self):
        op = ''
        i = self.start
        while i is not None:
            op += str(i.data) + ' > '
            i = i.next
        print(op)

    def add_at(self, data, pos):
        if self.start is None:
            self.at_beginning(data)
        node = Node(data)
        count = 0
        i = self.start
        while count != pos-1:
            count += 1
            i = i.next
        node.next = i.next
        i.next = node

    def remove_at(self,  pos):
        count = 0
        i = self.start
        while count != pos-1:
            count += 1
            i = i.next
        i.next = i.next.next
    
    def remove_at_end(self):
        count = 0
        i = self.start
        while count != self.length() - 2:
            # -1 because of array starting at 0 and
            # -1 because we need to end at the second last
            count += 1
            i = i.next
        i.next = self.start
