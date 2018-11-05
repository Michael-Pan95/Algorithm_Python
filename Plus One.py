class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        length = len(digits)

        for i, v in enumerate(digits[::-1]):

            if v == 9:
                if i == length - 1:
                    digits[length - i - 1] = 0
                    digits.insert(0, 1)
                    break
                else:
                    digits[length - i - 1] = 0
                    continue
            digits[length - i - 1] += 1
            break

        return digits


a = Solution()
print(a.plusOne([9, 9]))
