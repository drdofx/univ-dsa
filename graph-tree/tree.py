# https://www.javatpoint.com/program-to-implement-binary-tree-using-the-linked-list

# Represent a node of binary tree  
class Node:  
    def __init__(self,data):  
        #Assign data to the new node, set left and right children to None  
        self.data = data;  
        self.left = None;  
        self.right = None;  
   
class BinaryTree:  
    def __init__(self):  
        #Represent the root of binary tree  
        self.root = None;  
          
    #insertNode() will add new node to the binary tree  
    def insertNode(self, data):  
        #Create a new node  
        newNode = Node(data);  
          
        #Check whether tree is empty  
        if(self.root == None):  
            self.root = newNode;  
            return;  
        else:  
            queue = [];  
            #Add root to the queue  
            queue.append(self.root);  
              
            while(True):  
                node = queue.pop(0);  
                #If node has both left and right child, add both the child to queue  
                if(node.left != None and node.right != None):  
                    queue.append(node.left);  
                    queue.append(node.right);  
                else:  
                    #If node has no left child, make newNode as left child  
                    if(node.left == None):  
                        node.left = newNode;  
                        queue.append(node.left);  
                    else:  
                        #If node has left child but no right child, make newNode as right child  
                        node.right = newNode;  
                        queue.append(node.right);  
                    break;  
                      
    #inorder() will perform inorder traversal on binary search tree  
    def inorderTraversal(self, node):  
          
        #Check whether tree is empty  
        if(self.root == None):  
            print("Tree is empty");  
            return;  
        else:  
            if(node.left != None):  
                self.inorderTraversal(node.left);  
            print(node.data),  
            if(node.right!= None):  
                self.inorderTraversal(node.right);  
                  
bt = BinaryTree();  
#Add nodes to the binary tree  
   
bt.insertNode(1);  
#1 will become root node of the tree  
print("Binary tree after insertion");  
#Binary after inserting nodes  
bt.inorderTraversal(bt.root);  
   
bt.insertNode(2);  
bt.insertNode(3);  
#2 will become left child and 3 will become right child of root node 1  
print("\nBinary tree after insertion");  
#Binary after inserting nodes  
bt.inorderTraversal(bt.root);  
   
bt.insertNode(4);  
bt.insertNode(5);  
#4 will become left child and 5 will become right child of node 2  
print("\nBinary tree after insertion");  
#Binary after inserting nodes  
bt.inorderTraversal(bt.root);  
   
bt.insertNode(6);  
bt.insertNode(7);  
#6 will become the left child and 7 will become the right child of node 3  
print("\nBinary tree after insertion");  
#Binary after inserting nodes  
bt.inorderTraversal(bt.root);  