class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        last_result = None
        for i in range(n):
            if i == 0:
                last_result = '1'
            else:
                last_result = self.__say(last_result)
        return last_result

    def __say(self, n):
        count = 0
        result = ''
        last = None
        for i in n:
            if i != last and last:
                result += str(count) + str(last)
                count = 1
                last = i
            else:
                count += 1
                last = i
        if count != 0:
            result += str(count) + str(last)
        return result

a = Solution()
print(a.countAndSay(5))
