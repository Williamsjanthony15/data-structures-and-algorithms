class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self, head = None):
        self.head = head

    def insert(self, value):
        node = Node(value)

        if self.head is not None:
            node.next = self.head # -> pears, -> oranges, -> apples
        self.head = node #HEAD: pears -> oranges -> apples

    def __str__ (self):
        list_input = []
        if self.head is None:
            return  "there is no node value"
        current = self.head

        while current is not None:
            list_input.append(current.value)
            current = current.next


    def includes(self, value):
        current = self.head

        while current.value is not None:
            if current.value == value:
                return True
            current = current.next
        return False


#




# current = ll2.head
# while current.value is not None:
#     do something
#     current = current.next

# if __name__ == "__main__":
#     ll2 = LinkedList()
#     ll2.insert('apples')
#     ll2.insert('orange')
#     ll2.insert('pears')

# function link list head -> apples? / nope -> apples yet? / nope -> apples yet? / true
# if linked list's value becomes none, That is the end of the linked list.

## while loop  - if value is in the linked list, return items, if not than return None
# THIS IS HOW TO DO IT! MAIN WAY TO DO THIS!



# Manual long route
#     ll = LinkedList()
#     node1 = Node('apples')
#     node2 = Node('orange')
#     node3 = Node('pear')
#     ll.head == node1
#     node1.next == node2
#     node2.next == node3

# Should return this llhead = apples -> oranges -> pear -> None

# ll1 = LinkedList(Node('apples', Node('Oranges', Node('Pear'))))
# Single line on how to do it. BUT you cant reference inside the initial Node

