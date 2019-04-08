class Node():
	"""
	Binary Search Tree Node, represented by Pointers to its parent, its left child, and right child
	"""
	def __init__(self, val=None, parent=None, lchild=None, rchild=None):
		self.val = val
		self.parent = parent
		self.lchild = lchild
		self.rchild = rchild

class BinarySearchTree():
	"""
	Binary Search Tree, where each left child is less than parent, and each right child is greater than parent
	There are no duplicate values in this implementation
	It is important to recognize that a BST with the same values can have different structrue based on insertion order
	The smaller the height of the tree, the more efficient it is
	"""
	def __init__(self):
		self.length = 0
		self.root = None


	def search(self, val):
		# Empty Check
		if self.root == None:
			return None

		# Search for the proper placement of given value
		current_node = self.root

		while current_node != None and current_node.val != val:
			if val < current_node.val:
				current_node = current_node.lchild
			else:
				current_node = current_node.rchild

		return current_node


	def insert(self, val):
		# First, make sure this value isnt already in the BST
		#if self.search(val) == None:
			#return

		to_insert = Node(val)

		# if this is the first insertion, make insertion the root
		if self.root == None:
			self.root = to_insert
			return

		current_node = self.root
		current_parent = None
		
		# Traverse through the BST based on value
		while current_node != None:
			# Move one level down the BST
			current_parent = current_node

			if val < current_parent.val:
				current_node = current_parent.lchild
			else:
				current_node = current_parent.rchild

		to_insert.parent = current_parent

		if val < current_parent.val:
			current_parent.lchild = to_insert
		elif val > current_parent.val:
			current_parent.rchild = to_insert


	def delete(self, val):
		# first get the val
		node = self.search(val)
		# if its not in the tree, then i guess we can just say it was successfully deleted
		if node == None:
			return 0

		# if no lchild, replace node with its rchild (even if its None), effectively handling no children case
		if node.lchild == None:
			parent = node.parent
			node = node.rchild
			node.parent = parent
			return 0

		# same as above, but for rchild
		elif node.rchild == None:
			parent = node.parent
			node = node.lchild
			node.parent = parent
			return 0

		else:
			# if successor is rchild, replace node with rchild
			if self.get_successor(node.val) == node.rchild:
				parent  = node.parent
				lchild = node.lchild
				rchild = node.rchild
				node = self.get_successor(node.val)
				print("hello", node.val)
				node.parent = parent
				node.lchild = lchild
				node.rchild = rchild
				return 0

			# this is where it gets weird
			# if successor is not rchild, then replace successor(p) with its rchild, and replace node with successor
			else:
				parent = node.parent
				lchild = node.lchild
				rchild = node.rchild
				p = self.get_successor(node.val)
				p.parent.lchild = p.rchild
				node = p
				node.parent = parent
				node.lchild = lchild
				node.rchild = rchild
				return 0




	def get_max(self, node=None):
		# return the node with max value
		if node == None:
			node = self.root
		while node.rchild != None:
			node = node.rchild

		return node


	def get_min(self, node):
		# return the node with min value
		if node == None:
			node = self.root
		while node.lchild != None:
			node = node.lchild

		return node


	def get_successor(self, val):
		# return the smallest key that is greater than parameter val, None if val is not in the tree
		# first, search for this val
		node = self.search(val)
		if node == None:
			return None

		# if there is a right subtree, then it is the minimum of that
		if node.rchild != None:
			return self.get_min(node.rchild)
		# else, it is the first ancestor that is greater than node
		while node.parent != None and node.parent.val <= node.val:
			node = node.parent
		return node.parent


	def get_predecessor(self, val):
		# return the greatest key that is less than parameter val, None if val is not in the tree
		# search for val
		node = self.search(val)
		if node == None:
			return None

		# if there is a left subtree, then it is the max of that tree
		if node.lchild != None:
			return self.get_max(node.lchild)
		# else, it is first ancestor that is less than val
		while node.parent != None and node.parent.val >= node.val:
			node = node.parent
		return node.parent
		

	def __repr__(self):
		string = str(self.root.val) + str(self.root.lchild.val) + str(self.root.lchild.rchild.val) + str(self.root.rchild.val)
		return string




if __name__ == '__main__':
	array = [15, 6, 7, 13, 3, 2, 9, 4, 18, 20]
	bst = BinarySearchTree()

	for i in range(0, len(array)):
		#print (array[i])
		bst.insert(array[i])

	for i in range(0, len(array) - 1):
		bst.delete(i)

	print(bst)