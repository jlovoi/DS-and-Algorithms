from algorithms import merge_sort as merge
from algorithms import insertion_sort as insert
from algorithms import heap_sort as heap
from structures import stack as stack
from structures import queue as queue
from structures import linked_list as linkedlist

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

def test_stack_structure():
	myStack = stack.Stack()
	for i in range(0, len(arrayArray[0])):
		myStack.push(arrayArray[0][i])

	for i in range(len(arrayArray[0])-1, -1, -1):
		assertEqual(myStack.pop(), arrayArray[0][i])

def test_stack_isEmpty():
	myStack = stack.Stack()
	assert myStack.isEmpty() == True

	myStack.push(5)
	assert myStack.isEmpty() == False

	myStack.stack_pop()
	assert myStack.isEmpty() == True
	

def test_queue_isEmpty():
	myQueue = queue.Queue()
	assert myQueue.isEmpty() == True

	myQueue.enqueue(5)
	assert myQueue.isEmpty() == False

	myQueue.dequeue()
	assert myQueue.isEmpty() == True

def test_queue_isFull():
	myQueue = queue.Queue()
	array = [10] * 20

	assert myQueue.isFull() == False

	for i in range(0, len(array)):
		myQueue.enqueue(array[i])

	assert myQueue.isFull() == True


def test_queue_structure():
	myQueue = queue.Queue()

	for i in range(0, len(arrayArray[0])):
		myQueue.enqueue(arrayArray[0][i])

	for i in range(0, len(arrayArray[0])):
		assertEqual(myQueue.dequeue(), arrayArray[0][i])

	myQueue.enqueue(5)
	dequeued = myQueue.dequeue()
	assert dequeued == 5


def test_linkedlist_structure():
	myLinkedList = linkedlist.LinkedList()

	for i in range(0, len(arrayArray[0])):
		myLinkedList.insert(arrayArray[0][i])

	for i in range(0, len(arrayArray[0])):
		assertEqual(myLinkedList.get(i), arrayArray[0][i])


if __name__ == '__main__':
    pytest