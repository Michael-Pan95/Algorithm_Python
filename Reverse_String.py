class Solution:
    # reverse string based on string and number k
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        quotient = int(len(s) / (2 * k))
        remainder = 2 * k - len(s) % k

        result = ''
        for i in range(0, quotient):
            start = i * 2 * k
            end = start + k - 1
            if start == 0:
                result += s[end::-1]
            else:
                result += s[end:start - 1:-1]
            result += s[start + k:end + k + 1]

        if remainder != 0:
            if remainder < k:
                start = quotient * 2 * k
                end = start + remainder - 1
                if start == 0:
                    result += s[end:start - 1:-1]
                else:
                    result += s[end::-1]
            else:
                start = quotient * 2 * k
                end = start + k - 1
                if start == 0:
                    result += s[end::-1]
                else:
                    result += s[end:start - 1:-1]
                result += s[end + 1:]

        return result


a = Solution()
print(a.reverseStr('abcd', 3))
