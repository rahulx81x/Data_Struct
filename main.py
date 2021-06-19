import Linked_list
from Linked_list import *
phones = LinkedList()
phones.at_beginning('xiaomi')
phones.at_end('samsung')
phones.at_end('vivo')
phones.at_beginning('apple')

phones.at('1+', 2)
phones.remove_at(3)
phones.op()
print(phones.length())