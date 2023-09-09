#!/usr/bin/env python
# coding: utf-8

# Q1.Implement Binary tree

# In[6]:


class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def PrintTree(self):
        print(self.data)

root = BinaryTree(35)
root.PrintTree()


# Q2.Find height of a given tree.

# In[10]:


class Node:
  def __init__(self):
    self.left = None;
    self.right = None;

class BST:
  def __init__(self):
    self.root = Node();

    one = Node();
    two = Node();
    self.root.left = one;
    self.root.right = Node();

    three = Node();
    four = Node();
    five = Node();
    one.left = three;
    two.left = four;
    two.right = five;

  def findMax(self, a, b):
    if a >= b:
      return a;
    else:
      return b;
  
  def findHeight(self, root):
  
    if root is None:
      return 0;

    return self.findMax(self.findHeight(root.left), self.findHeight(root.right)) + 1;

myTree = BST();

print("Height of tree: ", myTree.findHeight(myTree.root))






# Q3.Perform Pre-order, Post-order, In-order traversal.

# In[39]:


class TreeNode:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def preorder(TreeNode):
    if TreeNode is None:
        return
    
    print(TreeNode.data, end=" ")
    
    preorder(TreeNode.left)
    
    preorder(TreeNode.right)

def inorder(TreeNode):
    if TreeNode is None:
        return
    
    inorder(TreeNode.left)
    
    print(TreeNode.data, end=" ")
    
    inorder(TreeNode.right)

def postorder(TreeNode):
    if TreeNode is None:
        return
    
    postorder(TreeNode.left)
    
    postorder(TreeNode.right)
    
    print(TreeNode.data, end=" ")
    
root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)

print("Inorder traversal")
inorder(root)
print("\nPreorder traversal")
preorder(root)
print("\nPostorder traversal")
postorder(root)


# Q4.Function to print all the leaves in a given binary tree.

# In[18]:


class Node:
 
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
def newNode(data):
    temp = Node(data)
    return temp
 
def printleafNodes(root):
    # base case
    if not root:
        return
   
    st = []
    st.append(root)
 
    while len(st) > 0:
        root = st.pop()
 
        if not root.left and not root.right:
            print(root.data, end=" ")
 
        if root.right:
            st.append(root.right)
        if root.left:
            st.append(root.left)

if __name__ == '__main__':
 
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(4)
    root.right.left = newNode(5)
    root.right.right = newNode(8)
    root.right.left.left = newNode(6)
    root.right.left.right = newNode(7)
    root.right.right.left = newNode(9)
    root.right.right.right = newNode(10)
    printleafNodes(root)


# Q5.Implement BFS (Breath First Search) and DFS (Depth First Search)

# In[38]:


class TreeNode:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def preorder(TreeNode):
    if TreeNode is None:
        return
    
    print(TreeNode.data, end=" ")
    
    preorder(TreeNode.left)
    
    preorder(TreeNode.right)

def inorder(TreeNode):
    if TreeNode is None:
        return
    
    inorder(TreeNode.left)
    
    print(TreeNode.data, end=" ")
    
    inorder(TreeNode.right)

def postorder(TreeNode):
    if TreeNode is None:
        return
    
    postorder(TreeNode.left)
    
    postorder(TreeNode.right)
    
    print(TreeNode.data, end=" ")

def printLevelOrder(root):
    queue = []
    queue.append(root)
    while queue:
        tempNode = queue.pop(0)
        print(tempNode.data, end=" ")
        
        if tempNode.left:
            queue.append(tempNode.left)
        
        if tempNode.right:
            queue.append(tempNode.right)
            
root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)

print("Inorder traversal")
inorder(root)
print("\nPreorder traversal")
preorder(root)
print("\nPostorder traversal")
postorder(root)
print("\nLevelorder traversal")
printLevelOrder(root)


# Q6.Find sum of all left leaves in a given Binary Tree.

# In[20]:


