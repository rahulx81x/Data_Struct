class TreeNode:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.children =[]

    def add_child(self, node):
        node.parent = self
        self.children.append(node)

    def ancestors(self):
        count = 0
        i = self
        while i.parent is not None:
            count += 1
            i = i.parent
        return count

    def create_from(self):
        indent = ' ' * self.ancestors() * 3
        print(indent + '-->' + str(self.data))
        for index in self.children:
            index.create_from()

