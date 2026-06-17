# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # def findPath(searchNode):
            
        #     path = []
        #     curNode = root
        #     while True:
        #         path.append(curNode)
        #         print(searchNode.val, curNode.val)
        #         if curNode.val == searchNode.val:
        #             break
        #         elif curNode.val > searchNode.val:
        #             curNode = curNode.left
        #         else:
        #             curNode = curNode.right

        #     return path

        # pathP = findPath(p)
        # pathQ = findPath(q)
        # print("2.", len(pathP), len(pathQ))
        # for i in range(len(pathP) - 1, -1, -1):
        #     print("i:", i)
        #     for j in range(len(pathQ) -1, -1, -1):
        #         print("j:", j)
        #         print("1.", pathP[i].val, pathQ[j].val)
        #         if pathP[i].val == pathQ[j].val:
        #             return pathP[i]


        if p.val < q.val: 
            small = p.val
            big = q.val
        else:
            small = q.val
            big = p.val
        node = root
        while node:
            if node.val < small and node.val < big:
                node = node.right
            elif node.val > small and node.val > big:
                node = node.left
            else:
                return node

        


                
                
            

            


        