class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = dict()
        self.isWord = False

class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root=TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node=self.root
        for c in word:
            if c not in node.children: node.children[c]=TrieNode()
            node=node.children[c]
        node.isWord=True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.find(self.root,word)
        
    def find(self,node,word):
        if word=='': return node.isWord #the actual false/true
        if word[0]=='.':
            for x in node.children:
                if self.find(node.children[x],word[1:]): 
                    return True #summary true
            return False #summary false
        else:
            child = node.children.get(word[0])
            if not child: return False #the actual false
            else: return self.find(child,word[1:]) #summary true/false

# Your WordDictionary object will be instantiated and called as such:
wordDictionary = WordDictionary()
wordDictionary.addWord("bad")
wordDictionary.addWord("dad")
wordDictionary.addWord("mad")
wordDictionary.search("pad") #false
wordDictionary.search("bad") #true
wordDictionary.search(".ad") #true
wordDictionary.search("b..") #true
