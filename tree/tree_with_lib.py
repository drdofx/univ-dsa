from binarytree import tree, bst, Node

my_tree = tree(height=3, is_perfect=True, letters=True)
my_bst = bst(height=3, is_perfect=False)

print(my_tree)
print(my_bst)

root = Node(4)
root.left = Node(2)
root.left.right = Node(5)
root.left.left = Node(7)
root.right = Node(9)
root.right.left = Node(1)
root.right.right = Node(3)

print(root)

prop = root.properties

print(prop)

print(root.inorder)
print(root.preorder)
print(root.postorder)
print(root.levelorder)