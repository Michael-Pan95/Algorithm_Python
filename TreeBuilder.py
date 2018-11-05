class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class TreeBuilder:
    @staticmethod
    def treeBuilder(nums:list):

        if not nums:
            return []

        head = TreeNode(nums[0])
        level = 1
        current_root_list = [head]

        nums = nums[1:]
        # more general way to generate a tree
        while nums:
            tmp_list = []
            tmp = 0
            for r_tmp in current_root_list:
                if tmp < len(nums):
                    r_tmp.left = TreeNode(nums[tmp])
                    tmp_list.append(r_tmp.left)
                    tmp += 1

                if tmp < len(nums):
                    r_tmp.right = TreeNode(nums[tmp])
                    tmp_list.append(r_tmp.right)
                    tmp += 1

            current_root_list = tmp_list
            nums = nums[tmp:]
            level += 1
        return head


root = TreeBuilder.treeBuilder([-10, -3, 0, 5, 9])
print('')
