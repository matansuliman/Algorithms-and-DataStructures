class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinarySearchTree:
    def __init__(self, root:TreeNode=None):
        self.root = root

    def insert(self, key:int):

        def _insert(root:TreeNode, key:int):
            if key < root.val:
                if root.left is None: root.left = TreeNode(key)
                else: self._insert(root.left, key)
            elif key > root.val:
                if root.right is None: root.right = TreeNode(key)
                else: self._insert(root.right, key)

        if self.root is None: self.root = TreeNode(key)
        else: _insert(self.root, key)

    

    """
    searchs for node with val in BST
    has recursive and iterative approach

    time - O(h) where h in the height of the BST
    worst case O(h) = O(n)
    if BST is height balanced then O(h) = O(log n)
    
    return TreeNode or None if do not exsist
    """
    def search(self, key:int, type:str="recursive"):

        def recursive_search(root:TreeNode, key: int):
            if root == None or root.val == key: return root
            if key < root.val: return recursive_search(root.left, key)
            else: return recursive_search(root.right, key)
        
        def iterative_search(node, val: int):
            while node != None and node.val != val:
                if val < node.val: node = node.left
                else: node = node.right
            return node
        
        match type:
            case "recursive": return recursive_search(self.root, key)
            case "iterative": return iterative_search(self.root, key)
            case _: return "Invalid type"

    """
    traverse the tree values
    has pre/in/post orders approachs

    time - O(n) where n in the number of nodes in the BST
    
    return arr
    """
    def traverse(self, type:str="inorder"):

        def preorder(self, root:TreeNode, res:list[int]):
            if root != None:
                res.append(root.val)
                self.preorder(root.left, res)
                self.preorder(root.right, res)
            return res

        def inorder(self, root:TreeNode, res:list[int]):
            if root != None:
                self._inorder(root.left, res)
                res.append(root.val)
                self._inorder(root.right, res)
            return res


        def postorder(self, root:TreeNode, res:list[int]):
            if root != None:
                self.postorder(root.left, res)
                self.postorder(root.right, res)
                res.append(root.val)
            return res


        match type:
            case "preorder": return preorder(self.root, [])
            case "inorder": return inorder(self.root, [])
            case "postorder": return postorder(self.root, [])
            case _: return "Invalid type"
    
        return _inorder(self.root, [])

    
    
    def delete(self, key:int):

        def _delete(self, root, key):
            if root is None: return root
            if key < root.val: root.left = _delete(root.left, key)
            elif key > root.val: root.right = _delete(root.right, key)
            else:
                if root.left is None: return root.right
                elif root.right is None: return root.left
                temp = self._min_value_node(root.right)
                root.val = temp.val
                root.right = _delete(root.right, temp.val)
            return root
    
        self.root = _delete(self.root, key)

    
    """
    find min in BST
    time - O(h) where h in the height of the BST
    return min node
    """
    def min_value_node(self, node):
        current = node
        while current.left != None:
            current = current.left
        return current

    """
    find min in BST
    time - O(h) where h in the height of the BST
    return min node
    """
    def max_value_node(self, node):
        current = node
        while current.right is not None:
            current = current.right
        return current

    # Find successor
    def successor(self, key):
        node = self.search(key)
        if node is None: return None
        if node.right: return self.min_value_node(node.right)
        else:
            successor = None
            ancestor = self.root
            while ancestor != node:
                if node.val < ancestor.val:
                    successor = ancestor
                    ancestor = ancestor.left
                else: ancestor = ancestor.right
            return successor

    # Find predecessor
    def predecessor(self, key):
        node = self.search(key)
        if node is None: return None
        if node.left: return self.max_value_node(node.left)
        else:
            predecessor = None
            ancestor = self.root
            while ancestor != node:
                if node.val > ancestor.val:
                    predecessor = ancestor
                    ancestor = ancestor.right
                else: ancestor = ancestor.left
            return predecessor