# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def checkEqual(node1, node2):
            if node1 is None and node2 is not None:
                return False
            
            if node1 is not None and node2 is None:
                return False

            if node1 is None and node2 is None:
                return True

            if node1.val != node2.val:
                return False


            leftCheck = checkEqual(node1.left, node2.left)
            rightCheck = checkEqual(node1.right, node2.right)
            return leftCheck and rightCheck


        def dfs(node):
            if not node:
                return False

            if checkEqual(node, subRoot):
                return True

            left = dfs(node.left)
            right = dfs(node.right)
            return left or right 

        return dfs(root)
        