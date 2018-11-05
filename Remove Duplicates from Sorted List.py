# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        result = head
        last = head.val
        while head.next:
            if head.next.val == head.val:
                head.next = head.next.next
            else:
                last = head.val
                head = head.next
        return result

a = Solution()
print(a.deleteDuplicates())
