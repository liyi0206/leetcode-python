class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        self.trie=Trie()
        for w in words: self.trie.insert(w)
        
        self.board=board
        self.n,self.m=len(board),len(board[0])
        self.visited=[[0]*self.m for i in range(self.n)]
        self.res=[]
        
        for i in range(self.n):
            for j in range(self.m):
                self.dfs(i,j,"")
        return self.res
        
    def dfs(self,x,y,tmp):
        if not (0<=x<self.n and 0<=y<self.m) or self.visited[x][y]: return
        tmp+=self.board[x][y]
        if not self.trie.startsWith(tmp): return
        if self.trie.search(tmp): self.res.append(tmp)
        
        self.visited[x][y]=1
        for nx,ny in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
            self.dfs(nx,ny,tmp)
        self.visited[x][y]=0
        
class TrieNode(object):
    def __init__(self):
        self.children = dict()
        self.isWord = False

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children: node.children[c]=TrieNode()
            node=node.children[c]
        node.isWord = True

    def search(self, word):
        node = self.root
        for c in word:
            node = node.children.get(c)
            if not node: return False
        return node.isWord

    def startsWith(self, prefix):
        node = self.root
        for c in prefix:
            node = node.children.get(c)
            if not node: return False
        return True
        
board=[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]
a=Solution()
print a.findWords(board,words)