# You are climbing a stair case. It takes n steps to reach to the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
import math


class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # length = n
        # iteration_num = n // 2
        # total = 0
        # for i in range(0, iteration_num + 1):
        #     temp_length = length - i
        #     one_num = temp_length - i
        #     total += math.factorial(temp_length)/(math.factorial(one_num)*math.factorial(i))
        # return int(total)

        a = 1
        b = 1
        for _ in range(n-1):
            tmp = a
            a = b
            b += tmp
        return b


a = Solution()
print(a.climbStairs(1024))
