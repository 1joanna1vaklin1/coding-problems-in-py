def find_closest_value_in_bst(tree, target):
    closest_value_curr = float('inf')
    return find_closest_value_helper(tree, target, closest_value_curr)


def find_closest_value_helper(tree, target, closest_value):
    if tree is None:
        return closest_value
    else:
        # if we found a smaller difference on the current value we are at, then we set the closest
        # to the value
        if abs(target - closest_value) > abs(target - tree.value):
            closest_value = tree.value
        if target > tree.value:
            return find_closest_value_helper(tree.right, target, closest_value)
        elif target < tree.value:
            return find_closest_value_helper(tree.left, target, closest_value)
        else:
            return closest_value


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

if __name__ == '__main__':
    find_closest_value_in_bst()
