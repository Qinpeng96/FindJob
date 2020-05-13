'''
给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord 的最短转换序列的长度。转换需遵循如下规则：
每次转换只能改变一个字母。
转换过程中的中间单词必须是字典中的单词。
说明:
如果不存在这样的转换序列，返回 0。
所有单词具有相同的长度。
所有单词只由小写字母组成。
字典中不存在重复的单词。
你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
示例 1:
输入:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]
输出: 5
示例 2:
输入:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
输出: 0
解释: endWord "cog" 不在字典中，所以无法进行转换。 
'''
from typing import List
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str])->int:
        if endWord not in wordList:
            return 0
        value = self._ladderLength(beginWord,endWord,wordList)
        if value:
            return value+1
        else:
            return value
    def _ladderLength(self, beginWord: str, endWord: str, wordList: List[str]):
        res = 0
       # print("++")
        word_len = len(beginWord)
        arr = list(beginWord)  
        while beginWord in wordList:
            wordList.remove(beginWord)

        for i in range(word_len):#从第一个字母开始匹配
            orign = arr[i]  #当前字母开始分支
            for j in range(97,123) :#从'a'开始
                num = 0
                arr[i] = chr(j)
                new_beginword = ''.join(arr)
                if new_beginword ==  endWord:
                    return 1
                else:
                    if new_beginword in wordList:
                        wordList.remove(new_beginword) 
                        num += 1
                        value = self._ladderLength(new_beginword,endWord,wordList)
                        if value != 0:#找到
                            #print(new_beginword)
                            num += value
                            if res == 0:
                                res = num
                                #print("res:%d"%(res))
                            else:
                                res = min(num,res)
                                
            arr[i] = orign
        return res
s = Solution()
#kiss diss disk dusk tusk
#kiss diss miss muss dusk tusk 
print(s.ladderLength("kiss","tusk",["kiss","diss","disk","dusk","tusk","miss","musk","sang","ties","muss"]))
#hot dot dog
print(s.ladderLength("hot","dog",["hot","cog","dog","tot","hog","hop","pot","dot"]))
#a c
print(s.ladderLength("a","c",["a","b","c"]))
#hit hot lot log cog
print(s.ladderLength("hit","cog",["hot","dot","dog","lot","log","cog"]))

