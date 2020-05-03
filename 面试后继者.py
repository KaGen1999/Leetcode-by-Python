# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        n = []
        if root == None:
            return None
        def dfs(tree):
            if tree == None:
                return
            if tree != None:
                dfs(tree.left)
                n.append(tree)
                dfs(tree.right)
        dfs(root)

        for i in range(len(n)-1):
            if n[i].val == p.val:
                return n[i+1]
        return None