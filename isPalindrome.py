class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # if we accept negative as an eligible answer then uncomment the next line and comment the line 9-10
        # x = abs(x)
        if x < 0:
            return False

        length = len(str(x))
        last_left = 0
        last_right = 0
        for i in range(1, int(length / 2) + 1):
            left = int(x / (10 ** (length - i))) - last_left
            right = int((x % (10 ** i) - last_right) / 10 ** (i - 1))
            if left != right:
                return False
            last_left = (last_left + left) * 10
            if i != 1:
                last_right = last_right + right * 10
        return True


a = Solution()
print(a.isPalindrome(2222222))
