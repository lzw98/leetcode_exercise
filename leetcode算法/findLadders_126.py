#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# AUTHOR: Zhenwei Lin
# DATE: 2020/06/07 Sun
# TIME: 17:08:07

# DESCRIPTION:
from collections import defaultdict
from collections import deque

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        wordList.append(beginWord)
        ### 构建具有邻接关系的桶,这个比较有意思
        buckets = defaultdict(list)#这样默认里面的每个元素为列表
        for word in wordList:
            for i in range(len(beginWord)):
                match = word[:i] + '_' + word[i+1:]
                buckets[match].append(word)
                
        ##### BFS遍历
        preWords = defaultdict(list)#前溯词列表
        toSeen = deque([(beginWord, 1)])#待遍历词及深度列表
        beFound = {beginWord:1}#已探测词词列表
        while toSeen:
            curWord, level = toSeen.popleft()
            for i in range(len(beginWord)):
                match = curWord[:i] + '_' + curWord[i+1:]
                for word in buckets[match]:
                    if word not in beFound:
                        beFound[word] = level + 1
                        toSeen.append((word, level+1))
                    if beFound[word] == level+1:#当前深度等于该词首次遍历深度，则仍应加入前溯词列表
                        preWords[word].append(curWord)
            if endWord in beFound and level+1 > beFound[endWord]:#已搜索到目标词，且完成当前层遍历
                break
        #### 列表推导式输出结果
        if endWord in beFound:
            res = [[endWord]]
            while res[0][0] != beginWord:
                res = [[word] + r for r in res for word in preWords[r[0]]] 
            return res
        else:
            return []

print(Solution().findLadders("hit","cog",["hot","dot","dog","lot","log","cog"]))
