# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        now_nodes = [root]
        next_nodes = []
        result = [root.val]
        while True:
            for nd in now_nodes:
                if nd.left != None:
                    next_nodes.append(nd.left)
                if nd.right != None:
                    next_nodes.append(nd.right)
            if next_nodes == []:
                return result
            else:
                result.append(next_nodes[-1].val)
                now_nodes = next_nodes
                next_nodes = []