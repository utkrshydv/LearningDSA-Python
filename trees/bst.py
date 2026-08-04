class Node:
  def __init__(self, value):
    self.left = None
    self.right = None
    self.value = value

def insert(root, value):
  if root == None:
    return Node(value)
  if root.value == value:
    return root
  if root.value > value:
    root.left = insert(root.left, value)
  else:
    root.right = insert(root.right, value)
  return root

def search(root, value):
  if root == None:
    print("Element not found")
    return
  if root.value == value:
    print("Element found")
    return
  if root.value > value:
    search(root.left, value)
  else:
    search(root.right, value)
    

def inOrder(root):
  if root!=None:
    inOrder(root.left)
    print(root.value, end = " ")
    inOrder(root.right)
    
def get_successor(root):
  root = root.right
  while root!=None and root.left != None:
    root = root.left
  return root
 
def delete(root, value):
  if root==None:
    return root
  if root.value > value:
    root.left = delete(root.left, value)
  elif root.value < value:
    root.right = delete(root.right, value)
  else:
    if root.left == None: 
      return root.right
    if root.right == None:
      return root.left
    else:
      succ = get_successor(root) 
      root.value = succ.value
      root.right = delete(root.right, succ.value)
  return root 



root = Node(20)
root.left = Node(15)
root.right = Node(30)
root.left.left = Node(12)
root.left.right = Node(18)
root = insert(root, 50)

search(root, 50)
 
inOrder(root)               

