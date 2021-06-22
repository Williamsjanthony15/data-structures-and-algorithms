from code_challenges.linked_list.linked_list import LinkedList, Node
# from LinkedList import includes


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

def test_can_succesfully_add_a_node_to_the_end_of_the_list():
    ll1 = LinkedList()
    ll1.insert('a').insert('b').insert('c').insert('d')
    ll1.append('Z')
    expected = ['d', 'c', 'b', 'a', 'Z']
    current = ll1.head
    index = 0
    while current is not None:
        assert current.value == expected[index]
        index+=1
        current = current.next

def test_can_sucessfully_add_multiple_nodes_to_the_end_of_list():
    ll1 = LinkedList()
    ll1.append('a').append('b').append('c').append('d')
    expected = ['a', 'b', 'c', 'd']
    current = ll1.head
    index = 0
    while current is not None:
        assert current.value == expected[index]
        index+=1
        current = current.next

def test_can_succesfully_insert_a_node_before_a_node_in_middle_of_list():
    ll1 = LinkedList()
    ll1.append('a').append('b').append('c').append('d')
    ll1.insert_before('c', 'Z')
    expected = ['a', 'b', 'Z', 'c', 'd']
    current = ll1.head
    index = 0
    while current is not None:
        assert current.value == expected[index]
        index+=1
        current = current.next

def test_can_succesfully_insert_a_node_before_the_first_node_of_a_linked_list():
    ll1 = LinkedList()
    ll1.append('a').append('b').append('c').append('d')
    ll1.insert_before('a', 'Z')
    expected = ['Z', 'a', 'b', 'c', 'd']
    current = ll1.head
    index = 0
    while current is not None:
        assert current.value == expected[index]
        index+=1
        current = current.next

def test_Can_successfully_insert_after_a_node_in_the_middle_of_the_linked_list():
    ll1 = LinkedList()
    ll1.append('a').append('b').append('c').append('d')
    ll1.insert_after('b', 'Z')
    expected = ['a', 'b', 'Z', 'c', 'd']
    current = ll1.head
    index = 0
    while current is not None:
        assert current.value == expected[index]
        index+=1
        current = current.next

def test_Can_successfully_insert_a_node_after_the_last_node_of_the_linked_list():
    ll1 = LinkedList()
    ll1.append('a').append('b').append('c').append('d')
    ll1.insert_after('d', 'Z')
    expected = ['a', 'b', 'c', 'd', 'Z']
    current = ll1.head
    index = 0
    while current is not None:
        assert current.value == expected[index]
        index+=1
        current = current.next
