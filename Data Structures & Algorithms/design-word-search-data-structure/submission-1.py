class Node:
    def __init__(self):
        self.letters = {}
        self.endOfWord = False

class WordDictionary:
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root

        for char in word:
            if char not in cur.letters:
                node = Node()
                cur.letters[char] = node
            cur = cur.letters[char]
        cur.endOfWord = True
        
    def search(self, word: str) -> bool:
        def helper(node,index):
            if index == len(word):
                return node.endOfWord
            
            if word[index] != ".":
                if word[index] not in node.letters:
                    return False
                
                return helper(node.letters[word[index]], index +1)

            for char in node.letters:
                if helper(node.letters[char], index+1):
                    return True

            return False
            
        return helper(self.root,0)
        
