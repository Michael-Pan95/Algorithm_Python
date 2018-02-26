class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        '''Solution 1'''
        # last = None
        # pool = []
        # for i in nums:
        #     if i == last:
        #         pool.append(i)
        #     last = i
        # for i in pool:
        #     nums.remove(i)
        # print(nums)
        # return len(nums)

        '''Solution 2'''
        # length = len(nums)
        # last = None
        # i = 0
        # while i < length:
        #     current_num = nums[i]
        #     if current_num == last:
        #         nums.remove(current_num)
        #         length -= 1
        #         i -= 1
        #     last = current_num
        #     i += 1
        # print(nums)
        # return len(nums)


        '''Solution 3'''
        f_worker = 0
        s_worker = 1
        change = 0

        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1

        while s_worker < len(nums):
            if nums[s_worker] != nums[f_worker]:
                change += 1
                nums[change] = nums[s_worker]
            f_worker += 1
            s_worker += 1
        print(nums)
        return change + 1

a = Solution()
print(a.removeDuplicates([1,1,2,2,2,3,3,3,4,5]))