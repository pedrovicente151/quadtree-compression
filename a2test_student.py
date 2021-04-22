"""
Assignment 2: Quadtree Compression

=== CSC148 Winter 2021 ===
Department of Mathematical and Computational Sciences,
University of Toronto Mississauga

=== Module Description ===
This module contains the test suite
"""

import pytest
from a2tree import QuadTreeNode, QuadTreeNodeEmpty, QuadTreeNodeLeaf, QuadTree

"""
Test cases
"""


def test_split_quadrants_1():
    example = QuadTree()
    assert example._split_quadrants([[1, 2], [3, 4]]) == \
           [[[1]], [[2]], [[3]], [[4]]]


def test_split_quadrants_2():
    example = QuadTree()
    assert example._split_quadrants([[1, 2, 3, 4],
                                     [4, 5, 6, 7],
                                     [8, 9, 10, 11],
                                     [12, 13, 14, 15]]) == \
           [
               [[1, 2], [4, 5]],
               [[3, 4], [6, 7]],
               [[8, 9], [12, 13]],
               [[10, 11], [14, 15]]
           ]


def test_split_quadrants_3():
    example = QuadTree()
    assert example._split_quadrants([[11, 12, 13],
                                     [14, 15, 16],
                                     [17, 18, 19]]) == \
           [
               [[11]],
               [[12, 13]],
               [[14], [17]],
               [[15, 16], [18, 19]]
           ]


def test_restore_from_preorder_1():
    node = QuadTree.restore_from_preorder(['','E','210','E', '103'], 1, 2)
    assert node.convert_to_pixels() == [[210], [103]]


def test_restore_from_preorder_2():
    node = QuadTree.restore_from_preorder(['',
                                           '', 'E', '77', 'E', '44',
                                           '5',
                                           'E',
                                           '', '2', '3', 'E', 'E'], 4, 4)
    assert node.convert_to_pixels() == [[255, 77, 5, 5],
                                        [255, 44, 5, 5],
                                        [255, 255,  2, 3],
                                        [255, 255, 255, 255]]


def test_restore_from_preorder_3():
    node = QuadTree.restore_from_preorder(['',
                                           '11',
                                           '', 'E', 'E', '12', '13',
                                           '', 'E', '14', 'E', '17',
                                           '', '15', '16', '18', '19'], 3, 3)
    assert node.convert_to_pixels() == [[11, 12, 13],
                                        [14, 15, 16],
                                        [17, 18, 19]]


if __name__ == '__main__':
    pytest.main(['a2test_student.py'])
