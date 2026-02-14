# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def calcHeight(self, root: Optional[TreeNode], isLeft: boolean) -> int:
        h=0
        if isLeft:
            while root and root.left:
                h+=1
                root=root.left
        else:
            while root and root.right:
                h+=1
                root=root.right
        return h
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        lHeight = self.calcHeight(root,True)
        rHeight = self.calcHeight(root,False)
        tmp=root
        
        return self.countNodes(root.left) + self.countNodes(root.right)+1
