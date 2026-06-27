# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':



        lca = None

        def dfs(node):
            nonlocal lca
            if node == None:
                return False

            if lca:
                return False


            left = dfs(node.left)
            right = dfs(node.right)
            selfBool = False
            if node.val == p.val or node.val == q.val:
                selfBool = True

            trues = 0
            if left:
                trues += 1

            if right:
                trues += 1

            if selfBool:
                trues += 1

            if trues >= 2:
                lca = node

            return left or right or selfBool

        dfs(root)
        return lca     
