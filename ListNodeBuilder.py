class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class ListNodeBuilder:
    @staticmethod
    def listNodeBuilder(nums: list):
        if not list:
            return False
        head = None
        lastNode: ListNode = None
        length_of_nums = len(nums)
        for i in range(length_of_nums):
            tmpNode = ListNode(nums[i])

            if i == 0:
                head = tmpNode
                lastNode = tmpNode
            else:
                lastNode.next = tmpNode
                lastNode = lastNode.next
        return head
