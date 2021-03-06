# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if preorder is None or len(preorder) == 0:
            return None
        anchor = preorder[0]
        mid = inorder.index(anchor)
        root = TreeNode(anchor)
        left = inorder[:mid]
        right = inorder[mid+1:]
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root

