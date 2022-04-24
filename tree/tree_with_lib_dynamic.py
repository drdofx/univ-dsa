from binarytree import tree, bst, Node

root = Node("D")
root.left = Node("B")
root.left.left = Node("A")
root.left.right = Node("C")
root.right = Node("F")
root.right.left = Node("E")
root.right.right = Node("G")

# Insert Binary Search Tree
def insertNodeBST(node, data):
    # print(node)
    if node == None:
        return Node(data)
    else:
        if data < node.value:
            node.left = insertNodeBST(node.left, data)
        else:
            node.right = insertNodeBST(node.right, data)
        return node

# Insert Binary Tree
def insertNodeBT(node, data):
    if node == None:
        return Node(data)
    else:
        queue = [];  
        #Add root to the queue  
        queue.append(node);  
            
        while(True):  
            the_node = queue.pop(0);  
            #If node has both left and right child, add both the child to queue  
            if(the_node.left != None and the_node.right != None):  
                queue.append(the_node.left);  
                queue.append(the_node.right);  
            else:  
                #If node has no left child, make newNode as left child  
                if(the_node.left == None):  
                    the_node.left = Node(data);  
                    queue.append(the_node.left);  
                else:  
                    #If node has left child but no right child, make newNode as right child  
                    the_node.right = Node(data);  
                    queue.append(the_node.right);  
                break;  

root_data = input("Enter root node: ")
root_bst = Node(root_data)
root_bt = Node(root_data)
while True:
    data = (input("Enter node: "))
    if (data == "exit"):
        break
    insertNodeBST(root_bst, data)
    insertNodeBT(root_bt, data)

for tree in [root_bst, root_bt]:
    print(tree)
    print(tree.properties)
    print("Inorder traversal: " + str(tree.inorder))
    print("Preorder traversal: " + str(tree.preorder))
    print("Postorder traversal: " + str(tree.postorder))