#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# AUTHOR: Zhenwei Lin
# DATE: 2020/05/28 Thu
# TIME: 09:52:51

# DESCRIPTION:
'''
自己的这种写法应该只能解循环套用的[]
'''

# class Solution(object):
#     def decodeString(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         def get_string(s):
#             index1,index2 = 0,len(s)-1
#             while True:
#                 if s[index1] == '[' and s[index2] == ']':
#                     mul = s[index1-1]
#                     mul_s = s[index1:index2-1]
#                     return int(mul)*get_string(mul_s)

#                 if s[index1] != '[':
#                     index1 += 1
#                 if s[index2] != ']':
#                     index2-=1
#                 if index1 == index2:
#                     return s

#         return get_string(s)

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for c in s:
            if c != ']':
                #push in stack
                stack.append(c)
            else:
                tmp = ''
                while stack[-1] != '[':
                    #from the last string in stack 
                    tmp = stack.pop(-1)+tmp #后来的要放在左边
                stack.pop(-1)#remove [
                times = ''
                while stack and stack[-1].isdigit():
                    times = stack.pop(-1) + times
                times = int(times)
                
                tmp = times*tmp
                stack.append(tmp)
                
        return "".join(stack)

                    
                    
a = Solution()
print(a.decodeString("3[a]2[bc]"))
