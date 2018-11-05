class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    @staticmethod
    def treeBuilder(val_list):
        head = TreeNode(val_list[0])
        level = 1
        current_root_list = [head]

        val_list = val_list[1:]
        # more general way to generate a tree
        while val_list:
            tmp_list = []
            tmp = 0
            for r_tmp in current_root_list:
                if val_list[tmp]:
                    r_tmp.left = TreeNode(val_list[tmp])
                    tmp_list.append(r_tmp.left)
                if val_list[tmp + 1]:
                    r_tmp.right = TreeNode(val_list[tmp + 1])
                    tmp_list.append(r_tmp.right)
                tmp += 2
            current_root_list = tmp_list
            val_list = val_list[tmp:]
            if not val_list:
                break
            level += 1
        return head

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        node_list = [root]
        depth = 0
        while node_list:
            tmp_list = []
            for node in node_list:
                if node.right:
                    tmp_list.append(node.right)
                if node.left:
                    tmp_list.append(node.left)
                if not node.right and not node.left:
                    return depth + 1
            if tmp_list:
                depth += 1
            node_list = tmp_list
        return depth


root = Solution.treeBuilder([3, 9, 20, None, None, 15, 7])
a = Solution()
print(a.minDepth(root))
