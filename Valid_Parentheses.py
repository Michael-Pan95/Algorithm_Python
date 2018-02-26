class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        f = {'(': ')', '[': ']', '{': '}'}
        stack = []
        s = list(s)

        for p in s:
            if p not in f:
                if not stack:
                    return False
                elif p != stack[-1]:
                    return False
                elif p == stack[-1]:
                    stack = stack[:-1]
            else:
                target = f[p]
                stack.append(target)
        if not stack:
            return True
        else:
            return False


a = Solution()
print(a.isValid('([)]'))
