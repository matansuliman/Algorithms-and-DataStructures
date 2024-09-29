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
        
        def iterative_search(node:TreeNode, key: int):
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

        def preorder(root:TreeNode, res:list[int]):
            if root != None:
                res.append(root.key)
                preorder(root.left, res)
                preorder(root.right, res)
            return res

        def inorder(root:TreeNode, res:list[int]):
            if root != None:
                inorder(root.left, res)
                res.append(root.key)
                inorder(root.right, res)
            return res

        def postorder(root:TreeNode, res:list[int]):
            if root != None:
                postorder(root.left, res)
                postorder(root.right, res)
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
    def min_value_node(self, node:TreeNode) -> TreeNode:
        current = node
        while current.left != None: current = current.left
        return current


    """
    find min in BST
    time - O(h) where h in the height of the BST
    return min node
    """
    def max_value_node(self, node:TreeNode) -> TreeNode:
        current = node
        while current.right != None: current = current.right
        return current
    

        """
    find successor of key in BST
    time - O(h) where h in the height of the BST
    if there is no successor return None
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
    if there is no predecessor return None
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
    

    """
    
    
    """
    def delete(self, key:int, type:str="recursive"):

        def recursive_delete(root, key):
            # base case
            if root == None: return root
            # search in subtrees and update the left or right node
            if key < root.key: root.left = recursive_delete(root.left, key)
            elif key > root.key: root.right = recursive_delete(root.right, key)
            else:
                # root.key == key => key found
                # has only right child
                if root.left == None: return root.right
                # has only left child
                elif root.right == None: return root.left
                # has both left and right childs
                # find succesor
                root_successor = self.successor(key)
                # place succesor instead of root
                root.key = root_successor.key
                # delete the succesor in the right subtree
                root.right = recursive_delete(root.right, root_successor.key)
            return root
        
        def iterative_delete(root, key):
            # find the node and his parent
            node = self.root
            parent = None
            while node != None and node.key != key:
                parent = node
                if key < node.key: node = node.left
                else: node = node.right
            # if key not found
            if node == None: return None
            # node != None
            # node has at most 1 child
            if node.left == None or node.right == None:
                if node.left != None: new_node = node.left
                else: new_node = node.right
                # if the node to be deleted is the root
                if parent == None: return new_node
                # check what type of son (left/right) is node
                # and set the child of the parent to his grandchild
                if node == parent.left: parent.left = new_node
                else: parent.right = new_node
            # node has 2 children
            else:
                # find node successor and successor parent
                parent_successor = None
                successor = node.right
                while successor.left != None: 
                    parent_successor = successor
                    successor = successor.left
                # note: there is no left child to successor
                # if the successor is the right child of node
                # (equal to parent of successor to be None beacuse of the while loop above)
                if parent_successor == None: node.right = successor.right
                # if not, replace successor with his right child
                else: parent_successor.left = successor.right
                # replace the node with his successor
                node.key = successor.key

            return root


        match type:
            case "recursive": return recursive_delete(self.root, [])
            case "iterative": return iterative_delete(self.root, [])
            case _: return "Invalid type"
    
        self.root = recursive_delete(self.root, key)

    
