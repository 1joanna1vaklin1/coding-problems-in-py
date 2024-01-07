# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branch_sums(root):
    sums = []
    update_branch_sums(root, 0, sums)
    return sums


def update_branch_sums(node, current_running_sum, sums):
    if node is None:
        return
    current_running_sum = current_running_sum + node.value
    if node.right is None and node.left is None:
        sums.append(current_running_sum)
        return
    update_branch_sums(node.left, current_running_sum, sum)
    update_branch_sums(node.right, current_running_sum, sum)


if __name__ == '__main__':
    branch_sums()

    # {
    #     "tree": {
    #         "nodes": [
    #             {"id": "1", "left": "2", "right": "3", "value": 1},
    #             {"id": "2", "left": "4", "right": "5", "value": 2},
    #             {"id": "3", "left": "6", "right": "7", "value": 3},
    #             {"id": "4", "left": "8", "right": "9", "value": 4},
    #             {"id": "5", "left": "10", "right": null, "value": 5},
    #             {"id": "6", "left": null, "right": null, "value": 6},
    #             {"id": "7", "left": null, "right": null, "value": 7},
    #             {"id": "8", "left": null, "right": null, "value": 8},
    #             {"id": "9", "left": null, "right": null, "value": 9},
    #             {"id": "10", "left": null, "right": null, "value": 10}
    #         ],
    #         "root": "1"
    #     }
    # }