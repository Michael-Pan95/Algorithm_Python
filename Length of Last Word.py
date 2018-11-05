class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        first_word = 0
        for i in s[::-1]:
            if i == ' ':
                first_word += 1
            else:
                break

        for i in s[len(s) - first_word - 1::-1]:
            if i == ' ':
                return count
            count += 1
        return count

a = Solution()
print(a.lengthOfLastWord('a b cd '))