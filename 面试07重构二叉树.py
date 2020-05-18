# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recur(self,pre_root,in_left,in_right):
        if in_left > in_right:
            return
        root = TreeNode(self.po[pre_root])
        i = self.dic[self.po[pre_root]]
        root.left = self.recur(pre_root+1,in_left,i-1)
        root.right = self.recur(i-in_left+pre_root+1,i+1,in_right)
        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        self.dic = {}
        self.po = preorder
        for i in range(len(inorder)):
            self.dic[inorder[i]] = i
        return self.recur(0,0,len(preorder)-1)