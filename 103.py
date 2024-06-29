# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        reverse = 0
        
        res = [[root.val]]
        q = deque([])
        q.append(root)
        
        while q:
            current_level = []
            while q:
                node = q.popleft()
                if not node:
                    continue
                current_level.append(node.left)
                current_level.append(node.right)
            
            reverse ^= 1
            
            values = []
            for node in current_level:
                if not node:
                    continue
                values.append(node.val)
                q.append(node)
            
            if values:
                if reverse:
                    values.reverse()
                res.append(values)

        return res
            
            


