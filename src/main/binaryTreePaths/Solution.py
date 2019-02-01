# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def findPath(self, node, path, res=None):
        if not node:
            path.add(node.val)

            if not node.left and not node.right:
                res.add(path)
            else:
                self.findPath(node.left, path, res)
                self.findPath(node.left, path, res)

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []

        if root is not None:
            self.findPath(root, [], res)

        for path in res:
            "->".join(path)

        return res


