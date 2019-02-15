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

		# if this is the first insertion, just set the head and tail node
		if index == 0 and self.head.next == None:
			self.head.node = number
			self.tail = self.head

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

		# inserting inbetween nodes
		else:
			nodes = self.traverse(index - 1)
			to_insert = Node(num=number, prev=nodes[0])
			if len(nodes) == 2:
				to_insert.next = nodes[1]
			nodes[0].next = to_insert
			nodes[1].prev = to_insert

		self.length += 1


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
		if node != self.tail:
			ret.append(node.next)

		return ret


	def get(self, index):
		# return value of specified node
		return self.traverse(index)[0].node


	def rem(self, index): # index = 0
		# remove node[index] from the list, return value
		ret = self.traverse(index)[0] #traverse(0)[0] = 
		self.length -= 1

		# if it is neither the head nor the tail
		if ret.prev != None and ret.next != None:
			ret.prev.next = ret.next
			ret.next.prev = ret.prev
			return ret.node

		# if it is the tail
		elif ret == self.tail:
			ret.prev.next = None
			self.tail = ret.prev
			return ret.node

		# if it is the head
		elif ret == self.head:
			ret.next.prev = None
			self.head = ret.next
			return ret.node



class Node():
	#The node will hold the value and pointers to the next and previous nodes
	def __init__(self, prev=None, num=None, nnode=None):
		self.node = num
		self.prev = prev
		self.next = nnode

if __name__=='__main__':
	arrayArray = [
        [4, 1, 3, 2, 7, 16, 9, 10, 14, 8],
        [2, 16, 4, 9, 14, 7, 8, 10, 1, 3],
    ]

	myLinkedList = LinkedList()

	for i in range(0, 10):
		myLinkedList.insert(arrayArray[0][i])


	print ("1: ",myLinkedList.rem(0) == 4)

	print ("2: ",myLinkedList.rem(8) == 8)

	print ("3: ",myLinkedList.rem(4) == 16)

	arr = [1, 3, 2, 7, 9, 10, 14]

	for i in range(0, myLinkedList.length):
		print (myLinkedList.get(i) == arr[i])
