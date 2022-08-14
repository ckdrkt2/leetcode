from collections import defaultdict

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList = set(wordList)
        res, layer = [], {}
        layer[beginWord] = [[beginWord]]
        while layer:
            newlayer = defaultdict(list)
            for w in layer:
                if w == endWord:
                    res.extend(k for k in layer[w])
                else:
                    for neww in wordList:
                        if sum([True for i, j in zip(w,neww) if i != j]) == 1:
                            newlayer[neww]+=[j+[neww] for j in layer[w]]
            wordList -= set(newlayer.keys())
            layer = newlayer
        return res