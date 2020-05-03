class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def dfs(tree, l, r):
            if tree.left != None:
                t = r
                l, r, f = dfs(tree.left, l, r)
                if f == True:
                    return 0, 0, True
                l = max(l, r) + 1
                r = t
            else:
                l = 0
            if tree.right != None:
                t = l
                l, r, f = dfs(tree.right, l, r)
                if f == True:
                    return 0, 0, True
                r = max(l, r) + 1
                l = t
            else:
                r = 0

            return l, r, abs(l - r) > 1

        if root == None:
            return True
        l, r, f = dfs(root, 0, 0)
        return not f