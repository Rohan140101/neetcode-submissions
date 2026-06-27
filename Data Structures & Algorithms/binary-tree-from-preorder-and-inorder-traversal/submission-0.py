# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        
        def dfs(preorder, inorder):
            if not preorder:
                return None

            nodeVal = preorder[0]
            node = TreeNode(val=preorder[0])
            indexInorder = inorder.index(nodeVal)
            node.left = dfs(preorder[1:indexInorder + 1], inorder[:indexInorder])
            node.right = dfs(preorder[indexInorder+1:], inorder[indexInorder+1:])
            return node

        return dfs(preorder, inorder)
        