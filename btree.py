class BTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_node(self, data):

        if data == self.data:
            return
        if data < self.data:
            if self.left is not None:
                self.left.add_node(data)
            else:
                self.left = BTree(data)

        if data > self.data:
            if self.right is not None:
                self.right.add_node(data)
            else:
                self.right = BTree(data)

    def out_in(self):
        output = []
        if self.left is not None:
            output += self.left.out_in()

        output.append(self.data)

        if self.right is not None:
            output += self.right.out_in()

        return output

    def out_pre(self):
        output = []
        output.append(self.data)
        if self.left is not None:
            output += self.left.out_pre()

        if self.right is not None:
            output += self.right.out_pre()

        return output

    def out_post(self):
        output = []

        if self.left is not None:
            output += self.left.out_post()

        if self.right is not None:
            output += self.right.out_post()

        output.append(self.data)

        return output
