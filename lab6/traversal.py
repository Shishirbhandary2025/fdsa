class TreeNode:
    """
    Represents a node in a binary tree.
    """
    def __init__(self, data):
        """
        Initializes a TreeNode object.

        Args:
            data: The data to be stored in the node.
        """
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    """
    Represents a binary tree.
    """
    def __init__(self, root=None):
        """
        Initializes an empty BinaryTree object.

        Args:
            root: The root TreeNode of the tree (optional).
        """
        self.root = root

    def in_order_traversal(self, node=None):
        """
        Performs an in-order traversal of the tree and prints the data of each node.

        Args:
            node: The current node being visited (defaults to the root).
        """
        if node is None:
            node = self.root

        if node:
            self.in_order_traversal(node.left)
            print(node.data, end=" ")
            self.in_order_traversal(node.right)

    def post_order_traversal(self, node=None):
        """
        Performs a post-order traversal of the tree and prints the data of each node.

        Args:
            node: The current node being visited (defaults to the root).
        """
        if node is None:
            node = self.root

        if node:
            self.post_order_traversal(node.left)
            self.post_order_traversal(node.right)
            print(node.data, end=" ")

# Example Usage:
if __name__ == "__main__":
    # Create some nodes
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    # Create a binary tree
    binary_tree = BinaryTree(root)

    print("In-order traversal:")
    binary_tree.in_order_traversal()
    print()

    print("Post-order traversal:")
    binary_tree.post_order_traversal()
    print()
