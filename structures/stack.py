class Stack():
	"""
	Class representing the Stack Data Structure, which uses LIFO
	"""
	def __init__(self):
		self._stack = []
		self._count = 0


	def isEmpty(self):
		# If count = 0, then there are obviously no elements in the stack
		if self._count == 0:
			return True
		else:
			return False

	def push(self, num):
		# Just a simple append
		self._stack.append(num)
		self._count += 1

	def pop(self):
		# if stack is not empty, pop (remove and return) the most recently pushed element
		if not self.isEmpty:
			popped = self._stack[self._count-1]
			self._stack.remove(self._count-1)
			return popped
		else:
			raise ValueError("Stack is empty, nothing to pop!")

	
