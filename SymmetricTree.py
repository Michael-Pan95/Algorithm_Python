from .TreeBuilder import TreeNode

class SymmetricTree:
    @staticmethod
    def treeBuilder(val_list):
        head = TreeNode(val_list[0])
        level = 1
        current_root_list = [head]

        val_list = val_list[1:]
        # This method has some flaw, it needs a list with lots of redundancy
        # while val_list:
        #     tmp = 0
        #     while tmp < 2 ** level:
        #         tmp_list = []
        #         for r_tmp in current_root_list:
        #             r_tmp.left = TreeNode(val_list[tmp])
        #             r_tmp.right = TreeNode(val_list[tmp + 1])
        #             tmp += 2
        #             tmp_list.append(r_tmp.left)
        #             tmp_list.append(r_tmp.right)
        #         current_root_list = tmp_list
        #     val_list = val_list[2 ** level:]
        #     if not val_list:
        #         break
        #     level += 1

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

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        # '''First solution'''
        # if not root:
        #     return True
        # root_list = [root.left, root.right]
        # while True:
        #     tmp = []
        #     for index in range(len(root_list) // 2):
        #         if root_list[index] != root_list[-(index + 1)] and (not root_list[index] or not root_list[-(index + 1)]):
        #             return False
        #         if root_list[index] != root_list[-(index + 1)] and root_list[index].val != root_list[-(index + 1)].val:
        #             return False
        #
        #     for r in root_list:
        #         if not r:
        #             continue
        #         tmp.append(r.left)
        #         tmp.append(r.right)
        #     if len(tmp) == 0:
        #         return True
        #     root_list = tmp

        '''Second Solution'''
        if not root:
            return True
        return self.isSubSymmetric(root.left, root.right)

    def isSubSymmetric(self, left, right):
        if not left and not right:
            return True
        if not left or not right or left.val != right.val:
            return False
        return self.isSubSymmetric(left.left, right.right) and \
               self.isSubSymmetric(left.right, right.left)


root = Solution.treeBuilder([1, 2, None, 3, 4, None, None])

a = Solution()
print(a.isSymmetric(root))
