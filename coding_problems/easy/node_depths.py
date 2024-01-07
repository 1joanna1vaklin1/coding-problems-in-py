#My own solution
def nodeDepths(root):
    sums = []
    get_node_depth(root, -1, sums)
    return sum(sums)


def get_node_depth(node, current_depth, sums):
    if node is None:
        return
    current_depth = current_depth + 1
    sums.append(current_depth)
    if node.right is None and node.left is None:
        return
    get_node_depth(node.left, current_depth, sums)
    get_node_depth(node.right, current_depth, sums)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


if __name__ == '__main__':
    nodeDepths()