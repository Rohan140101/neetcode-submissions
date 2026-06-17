from collections import deque
# Definition for a binary tre node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        queue = deque([(root, 1)])
        maxLevel = 0
        while queue:
            # print(queue.popleft())
            curNode, level = queue.popleft()
            if curNode == None:
                continue
            if level > maxLevel:
                answer.append(curNode.val)
                maxLevel += 1

            if curNode.right:
                queue.append((curNode.right, level+1))
            if curNode.left:
                queue.append((curNode.left, level+1))

        return answer
        
        