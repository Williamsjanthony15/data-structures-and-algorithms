import pytest
from code_challenges.stacks_queue_brackets.s_q_brackets import string_balance



# def test_inst_node():
#     new_node = Node()
#     # actual = new_node.value
#     # expected = None
#     # assert actual == expected
#     assert new_node

def test_string_balance():
    new_string = string_balance()
    actual = new_string
    expected = "Balanced"
    assert actual == expected

# print(string,"-", check(string))
  
# string = "[{}{})(]"
# print(string,"-", check(string))
  
# string = "((()"
# print(string,"-",check(string))

