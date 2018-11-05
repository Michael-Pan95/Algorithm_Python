# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class SortedArrayToHeightBalancedTree:
    def sortedArrayToHBT(self, nums):
        if not nums:
            return []
        head = TreeNode(nums[0])
        up_layer = [head]
        nums = nums[1:]
        layer_num = 0
        while nums:
            up_node_num = 2 ** layer_num
            if len(nums) <= up_node_num:
                for i in range(0, len(nums)):
                    up_layer[i].left = TreeNode(nums[i])
                nums = []
            elif up_node_num < len(nums) <= 2 * up_node_num:
                for i in range(up_node_num):
                    up_layer[i].left = TreeNode(nums[i])
                nums = nums[up_node_num:]
                for i in range(len(nums)):
                    up_layer[i].right = TreeNode(nums[i])
                nums = []
            else:
                for i in range(up_node_num):
                    up_layer[i].left = TreeNode(nums[i])
                nums = nums[up_node_num:]
                for i in range(up_node_num):
                    up_layer[i].right = TreeNode(nums[i])
                nums = nums[up_node_num:]

            tmp = []
            for node in up_layer:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            up_layer = tmp
            layer_num += 1
        return head


a = SortedArrayToHeightBalancedTree()
a.sortedArrayToBST([0, 1, 2, 3, 4, 5])
