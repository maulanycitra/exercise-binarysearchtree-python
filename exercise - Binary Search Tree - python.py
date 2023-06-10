#!/usr/bin/env python
# coding: utf-8

# In[4]:


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.middle = None
        self.right = None
        
class Tree:
    def __init__(self, root, name=''):
        self.root = root
        self.name = name
        
node = Node(10)

node.left = Node(5)
node.middle = Node(7)
node.right = Node(6)

node.left.left = Node(8)
node.left.right = Node(9)

node.middle.left = Node(10)
node.middle.right = Node(11)

node.right.left = Node(12)
node.right.right = Node(13)

myTree = Tree(node, 'Basic BST')

print(myTree.name)
print('Node Kiri:',myTree.root.left.data)
print('Node Tengah:',myTree.root.middle.left.data)
print('Node Kanan:',myTree.root.right.right.data)


# In[ ]:




