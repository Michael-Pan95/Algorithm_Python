class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        start_point = 1
        end_point = x
        mid_point = None
        while start_point != end_point:
            temp = (start_point + end_point) // 2
            if temp == mid_point:
                break
            mid_point = temp
            mid_point_sq = mid_point ** 2
            if mid_point_sq == x:
                return mid_point
            elif mid_point_sq > x:
                end_point = mid_point
            else:
                start_point = mid_point
        return start_point


a = Solution()
print(a.mySqrt(10))
