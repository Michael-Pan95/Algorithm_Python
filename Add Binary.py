class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return str(bin(int(a, 2) + int(b, 2))[2:])


a = Solution()
print(a.addBinary('1010', '11001'))
