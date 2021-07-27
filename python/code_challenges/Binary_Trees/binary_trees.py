class Node:

  def __init__(self, value, right=None, left=None):

    self.value = value
    self.right = right
    self.left = left
  
class BinaryTree:
  
  def __init__(self, root=None):
    self.root = root


  def preOrder(self):

    if self.root is None:
      return "Tree is empty"

    order = []

    def direction(root):
      order.append(root.value)

      if root.left is not None:
        direction(root.left)
      
      if root.right is not None:
        direction(root.right)
      
    direction(self.root)
    
    return order


  def inOrder(self):

    if self.root is None:
      return "No Data"
    
    order = []

    def direction(root):
      if root.left is not None:
        direction(root.left)
      
      order.append(root.value)
      
      if root.right is not None:
        direction(root.right)
    
    direction(self.root)

    return order


  def postOrder(self):
    
    if self.root is None:
      return "No data"
    
    order = []

    def direction(root):
      if root.left is not None:
        direction(root.left)

      if root.right is not None:
        direction(root.right)

      order.append(root.value)

    direction(self.root)

    return order

  def maxData(self):
    if self.root is None:
      return "No data"

    def findMax(root):

      dataRoot = root.value
      leftDR = findMax(root.left)
      rightDR = findMax(root.right)
      if (leftDR > dataRoot):
        dataRoot = leftDR
      if (rightDR > dataRoot):
        dataRoot = rightDR
      return dataRoot

    

class BinarySearchTree(BinaryTree):
  
  def __init__(self, root=None):
    self.root = root

  
  def add(self, value):

    if value is None or type(value) == str:
      return "Please Input Number"
        
    newNode = Node(value)


    if self.root is None:
      self.root = newNode
      
    current = self.root

    while current:

      if current.value > value:
        if current.left is None:
          current.left = newNode
        else:
          current = current.left

      if current.value < value:
        if current.right is None:
          current.right = newNode
        else:
          current = current.right

      if current.value == value:
        return "Already Have that value"


  def contains(self, value):
    current = self.root

    while current is not None:
      if current.value > value:
        current = current.left
      if current.value < value:
        current = current.right
      if current.value == value:
        return True
      else:
        return False