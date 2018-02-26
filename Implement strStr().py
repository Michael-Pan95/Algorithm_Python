class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n_len = len(needle)
        find = 0

        if n_len == 0:
            return 0

        if n_len > len(haystack):
            return -1

        for i, v in enumerate(haystack):
            if i >= n_len - 1 and v == needle[-1]:
                for j in range(n_len - 1):
                    if haystack[i - j - 1] != needle[-j - 2]:
                        break
                    find += 1
                if find == n_len - 1:
                    return i - n_len + 1
                else:
                    find = 0
        return -1


a = Solution()
print(a.strStr('', ''))
