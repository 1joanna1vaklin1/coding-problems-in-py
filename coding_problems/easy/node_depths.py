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

# time 0(n) and space O(h) height of the tree.
# much cleaner approach to the recursive algorithm. + space complexity gets
# reduced from the above algorithm. from 0(n) to o(h)
def nodeDepths_recursive(root, depth=0):
    if root is None:
        return 0
    return depth + nodeDepths(root.left, depth + 1) + nodeDepths(root.right, depth + 1)


if __name__ == '__main__':
    nodeDepths()