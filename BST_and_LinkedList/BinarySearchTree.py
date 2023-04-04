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


def printTree(root, space: int):
    if root is None:
        return
    space += 10
    printTree(root.right, space)
    print()
    for i in range(10, space):
        print(end=' ')
    print(root.key)
    printTree(root.left, space)


def getHeight(root) -> int:
    if root is None:
        return 0
    return max(getHeight(root.left), getHeight(root.right)) + 1


# ======================== AVL Tree ========================
def createAVLFromBST(root) -> Node:

    # Base case
    if root is None:
        return root

    # Recursively create left and right subtrees

    root.left = createAVLFromBST(root.left)
    root.right = createAVLFromBST(root.right)

    # Get the balance factor of this ancestor node to check
    # whether this node became unbalanced
    height_difference = getHeight(root.left) - getHeight(root.right)

    # If this node becomes unbalanced, then there are 4 cases``
    if height_difference > 1:
        # Left Left Case
        if getHeight(root.left.left) >= getHeight(root.left.right):
            root = rightRotate(root)
        # Left Right Case
        else:
            root.left = leftRotate(root.left)
            root = rightRotate(root)
    elif height_difference < -1:
        # Right Right Case
        if getHeight(root.right.right) >= getHeight(root.right.left):
            root = leftRotate(root)
        # Right Left Case
        else:
            root.right = rightRotate(root.right)
            root = leftRotate(root)
    return root


def rightRotate(root):
    new_root = root.left
    root.left = new_root.right
    new_root.right = root
    return new_root


def leftRotate(root):
    new_root = root.right
    root.right = new_root.left
    new_root.left = root
    return new_root
