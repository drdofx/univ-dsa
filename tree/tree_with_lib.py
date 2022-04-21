from binarytree import tree, bst, Node

# my_tree = tree(height=3, is_perfect=True, letters=True)
# my_bst = bst(height=3, is_perfect=False)

# print(my_tree)
# print(my_bst)

root = Node("D")
root.left = Node("B")
root.left.left = Node("A")
root.left.right = Node("C")
root.right = Node("F")
root.right.left = Node("E")
root.right.right = Node("G")

print(root)

prop = root.properties

# print(prop)

print("Inorder traversal: " + str(root.inorder))
print("Preorder traversal: " + str(root.preorder))
print("Postorder traversal: " + str(root.postorder))
# print(root.levelorder)