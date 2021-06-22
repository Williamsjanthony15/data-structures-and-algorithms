from linked_list.linked_list import LinkedList, Node
from LinkedList import includes


def test_node_instance():
    node = Node('apples', None)
    actual = node.value
    expected = 'apples'
    assert actual == expected
    assert node.next == None

def test_two_node():
    node2 = Node('orange', None)
    node1 = Node('apples', node2)
    actual = node1.next.value
    expected = 'orange'
    assert actual == expected

def test_empty_ll():
    ll = LinkedList()
    assert ll

def insert_one():
    ll = LinkedList()
    ll.insert('apples')
    actual = ll.head.value
    expected = 'apples'
    assert actual == expected

def pointer():
    ll = LinkedList()
    ll.insert('a')
    ll.insert('b')
    ll.insert('c')
    actual = ll.head.value
    expected = 'c'
    assert actual == expected

def true_search():
    ll = LinkedList(Node('apples', Node('oranges', Node('bananas', Node('cherry')))))
    actual = ll.includes('cherry')
    expected = True
    assert actual == expected


def false_search():
    ll = LinkedList(Node('apples', Node('oranges', Node('bananas', Node('cherry')))))
    actual = ll.includes('watermelon')
    expected = False
    assert actual == expected


#need to insert multiple
#return all
