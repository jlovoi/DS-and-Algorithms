class Queue():
	def __init__(self):
		""" 
		Queue Data Structure, using FIFO implementation
		Queue is preset to size 20, allowing for head/tail implementation at init
		"""
		self._queue = [None] * 20
		# Next element to be dequeued
		self._head = 10
		# Next placement of enqueued item
		self._tail = 10


	def isEmpty(self):
		# When head is equal to tail AND head is None, it is empty
		if self._head == self._tail and self._queue[self._head] == None:
			return True
		else:
			return False

	def isFull(self):
		# When head is equal to tail AND head is not NONE, it is full
		if self._tail == self._head and self._queue[self._head] != None:
			return True
		else:
			return False

	def enqueue(self, num):
		# First, make sure Queue isn't full
		if not self.isFull():
			# set tail equal to enqueued num
			self._queue[self._tail] = num
			if self._tail != 19:
				self._tail += 1
			else:
				self._tail = 0
		else:
			raise ValueError("Queue is Full!")

	def dequeue(self):
		# Check that queue is not empty
		if not self.isEmpty():
			if self._tail != 0:
				self._tail -= 1
			else:
				self._tail = 19
			dequeued = self._queue[self._tail]
			self._queue.pop(self._tail)
			return dequeued
		else:
			raise ValueError("Queue is Empty!")