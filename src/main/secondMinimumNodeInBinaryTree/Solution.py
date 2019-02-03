class Solution:
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.traverse(root, root.val, -1)

    def traverse(self, node, fstMin, scnMin):
        if node is not None:
            if node.val != fstMin:
                if node.val < fstMin:
                    scnMin = fstMin
                    fstMin = node.val
                elif scnMin == -1 or node.val < scnMin:
                    scnMin = node.val

            return self.traverse(node.right, fstMin, self.traverse(node.left, fstMin, scnMin))

        return scnMin
