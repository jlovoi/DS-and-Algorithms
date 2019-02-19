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

	def __repr__(self):
		string = str(self.root.val) + str(self.root.lchild.val) + str(self.root.lchild.rchild.val) + str(self.root.rchild.val)
		return string




if __name__ == '__main__':
	array = [5, 1, 2, 7]
	bst = BinarySearchTree()

	for i in range(0, len(array)):
		#print (array[i])
		bst.insert(array[i])

	print(bst.search(8))