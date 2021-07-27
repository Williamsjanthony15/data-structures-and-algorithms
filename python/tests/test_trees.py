import pytest
from code_challenges.Binary_Trees.binary_trees import Node, BinaryTree

def test_finding_max_value_in_binary_tree():
    treeStub = BinaryTree
    treeStub.root = Node(2)
    treeStub.root.left = Node(7)
    treeStub.root.right = Node(9)
    treeStub.root.left.right = Node(12)
    treeStub.root.left.right.left = Node(1)
    treeStub.root.left.right.right = Node(3)
    treeStub.root.right.right = Node(8)
    treeStub.root.right.left = Node(10)
    actual = BinaryTree.maxData(12)
    expected = 12
    assert actual == expected 