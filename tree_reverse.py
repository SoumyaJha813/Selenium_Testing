from collections import deque
from queue import Queue


class BinaryTree:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def levelOrderTraversal(self, root):
        q = deque()
        stack = []
        if not root:
            return
        q.append(root)
        
        while q:
            node = q.popleft()
            stack.append(node)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        while stack:
            print(stack.pop().val)

if __name__ == '__main__':
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.right = BinaryTree(3)
    root.left.left = BinaryTree(4)
    root.left.right = BinaryTree(5)
    root.right.left = BinaryTree(6)
    root.right.right = BinaryTree(7)
    print("Reverse order of Tree: ")
    root.levelOrderTraversal(root)


