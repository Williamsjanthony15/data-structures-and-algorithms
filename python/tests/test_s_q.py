import pytest
from code_challenges.Stacks_and_queues.stack_queue import Node, Stack

def test_successfully_push_onto_a_stack(create_stack):
    s = create_stack
    s.push(1)
    actual = s.head.value
    expected = 1
    assert actual == expected
    # assert stacking.next == None

def test_succ_push_mult_onto_a_stack(create_stack):
    s = create_stack
    s.push(1)
    s.push(2)
    actual = s.head.value
    expected = 2
    assert actual == expected

def test_succ_pop_a_stack(create_stack):
    s = create_stack
    s.pop()
    actual = s.head
    expected = None
    assert actual == expected

def test_succ_empty_stack_after_mult_pops(create_stack, pushing, popping):
    s = create_stack
    p = pushing
    p.pop()
    p.pop()
    actual = s.head
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

@pytest.fixture
def pushing():
    p = Stack()
    p.push(1)
    p.push(2)
    p.push(3)
    return p

@pytest.fixture
def popping():
    po = pushing()
    po.pop()
    po.pop()
    return po