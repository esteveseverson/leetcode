class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    # Insert Node
    def insert(self, data):
        if self.data:
            if data < self.data:
                if not self.left:
                    self.left = TreeNode(data)

                if self.left:
                    self.left.insert(data)

            if data > self.data:
                if not self.right:
                    self.right = TreeNode(data)
                
                if self.right:
                    self.right.insert(data)

        if not self.data:
            self.data = data

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        
        print(self.data)

        if self.right:
            self.right.print_tree()

    def in_order_transversal(self, root):
        res = []

        if root:
            res = self.in_order_transversal(root.left)
            res.append(root.data)
            res = res + self.in_order_transversal(root.right)

        return res