class Node:
 
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
 
def leftLeavesSumRec(root, isLeft, summ):
    if root is None:
        return
     
    if root.left is None and root.right is None and isLeft == True:
        summ[0] += root.key
 
    leftLeavesSumRec(root.left, 1, summ)
    leftLeavesSumRec(root.right, 0, summ)
     
def leftLeavesSum(root):
    summ = [0]
     
    leftLeavesSumRec(root, 0, summ)
     
    return summ[0]
 
root = Node(20);
root.left= Node(9);
root.right   = Node(49);
root.right.left = Node(23);
root.right.right= Node(52);
root.right.right.left  = Node(50);
root.left.left  = Node(5);
root.left.right = Node(12);
root.left.right.right  = Node(12);
 
print ("Sum of left leaves is", leftLeavesSum(root))


# Q7.Find sum of all nodes of the given perfect binary tree.

# In[21]:


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def createNode(data):
    newNode = Node(data)
    return newNode

def calculateSum(temp):
    sum, sumLeft, sumRight = 0, 0, 0
    if root is None:
        print("Tree is empty")
        return 0
    else:
        if temp.left is not None:
            sumLeft = calculateSum(temp.left)
        if temp.right is not None:
            sumRight = calculateSum(temp.right)
        sum = temp.data + sumLeft + sumRight
        return sum

root = createNode(10)
root.left = createNode(20)
root.right = createNode(30)
root.left.left = createNode(40)
root.right.left = createNode(50)
root.right.right = createNode(60)
print("Sum of all nodes of binary tree:", calculateSum(root))


# Q8.Count subtress that sum up to a given value x in a binary tree

# In[27]:



class Node:

   def __init__(self, data):

       self.data = data
       self.left = None
       self.right = None

   def getNode(data):

       newNode = Node(data)
       return newNode


count = 0
ptr = None

def countSubtreesWithSumXUtil(root, x):

   global count, ptr

   l = 0
   r = 0

   if (root == None):
       return 0

   l += countSubtreesWithSumXUtil(root.left, x)
   r += countSubtreesWithSumXUtil(root.right, x)

   if (l + r + root.data == x):
       count += 1

   if (ptr != root):
       return l + root.data + r

   return count

if __name__ == '__main__':

   root = getNode(5)
   root.left = getNode(-10)
   root.right = getNode(3)
   root.left.left = getNode(9)
   root.left.right = getNode(8)
   root.right.left = getNode(-4)
   root.right.right = getNode(7)

   x = 7
   ptr = root

   print("Count = " + str(countSubtreesWithSumXUtil( root, x)))


# Q9.Find maximum level sum in Binary Tree

# In[29]:


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 

def dfs(root, level, mm):

    if not root:
        return
 
    mm[level] = mm.get(level, 0) + root.data
 
    level += 1
 
    dfs(root.left, level, mm)
 
    dfs(root.right, level, mm)
 
def maxLevelSum(root):
    # Base case
    if not root:
        return 0
 
    mm = {}
 
    dfs(root, 0, mm)
 
    result = float('-inf')
 
    for val in mm.values():
        result = max(result, val)
 
    return result

def newNode(data):
    node = Node(data)
    return node
if __name__ == "__main__":
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(4)
    root.left.right = newNode(5)
    root.right.right = newNode(8)
    root.right.right.left = newNode(6)
    root.right.right.right = newNode(7)
 
    print("Maximum level sum is", maxLevelSum(root))


# Q10.Print the nodes at odd levels of a tree

# In[35]:


class newNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
 
def printOddNodes(root, isOdd = True):
     
    if (root == None):
        return
 
    if (isOdd):
        print(root.data, end = " ")
 
    printOddNodes(root.left, not isOdd)
    printOddNodes(root.right, not isOdd)

if __name__ == '__main__':
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(4)
    root.left.right = newNode(5)
    printOddNodes(root)


# In[ ]:




