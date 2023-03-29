class Solution(object): 
    def isValidBST(self, root):
        minVal, maxVal = -2**31-1, 2**31
        return self.checkBST(root, minVal, maxVal)
    
    def checkBST(self, node, minVal, maxVal):
        if node==None:
            return True
        elif minVal<node.val<maxVal:
            return self.checkBST(node.left, minVal, node.val) and self.checkBST(node.right, node.val, maxVal)
        else:
            return False