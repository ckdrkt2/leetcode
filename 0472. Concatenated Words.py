class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        d = set(words)

        def dfs(word):
            for i in range(1, len(word)):
                prefix, suffix = word[:i], word[i:]
                if prefix in d and suffix in d: return True
                if prefix in d and dfs(suffix): return True
                if suffix in d and dfs(prefix): return True
            return False

        ans = []
        for word in words:
            if dfs(word): ans.append(word)
        return ans