#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# AUTHOR: Zhenwei Lin
# DATE: 2020/05/31 Sun
# TIME: 14:33:19

# DESCRIPTION:

class Solution(object):
    
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman_digits = []
        digits = [(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),(90,'XC'),
                (50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]
        
        for value, symbol in digits:
            if num == 0:break
            count,num = divmod(num,value)
            roman_digits.append(symbol*count)
        
        return "".join(roman_digits)


print(Solution().intToRoman(329))
