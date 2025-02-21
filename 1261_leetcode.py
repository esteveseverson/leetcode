class TreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


class FindElements:
    def __init__(self, root: TreeNode):
        self.recovered_values = set()
        self.recover_tree(root, 0)

    def recover_tree(self, node: TreeNode, value: int):
        if node is None:
            return

        node.val = value  # Set the value of the current node
        self.recovered_values.add(value)

        if node.left:
            self.recover_tree(node.left, 2 * value + 1)

        if node.right:
            self.recover_tree(node.right, 2 * value + 2)

    def find(self, target: int) -> bool:
        return target in self.recovered_values


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)  # root is a TreeNode here, not a list
# param_1 = obj.find(target)
