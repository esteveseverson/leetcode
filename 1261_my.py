'''
by the given examples i think the input for the class is a list of integers
'''

from typing import List

class TreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


class FindElements:
    def __init__(self, root: List[TreeNode]):
        self.nodes = self.build_tree(root)
        self.recovered_values = set()
        self.recover_tree(self.nodes, 0)
        self.root = self.nodes

    def build_tree(self, nodes):
        if not nodes:
            return None
        
        root = TreeNode(nodes[0])
        queue = [root]
        i = 1

        while queue and i < len(nodes):
            current = queue.pop(0)

            if nodes[i]:
                current.left = TreeNode(nodes[i])
                queue.append(current.left)
            i += 1

            if i < len(nodes) and nodes[i]:
                current.right = TreeNode(nodes[i])
                queue.append(current.right)
            i += 1

        return root
    
    def recover_tree(self, node: TreeNode, value: int):
        if node is None:
            return
        
        node.val = value
        self.recovered_values.add(value)

        if node.left:
            self.recover_tree(node.left, 2 * value + 1)
        
        if node.right:
            self.recover_tree(node.right, 2 * value + 2)

    def find(self, target: int) -> bool:
        return target in self.recovered_values
    

root = FindElements([-1,-1,-1,-1,-1])

print(root.find(1))
print(root.find(3))
print(root.find(5))