class Solution:
    
    def numTilePossibilities(self, tiles):
        counter = [0] * 26
        for alpha in tiles:
            counter[ord(alpha) - ord('A')] += 1 #先统计26个字母分别出现的次数
        return self.__dfs(counter)

    def __dfs(self, counter):
        res = 0
        for i in range(26):
            if counter[i] == 0:
                continue
            res += 1#当前点也是一个解
            counter[i] -= 1#子树没有了当前的值

            res += self.__dfs(counter)
            counter[i] += 1#在当前这一层的其他点则count仍然为此，故需要再加回来
        return res