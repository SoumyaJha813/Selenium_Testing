class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def BuildTree(self,preOrder, inOrder):
        if not inOrder:
            return None
            root = TreeNode(preOrder[0])
            rootPos = inOrder.index(preOrder[0])
            root.left = self.BuildTree(preOrder[1:1+rootPos],inOrder[:rootPos])
            root.right = self.BuildTree(preOrder[rootPos+1:], inOrder[rootPos+1:])
        return root
