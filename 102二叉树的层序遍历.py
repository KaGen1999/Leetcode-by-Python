# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        a = [root]
        b = []
        r = [[root.val]]
        while a != []:
            t = a.pop()
            if t.left:
                b.append(t.left)
            if t.right:
                b.append(t.right)
            if a == []:
                if b == []:
                    break
                r.append([i.val for i in b])
                a = b[::-1]
                b = []
        return r