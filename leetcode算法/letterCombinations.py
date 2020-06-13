class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dct = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        output = []
        def backtrack(combination,next_digits):
            if len(next_digits) == 0:
                output.append(combination)

            else:
                for letter in dct.get(next_digits[0]):
                    backtrack(combination+letter,next_digits[1:])
        
        if digits:
            backtrack("",digits)
        return output
                
                
print(Solution().letterCombinations('2367'))