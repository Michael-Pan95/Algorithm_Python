class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, "X": 10, 'V': 5, 'I': 1}
        f_worker = None
        s_worker = None
        result = 0

        if len(s) == 1:
            return num[s]

        for letter in s:
            if f_worker is None:
                f_worker = num[letter]
            elif s_worker is None:
                s_worker = num[letter]
            else:
                f_worker = s_worker
                s_worker = num[letter]

            if f_worker and s_worker:
                if f_worker < s_worker:
                    result -= f_worker
                    f_worker = 0
                else:
                    result += f_worker
                    f_worker = 0

        result += f_worker + s_worker

        return result


a = Solution()
print(a.romanToInt('MMXIV'))
