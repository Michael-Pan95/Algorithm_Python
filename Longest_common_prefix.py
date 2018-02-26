class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        result = []
        strs = sorted(strs, key=len)
        least_length = len(strs[0])
        final = ''
        for i in range(least_length):
            temp = [s[i] for s in strs]
            result.append(temp)
        for s in result:
            first = s[0]
            for i in range(1, len(s)):
                if s[i] != s[0]:
                    return final
            final += s[0]
        return final


a = Solution()
print(a.longestCommonPrefix(['abcdefg', 'abert', 'ab']))
