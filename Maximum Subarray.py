class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''Solution 1'''
        # result_matrix = []
        # length = len(nums)
        # for i in range(length):
        #     tmp_sum = 0
        #     tmp_list = []
        #     tmp_sum += nums[i]
        #     tmp_list.append(tmp_sum)
        #     if i != length - 1:
        #         for j in range(i + 1, length):
        #             tmp_sum += nums[j]
        #             tmp_list.append(tmp_sum)
        #     result_matrix.append(max(tmp_list))
        # return max(result_matrix)

        '''Solution 2'''
        max_v = nums[0]
        result = max_v
        for i in nums[1:]:
            max_v = max(i, max_v + i)
            result = max(max_v, result)
        return result


a = Solution()
print(a.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
