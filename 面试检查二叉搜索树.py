# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        n = []
        if root == None:
            return True
        def dfs(tree):
            if tree.left != None:
                dfs(tree.left)
                # n.append(tree.left.val)

            n.append(tree.val)
            if tree.right != None:
                dfs(tree.right)
                # n.append(tree.right.val)

        dfs(root)

        for i in range(len(n)-1):
            if n[i] >= n [i+1]:
                return False
        return True