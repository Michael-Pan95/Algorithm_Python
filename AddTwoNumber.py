from ListNodeBuilder import ListNode, ListNodeBuilder


class AddTwoNumber:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # method 1
        # result = 0
        # length_l1 = 0
        # length_l2 = 0
        # while l1:
        #     result += l1.val * 10 ** length_l1
        #     l1 = l1.next
        #     length_l1 += 1
        # while l2:
        #     result += l2.val * 10 ** length_l2
        #     l2 = l2.next
        #     length_l2 += 1
        #
        # result_list = list(str(result))[::-1]
        # length_result = len(result_list)
        # head = None
        # lastNode = None
        # for index, value in enumerate(result_list):
        #     tmpNode = ListNode(int(value))
        #     if not head:
        #         head = tmpNode
        #         lastNode = tmpNode
        #     else:
        #         lastNode.next = tmpNode
        #         lastNode = tmpNode
        # return head

        # method 2
        head = None
        lastNode = None
        carrier = 0
        while l1 or l2 or carrier == 1:
            current_sum = carrier
            if l1:
                current_sum += l1.val
                l1 = l1.next
            if l2:
                current_sum += l2.val
                l2 = l2.next
            if current_sum > 9:
                carrier = 1
                current_sum -= 10
            else:
                carrier = 0
            tmpNode = ListNode(current_sum)
            if not head:
                head = lastNode = tmpNode
            else:
                lastNode.next = tmpNode
                lastNode = tmpNode
        return head


list_head1 = ListNodeBuilder.listNodeBuilder([1, 8])
list_head2 = ListNodeBuilder.listNodeBuilder([0])
a = AddTwoNumber().addTwoNumbers(list_head1, list_head2)
