from os import execlp
import pytest
from code_challenges.Stacks_and_queues.stack_queue import Node, Stack

"""Inst an empty node"""

def test_inst_node():
    new_node = Node()
    # actual = new_node.value
    # expected = None
    # assert actual == expected
    assert new_node

""" Node with single value"""

def  test_node_value():
    new_node = Node(5)
    actual = new_node.value
    expected = 5
    assert actual == expected

"""Checks that a node does NOT = a different value"""

def test_value():
    new_node = Node(5)
    actual = new_node.value
    expected = 6
    assert actual != expected 

""" Create test that will create node with value and next and make sure next is expected"""

def test_next_value():
    new_node = Node(5, Node(6))
    actual = new_node.next.value
    expected = 6
    assert actual == expected 

""" Create a new test inst an empty stack and make sure it exsist"""

def test_empty_stack():
    new_stack = Stack()
    assert new_stack

""" Create a stack and a node, Create stack with the node, Test the node is at top of stack"""

def test_has_a_value():
    new_stack = Stack()
    new_stack.push("a")
    actual = new_stack.top.value
    expected = "a"
    assert actual == expected 



def test_successfully_push_onto_a_stack(create_stack):
    s = create_stack
    s.push(1)
    actual = s.top.value
    expected = 1
    assert actual == expected
    # assert stacking.next == None

def test_succ_push_mult_onto_a_stack(create_stack):
    s = create_stack
    s.push(1)
    s.push(2)
    actual = s.top.value
    expected = 2
    assert actual == expected

def test_succ_pop_a_stack(create_stack):
    s = create_stack
    s.pop()
    actual = s.top
    expected = None
    assert actual == expected

def test_succ_empty_stack_after_mult_pops(create_stack):
    s = create_stack
    s.push(1)
    """ 1 is top"""
    s.push(2)
    """ 1 is bottom 2 is top"""
    s.push(3)
    """ 1 bottom 2 is middle 3 is top"""
    s.pop()
    """ pop 3 off top, 2 new top"""
    s.pop()
    """ pop 2 off top, 1 new top"""
    actual = s.top.value
    expected = 1
    assert actual == expected

# def test_succ_peek_next_item_stack():
#     actual = 
#     expected = 
#     assert actual ==

# def test_succ_instantiate_empty_stack():
#     actual = 
#     expected = 
#     assert actual ==

# def test_calling_pop_or_peek_empty_stack_raises_exception():
#     actual = 
#     expected = 
#     assert actual ==

# def test_succ_enqueue_into_queue():
#     actual = 
#     expected = 
#     assert actual ==

# def test_succ_enqueue_multiple_values_into_queue():
#     actual = 
#     expected = 
#     assert actual ==

# def test_succ_dequeue_out_of_queue_expected_value():
#     actual = 
#     expected = 
#     assert actual ==

# def test_succ_peek_into_a_queue_seeing_the_expected_value():
#     actual = 
#     expected = 
#     assert actual ==

# def test_succ_empty_queue_after_multiple_dequeues():
#     actual = 
#     expected = 
#     assert actual ==

# def test_succ_instantiate_an_empty_queue():
#     actual = 
#     expected = 
#     assert actual ==

# def test_calling_dequeue_or_peek_empty_queue_raises_exception():
#     actual = 
#     expected = 
#     assert actual ==

@pytest.fixture
def create_stack():
    s = Stack()
    return s
