# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        lHeight, rHeight = 0,0
        tmp=root
        while tmp and tmp.left:
            lHeight+=1
            tmp=tmp.left
        while tmp and tmp.right:
            rHeight+=1
            tmp=tmp.right
        if lHeight == rHeight:
            return 2 ** lHeight
        return self.countNodes(root.left) + self.countNodes(root.right)+1
