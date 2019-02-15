from algorithms import merge_sort as merge
from algorithms import insertion_sort as insert
from algorithms import heap_sort as heap
from structures import stack as stack
from structures import queue as queue
from structures import linked_list as linkedlist

import pytest

prob1 = [4, 1, 3, 2, 7, 16, 9, 10, 14, 8]
prob2 = [2, 16, 4, 9, 14, 7, 8, 10, 1, 3]

solution = [1, 2, 3, 4, 7, 8, 9, 10, 14, 16]


def test_insertion_sort():
    assert [insert.insertion(prob1[:]), insert.insertion(prob2[:])] == [solution, solution]

def test_merge_sort():
    assert [merge.merge_sort(prob1[:]), merge.merge_sort(prob2[:])] == [solution, solution]

def test_heap_sort():
	assert [heap.heap_sort(prob1[:]), heap.heap_sort(prob2[:])] == [solution, solution]

def test_stack_structure():
	myStack = stack.Stack()
	arr = prob1[:]
	for i in range(0, len(arr)):
		myStack.push(arr[i])

	for i in range(len(arr)-1, -1, -1):
		assert myStack.stack_pop() == arr[i]

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

	arr = prob1[:]

	for i in range(0, len(arr)):
		myQueue.enqueue(arr[i])

	for i in range(0, len(arr)):
		assert myQueue.dequeue() == arr[i]

	myQueue.enqueue(5)
	dequeued = myQueue.dequeue()
	assert dequeued == 5


def test_linkedlist_structure():
	myLinkedList = linkedlist.LinkedList()

	arr = prob2[:]

	print(arr)

	for i in range(0, len(arr)):
		myLinkedList.insert(arr[i])



	for i in range(0, 10):
		assert myLinkedList.get(i) == arr[i]


def test_linkedlist_rem():
	myLinkedList = linkedlist.LinkedList()

	for i in range(0, len(prob1)):
		myLinkedList.insert(prob1[i])

	assert myLinkedList.rem(0) == 4

	assert myLinkedList.rem(8) == 8

	assert myLinkedList.rem(4) == 16

	arr = [1, 3, 2, 7, 9, 10, 14]

	for i in range(0, myLinkedList.length):
		assert myLinkedList.get(i) == arr[i]


if __name__ == '__main__':
    pytest