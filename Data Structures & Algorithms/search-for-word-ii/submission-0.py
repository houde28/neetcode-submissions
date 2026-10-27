class TrieNode():
    def __init__(self):
        self.letters = {}
        self.word = False
    def addWord(self, word):
        cur = self
        for char in word:
            if char not in cur.letters:
                cur.letters[char] = TrieNode()
            cur = cur.letters[char]
        cur.word = True
        


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        used = set()
        trie = TrieNode()
        for word in words:
            trie.addWord(word)
        res = set()

        def helper(x,y, node, word):
            if (x < 0 or y < 0 or x == len(board) or y == len(board[0]) or (x,y) in used or board[x][y] not in node.letters):
                return 
            used.add((x,y))
            node = node.letters[board[x][y]]
            word += board[x][y]
            if node.word:
                res.add(word)        
            helper(x + 1, y, node, word)
            helper(x - 1, y, node, word)
            helper(x, y + 1, node, word)
            helper(x, y - 1, node, word)
            used.remove((x,y))

        for i in range(len(board)):
            for j in range(len(board[0])):
                helper(i,j,trie,"")

        return list(res)


        