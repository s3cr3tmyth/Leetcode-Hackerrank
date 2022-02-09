preorder: [1, 2, 4, 5, 3, 6]
inorder: [4, 2, 5, 1, 6, 3]

# The obvious way to build the tree is:
# Use the first element of preorder, the 1, as root.
# Search it in inorder.
# Split inorder by it, here into [4, 2, 5] and [6, 3].
# Split the rest of preorder into two parts as large as the inorder parts, here into [2, 4, 5] and [3, 6].
# Use preorder = [2, 4, 5] and inorder = [4, 2, 5] to add the left subtree.
# Use preorder =[3, 6]andinorder = [6, 3] to add the right subtree.

class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        
        rootValue = preorder[0]
        root = TreeNode(rootValue)
        inorderIndex = inorder.index(rootValue)

        root.left = self.buildTree(preorder[1:inorderIndex+1], inorder[:inorderIndex])
        root.right = self.buildTree(preorder[inorderIndex+1:], inorder[inorderIndex+1:])
        
        return root

