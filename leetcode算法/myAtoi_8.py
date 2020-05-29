# #!/usr/bin/env python
# # -*- coding:UTF-8 -*-
# # AUTHOR: Zhenwei Lin
# # DATE: 2020/05/29 Fri
# # TIME: 23:19:46

# # DESCRIPTION:

# INT_MAX = 2**32 - 1
# INT_MIN = -2**32

# class Automaton(object):
#     def __init__(self):
#         self.state = 'start'
#         self.sign = 1
#         self.ans = 0
#         self.table = {
#             'start':['start','signed','in_number','end'],
#             'signed':['end','end','in_number','end'],
#             'in_number':['end','end','in_number','end'],
#             'end':['end','end','end','end'],
#         }
#     def get_col(self,c):
#         if c.isspace():
#             return 0
#         if c == '+' or c == '-':
#             return 1
#         if c.isdigit():
#             return 2
#         else:
#             return 3
        
#     def get(self,c):
#         #这句表示的是从上一个状态到下一个状态
#         self.state = self.table[self.state][self.get_col(c)]
#         if self.state == 'in_number':
#             self.ans = 10*self.ans + int(c)
#             self.ans = min(self.ans,INT_MAX) if self.sign == 1 else max(self.ans,INT_MIN)
#         elif self.state == 'signed':
#             self.sign = 1 if c=='+' else -1
            

# class Solution:
#     def myAtoi(self, str):
#         automaton = Automaton()
#         for c in str:
#             automaton.get(c)
#         return automaton.sign * automaton.ans
            


import base64
f=open('C:\\Users\\lzw\\Desktop\\Snipaste_2020-05-29_23-35-19.png','rb') #二进制方式打开图文件
ls_f=base64.b64encode(f.read()) #读取文件内容，转换为base64编码
f.close()
print(ls_f)