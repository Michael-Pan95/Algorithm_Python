# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class SortedArrayToHeightBalancedBinarySearchTree:

    def shuffle(self, nums):
        shuffled = []


    def sp_list(self, nums):
        length = len(nums) // 2
        return nums[:length], nums[length:]

    def sortedArrayToHBBST(self, nums):
        if not nums:
            return []

        nums = tmp
        head = TreeNode(nums[0])
        nums = nums[1:]
        for num in nums:
            tmp_node = head
            satisfied = False
            while not satisfied:
                if num >= tmp_node.val:
                    if tmp_node.right:
                        tmp_node = tmp_node.right
                    else:
                        tmp_node.right = TreeNode(num)
                        satisfied = True
                elif num < tmp_node.val:
                    if tmp_node.left:
                        tmp_node = tmp_node.left
                    else:
                        tmp_node.left = TreeNode(num)
                        satisfied = True
                else:
                    print('wtf')
        return head


a = SortedArrayToHeightBalancedBinarySearchTree()
a.sortedArrayToHBBST([-10, -3, 0, 5, 9])
