class TrieNode:
    def __init__(self):
        self.children: dict = {}
        self.end: bool = False
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word) -> None:
        node = self.root
        for w in word:
            node = node.children.setdefault(w, TrieNode())
        node.end = True

    def search(self, word) -> bool:
        return self.dfs(self.root, word)

    def dfs(self, node, word) -> bool:
        if not word: return node.end
        if word[0] == ".":
            for child in node.children:
                if self.dfs(node.children[child], word[1:]): return True
        if word[0] in node.children:
            return self.dfs(node.children[word[0]], word[1:])
        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)