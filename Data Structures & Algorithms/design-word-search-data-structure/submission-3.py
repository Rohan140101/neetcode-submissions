class TrieNode:
    def __init__(self):
        self.children = dict()
        self.endOfWord = False

    def isChild(self, name):
        return name in self.children.keys()

    def getChild(self, name):
        return self.children[name]

    def addChild(self, name, child: TrieNode):
        self.children[name] = child

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for i in range(len(word)):
            if not node.isChild(word[i]):
                node.addChild(word[i], TrieNode())
            node = node.getChild(word[i])
        node.endOfWord = True

    def search(self, word: str) -> bool:

        def dfs(j, node):
            cur = node
            for i in range(j, len(word)):
                if word[i] == '.':
                    for child, childNode in node.children.items():
                        if dfs(i+1, childNode):
                            return True
                    return False 
                    

                else:
                    if not node.isChild(word[i]):
                        return False
                    else:
                        node = node.children[word[i]]

            return node.endOfWord

        return dfs(0, self.root)

                

                    


