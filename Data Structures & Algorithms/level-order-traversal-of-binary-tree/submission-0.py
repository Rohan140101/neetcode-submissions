# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        cur_level = -1
        answer = []
        queue = [[root, 0]]
        while queue:
            cur_node = queue.pop(0)
            node = cur_node[0]
            if not node:
                continue
            node_val = node.val
            node_level = cur_node[1]

            if cur_level != node_level:
                cur_level = node_level
                answer.append([])

            answer[cur_level].append(node_val)
            if node.left:
                queue.append([node.left, cur_level+1])
            if node.right:
                queue.append([node.right, cur_level+1])

        return answer
            

        
        