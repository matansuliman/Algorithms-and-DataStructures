class TreeNode:
    def __init__(self, val:int=None, left:"TreeNode"=None, right:"TreeNode"=None):
        self.val = val
        self.left = left
        self.right = right

class BST:
    def __init__(self, root:"TreeNode"=None):
        self.root = root
    
    """
    searchs for node with val in BST
    has recursive and iterative approach

    time - O(h) where h in the height of the BST
    worst case O(h) = O(n)
    if BST is height balanced then O(h) = O(log n)
    
    return TreeNode or None if do not exsist
    """
    def search(self, val:int, key="recursive"):

        def recursive_search(node: TreeNode, val: int):
            if node == None or node.val == val: return node
            if val < node.val: return recursive_search(node.left, val)
            else: return recursive_search(node.right, val)
        
        def iterative_search(node: TreeNode, val: int):
            while node != None and node.val != val:
                if val < node.val: node = node.left
                else: node = node.right
            return node

        node = self.root
        if key == "recursive": return recursive_search(node, val)
        elif key == "iterative": return iterative_search(node, val)
        else: return "Invalid key"

    def maximum(node:TreeNode):
        while node.right != None: node = node.right
        return node
    
    def minimum(node:TreeNode):
        while node.left != None: node = node.right
        return node
    
    def successor(node:TreeNode):
        pass

    def predecessor(node:TreeNode):
        pass

    
    
    


node1  = TreeNode(val=1)
node2  = TreeNode(val=11)
root = BST(TreeNode(val=10, left=node1, right=node2))
print(root.search(11, "iterative").val)