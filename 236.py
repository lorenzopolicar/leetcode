class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def search(node):
            if not node or node == p or node == q:
                return node

            left = search(node.left)
            right = search(node.right)

            if left and right:
                return node
            elif left:
                return left
            elif right:
                return right

        return search(root)

                
