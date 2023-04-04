# Binary search tree
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def inorder(root: Node | None):
    if root is not None:
        inorder(root.left)
        print(str(root.key) + '->', end=' ')
        inorder(root.right)


def insert(node, key: int) -> Node:
    if node is None:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return node


def minValueNode(node) -> Node:
    current = node
    while current.left is not None:
        current = current.left
    return current


def deleteNode(root, key: int) -> Node:
    # Base case
    if root is None:
        return root
    if key < root.key:
        root.left = deleteNode(root.left, key)
    elif key > root.key:
        root.right = deleteNode(root.right, key)
    else:
        # Node with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        # Node with two children
        # Get the inorder successor (smallest in the right subtree)
        temp = minValueNode(root.right)
        root.key = temp.key
        root.right = deleteNode(root.right, temp.key)
    return root


def findNode(root, key: int) -> Node:
    if root is None or root.key == key:
        return root
    if root.key < key:
        return findNode(root.right, key)
    return findNode(root.left, key)


def deleteTree(root):
    if root is None:
        return root
    deleteTree(root.left)
    deleteTree(root.right)
    root = None
    return root
