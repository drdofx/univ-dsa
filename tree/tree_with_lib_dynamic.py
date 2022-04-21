from binarytree import tree, bst, Node

root = Node("D")
root.left = Node("B")
root.left.left = Node("A")
root.left.right = Node("C")
root.right = Node("F")
root.right.left = Node("E")
root.right.right = Node("G")

def insertNode(node, data):
    # print(node)
    if node == None:
        return Node(data)
    else:
        if data < node.value:
            node.left = insertNode(node.left, data)
        else:
            node.right = insertNode(node.right, data)
        return node

# TODO: 

# def insertNode(node, data):
#     if node == None:
#         return Node(data)
#     else:
#         if node.left == None:
#             node.left = insertNode(node.left, data)
#         else:
#             node.right = insertNode(node.right, data)
#         return node

root_data = input("Enter root node: ")
root = Node(root_data)
while True:
    data = (input("Enter node: "))
    if (data == "exit"):
        break
    insertNode(root, data)

print(root)

print("Inorder traversal: " + str(root.inorder))
print("Preorder traversal: " + str(root.preorder))
print("Postorder traversal: " + str(root.postorder))