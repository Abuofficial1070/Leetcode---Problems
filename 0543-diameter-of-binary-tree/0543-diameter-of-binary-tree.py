class Solution:

    def __init__(self):
        self.diameter = 0

    def diameterOfBinaryTree(self, root):
        self.height(root)
        return self.diameter

    def height(self, root):

        if root is None:
            return 0

        left = self.height(root.left)
        right = self.height(root.right)

        self.diameter = max(self.diameter, left + right)

        return max(left, right) + 1
