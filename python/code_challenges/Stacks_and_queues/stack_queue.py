class Node():
    def __init__(self, value=None, next=None):
        self.value = value,
        self.next = next,

class StackQueues():
    
    def __init__(self, node=None):
        self.top = node

    def append(self):

        stack = []
        stack.append('a')
        stack.append('b')
        stack.append('c')
        stack.append('d')
        print('First Stack Attempt')
        print(stack)

        popOne = stack.pop()
        popTwo = stack.pop()
        popThree = stack.pop()
        popFour = stack.pop()

        popStack = [popOne, popTwo, popThree, popFour]
        
        print(popStack)
