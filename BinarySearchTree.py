class TreeNode:
    def __init__(self, key:int, left:'TreeNode'=None, right:'TreeNode'=None):
        self.left = None
        self.right = None
        self.key = key

class BinarySearchTree:
    def __init__(self, root:TreeNode=None):
        self.root = root

    """
    insert the key to the BST
    ignores duplicates

    time - O(h) where h in the height of the BST
    worst case O(h) = O(n)
    if BST is height balanced then O(h) = O(log n)
    
    return None
    """
    def insert(self, key:int, type:str="recursive") -> None:

        def recursive_insert(root:TreeNode, key:int):
            if key < root.key:
                if root.left == None: root.left = TreeNode(key)
                else: recursive_insert(root.left, key)
            elif key > root.key:
                if root.right == None: root.right = TreeNode(key)
                else: recursive_insert(root.right, key)
        

        def iterative_insert(root:TreeNode, key:int):
            parent = None
            node = root
            while node != None:
                parent = node
                if key < node.key: node = node.left
                else: node = node.right
            if parent == None: root = TreeNode(key=key)
            elif key < parent.key: parent.left = TreeNode(key=key)
            else: parent.right = TreeNode(key=key)

        match type:
            case "recursive": 
                if self.root == None: self.root = TreeNode(key)
                return recursive_insert(self.root, key)
            case "iterative": return iterative_insert(self.root, key)
            case _: return "Invalid type"

    

    """
    searchs for node with val in BST
    has recursive and iterative approach

    time - O(h) where h in the height of the BST
    worst case O(h) = O(n)
    if BST is height balanced then O(h) = O(log n)
    
    return TreeNode or None if do not exsist
    """
    def search(self, key:int, type:str="recursive") -> TreeNode:

        def recursive_search(root:TreeNode, key:int):
            if root == None or root.key == key: return root
            if key < root.key: return recursive_search(root.left, key)
            else: return recursive_search(root.right, key)
        
        def iterative_search(node, key: int):
            while node != None and node.key != key:
                if key < node.key: node = node.left
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
    def traverse(self, type:str="inorder") -> list[int]:

        def preorder(self, root:TreeNode, res:list[int]):
            if root != None:
                res.append(root.key)
                self.preorder(root.left, res)
                self.preorder(root.right, res)
            return res

        def inorder(self, root:TreeNode, res:list[int]):
            if root != None:
                self._inorder(root.left, res)
                res.append(root.key)
                self._inorder(root.right, res)
            return res


        def postorder(self, root:TreeNode, res:list[int]):
            if root != None:
                self.postorder(root.left, res)
                self.postorder(root.right, res)
                res.append(root.key)
            return res


        match type:
            case "preorder": return preorder(self.root, [])
            case "inorder": return inorder(self.root, [])
            case "postorder": return postorder(self.root, [])
            case _: return "Invalid type"
    
        return _inorder(self.root, [])

    """
    find min in BST
    time - O(h) where h in the height of the BST
    return min node
    """
    def min_value_node(self, node) -> TreeNode:
        current = node
        while current.left != None: current = current.left
        return current

    """
    find min in BST
    time - O(h) where h in the height of the BST
    return min node
    """
    def max_value_node(self, node) -> TreeNode:
        current = node
        while current.right != None: current = current.right
        return current
    


    def delete(self, key:int, type:str="recursive"):

        def recursive_delete(self, root, key):
            if root == None: return root
            if key < root.key: root.left = recursive_delete(root.left, key)
            elif key > root.key: root.right = recursive_delete(root.right, key)
            else:
                if root.left == None: return root.right
                elif root.right == None: return root.left\
                # has both left and right childs
                temp = self._min_value_node(root.right)
                root.key = temp.key
                root.right = recursive_delete(root.right, temp.key)
            return root

        match type:
            case "recursive": return recursive_delete(self.root, [])
            case "iterative": return iterative_delete(self.root, [])
            case _: return "Invalid type"
    
        self.root = recursive_delete(self.root, key)

    
    

    """
    find successor of key in BST
    time - O(h) where h in the height of the BST
    return successor node
    """
    def successor(self, key:int):
        node = self.search(key)
        if node == None: return None

        # the min node of the right subtree
        if node.right != None: return self.min_value_node(node.right)
        
        # the last ansector from top to bottom that is grater then key
        # always going left
        successor = None
        ancestor = self.root
        while ancestor != node:
            if node.key < ancestor.key:
                successor = ancestor
                ancestor = ancestor.left
            else: ancestor = ancestor.right
        return successor

    """
    find predecessor of key in BST
    time - O(h) where h in the height of the BST
    return predecessor node
    """
    def predecessor(self, key):
        node = self.search(key)
        if node == None: return None

        # the max node of the left subtree
        if node.left: return self.max_value_node(node.left)

        # the last ansector from top to bottom that is smaller then key
        # always going right
        predecessor = None
        ancestor = self.root
        while ancestor != node:
            if node.key > ancestor.key:
                predecessor = ancestor
                ancestor = ancestor.right
            else: ancestor = ancestor.left
        return predecessor