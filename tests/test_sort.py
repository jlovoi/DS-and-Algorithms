from algorithms import merge_sort as merge
from algorithms import insertion_sort as insert
from algorithms import heap_sort as heap

import pytest

arrayArray = [
        [4, 1, 3, 2, 7, 16, 9, 10, 14, 8],
        [2, 16, 4, 9, 14, 7, 8, 10, 1, 3],
    ]
solution = [1, 2, 3, 4, 7, 8, 9, 10, 14, 16]

def test_insertion_sort():
    assert [insert.insertion(arrayArray[0]), insert.insertion(arrayArray[1])] == [solution, solution]


def test_merge_sort():
    assert [merge.merge_sort(arrayArray[0]), merge.merge_sort(arrayArray[1])] == [solution, solution]

def test_heap_sort():
	assert [heap.heap_sort(arrayArray[0]), heap.heap_sort(arrayArray[1])] == [solution, solution]
        


if __name__ == '__main__':
    pytest