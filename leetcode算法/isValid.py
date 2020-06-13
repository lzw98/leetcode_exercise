class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dct = {
            ')':'(',
            '}':'{',
            ']':'['
            }
        stack = []
        for i in s:
            if stack and stack[-1] == dct.get(i):
                #注意这里用的是get，如果没有的话也不会报错
                stack.pop()
            else:
                stack.append(i)
        return True if not stack else False

print(Solution().isValid("([)]"))