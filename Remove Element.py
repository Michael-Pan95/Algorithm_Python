class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        f_worker = 0
        for i in nums:
            if i != val:
                nums[f_worker] = i
                f_worker += 1
        print(nums)
        return f_worker

a = Solution()
print(a.removeElement([3,2,2,3],3))