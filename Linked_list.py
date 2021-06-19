class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.start = None

    def length(self):
        count = 0
        i = self.start
        while i.next is not None:
            count += 1
            i = i.next
        return count+1

    def at_beginning(self, data):
        node = Node(data, self.start)
        self.start = node

    def at_end(self, data):
        node = Node(data, None)
        i = self.start
        while i.next is not None:
            i = i.next
        i.next = node

    def op(self):
        op = ''
        i = self.start
        while i is not None:
            op += str(i.data) + ' > '
            i = i.next
        print(op)

    def at(self, data, pos):
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
