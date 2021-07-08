class Node():
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class Stack():
    """
    Default
    """ 
    def __init__(self):
        self.top = None
    """
    Empty check
    """
    def isEmpty(self):
        if self.top == None:
            return True
        else:
            return False
    """
    Adding Nodes to a stack in the beginning
    """

    def push(self,value):
        if self.top == None:
            self.top = Node(value)
        else:
            newNode = Node(value)
            newNode.next = self.top
            self.top = newNode
    """ 
    Popping if !empty
    """
    def pop(self):
        if self.isEmpty():
            return None
        else:
            popNode = self.top
            self.top = self.top.next
            popNode.next = None
            return popNode.value
    """
    Looking to see what data is there if any at all
    """
    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.top.data
    """
    Displaying the data 
    """
    def display(self):
        displayingNode = self.top
        if self.isempty():
            print("empty")
        else:
            while(displayingNode != None):
                print('Beginning', displayingNode.data, end = " ")
                displayingNode = displayingNode.next
            return