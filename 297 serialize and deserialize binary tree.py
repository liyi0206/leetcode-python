# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec1: # DFS preorder traversal - similar to 331 Verify Preorder Serialization
              # the serialized string has a few more # on the bottom level, than BST way
              # o(height)~=o(logn) space, o(n) time.
              # but for this question, res needs o(n) space, so not matter
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        def doit(node): # no return, fill vals
            if node:
                vals.append(str(node.val))
                doit(node.left)
                doit(node.right)
            else: vals.append('#')
            
        vals = []
        doit(root)
        return ','.join(vals)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        def doit(): # has return for node
            val = vals.pop(0)
            if val!='#':
                node = TreeNode(int(val))
                node.left = doit()
                node.right= doit()
                return node
            else: return None
            
        vals = data.split(',')
        return doit()

class Codec2: # BFS level order traversal - easier to remember, 
              # need more space for cur and nxt, o(width)~=o(n)
              # but for this question, res needs o(n) space, so not matter
    def serialize(self, root):
        if not root: return "#"
        self.res=[]
        cur=[root]
        while cur:
            nxt=[]
            for node in cur:
                if node is not "#": 
                    self.res.append(str(node.val))
                    if node.left: nxt.append(node.left)
                    else: nxt.append("#")
                    if node.right:nxt.append(node.right)
                    else: nxt.append("#")
                else: self.res.append("#")
            if len(nxt)>len([a for a in nxt if a=="#"]): cur=nxt
            else: break
        return ",".join(self.res)

    def deserialize(self, data):
        if data=="#": return None
        vals=data.split(",")
        root=TreeNode(int(vals.pop(0)))
        cur =[root]
        while vals:
            nxt=[]
            for parent in cur:   # if child is #, don't append to nxt
                                 # thus no grand child will be considered
                val1=vals.pop(0) 
                if val1!="#": # everytime, create node, add to tree, add to nxt
                    node1=TreeNode(int(val1))
                    parent.left=node1
                    nxt.append(node1)
                val2=vals.pop(0)
                if val2!="#": 
                    node2=TreeNode(int(val2))
                    parent.right=node2
                    nxt.append(node2)
            cur=nxt
        return root


root=TreeNode(1)
root.left =TreeNode(2)
root.right=TreeNode(3)
root.right.left =TreeNode(4)
root.right.right=TreeNode(5)

codec = Codec2()
tmp = codec.serialize(root); print tmp
new = codec.deserialize(tmp)
print new.val,new.left.val,new.right.val,
print new.left.left,new.left.right,
print new.right.left.val,new.right.right.val