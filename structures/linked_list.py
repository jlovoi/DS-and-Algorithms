class LinkedList():
	"""
	A Linked List uses nodes and pointers to adjacent nodes to make up the list
	This allows for easy insertion and deletion, but is a bit inefficient (relatively speaking)
	This implementation will be a doubly linked list
	"""

	def __init__(self):
		# Just a length that will be incremented upon insertion
		self.length = 0
		self.head = Node()
		self.tail = None


	def insert(self, number, index=None):
		"""
		Create a new node, and insert it at index specified
		by default, node is inserted at the end of the list
		"""

		# if index is None, set to self.length
		if index == None:
			index = self.length

		# if this is the first insertion, just set the head node
		if index == 0 and self.head.next == None:
			self.head.node = number

		# inserting new head
		elif index == 0:
			to_insert = Node(num=number, next=self.head)
			self.head.prev = to_insert
			self.head = to_insert

		# inserting new tail
		elif index == self.length:
			to_insert = Node(num=number, prev=self.tail)
			self.tail.next = to_insert
			self.tail = to_insert


		else:
			nodes = self.traverse(index - 1)
			to_insert = Node(num=number, prev=nodes[0])
			if len(nodes) == 2:
				to_insert.next = nodes[1]
			nodes[0].next = to_insert
			nodes[1].prev = to_insert


	def traverse(self, index):
		"""
		Traverse to the specified index and return an array of size 2 containing node[i] and node[i+1]
		If index is the tail, then only return array of node[i]
		"""

		count = 0
		node = self.head
		ret = []

		while count < index and node.next != None:
			node = node.next
			count += 1

		# return error message if count != index at this point
		if count != index:
			return ValueError("Node does not exist!")

		ret.append(node)
		if node.next != self.tail:
			ret.append(node.next)

		return ret


	def get(self, index):
		# return value of specified node
		return self.traverse(index)[0].node


	def rem(self, index):
		# remove node[index] from the list, return value
		ret = self.traverse(index)[0]

		# if it is neither the head nor the tail
		if ret.prev != None and ret.next != None:
			ret.prev.next = ret.next
			ret.next.prev = ret.prev
			return ret.node

		# if it is the tail
		elif ret.prev != None:
			ret.prev.next = None
			self.tail = ret.prev
			return ret.node

		# if it is the head
		elif ret.next != None:
			ret.next.prev = None
			self.head = ret.next
			return ret.node



class Node():
	#The node will hold the value and pointers to the next and previous nodes
	def __init__(self, prev=None, num=None, nnode=None):
		self.node = num
		self.prev = prev
		self.next = nnode
