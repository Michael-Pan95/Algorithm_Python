from TreeBuilder import TreeBuilder, TreeNode


class PathSum:
    # method 1
    # def hasPathSum(self, root: TreeNode, sum: int):
    #     if root is None:
    #         return False
    #     else:
    #         print(str(self.hasPathCumulateSum(root, sum, 0)))
    #         return
    #
    # def hasPathCumulateSum(self, node: TreeNode, targetSum: int, currentSum: int):
    #     if node.left is None and node.right is None:
    #         if currentSum + node.val == targetSum:
    #             return True
    #         else:
    #             return False
    #
    #     result = False
    #     if node.left is not None:
    #         result = result or self.hasPathCumulateSum(node=node.left, targetSum=targetSum,
    #                                                    currentSum=currentSum + node.val)
    #         if result:
    #             return result
    #     if node.right is not None:
    #         result = result or self.hasPathCumulateSum(node=node.right, targetSum=targetSum,
    #                                                    currentSum=currentSum + node.val)
    #         if result:
    #             return result
    #     return result

    # method 2
    def hasPathSum(self, root: TreeNode, sum: int):
        if not root:
            return None

        if not root.left and not root.right:
            if root.val == sum:
                return True
            else:
                return False
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)


tree = TreeBuilder.treeBuilder([-10, -3, 0, 5, 9])
a = PathSum()
a.hasPathSum(tree, -11)
