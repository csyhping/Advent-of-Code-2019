# apply Node annd link list in python

# define Node class
class Node():
	"""Create a new node, args1 = data, args2 = next"""
	def __init__(self, data = None, next = None):
		super(Node, self).__init__()
		self.data = data 
		self.next = next
	def __repr__(self):
		# print the data of the node
		return str(self.data)

# define Link list class:
class SingleLinkList():
	"""Create a new node"""
	def __init__(self):
		super(SingleLinkList, self).__init__()
		self.head = None

	def __len__(self):
		# the length of the list
		count = 0
		curr = self.head
		while curr is not None:
			count += 1
			curr = curr.next
		return count

	def insertFront(self, insert_data):
		# insert a node at the front of the list
		# Return value: the new head node
		if insert_data is None:
			print('===[NOTE]=== Can not insert [None] data.')
			return None
		node = Node(insert_data, self.head)
		self.head = node 
		return node

	def append(self, append_data):
		# append a node at the last of the list
		# Return value: the new last node
		if append_data is None:
			return None
		node = Node(append_data)
		if self.head is None:
			# if the list is empty
			self.head = node
			return node
		curr = self.head
		while curr.next is not None:
			curr = curr.next
		curr.next = node
		return node

	def is_empty(self):
		return self.head == None

	def show(self):
		print('--[NOTE]--list show start')
		curr = self.head
		while curr is not None:
			print(curr.data)
			curr = curr.next
		print('--[NOTE]--list show end')

# # test single link list #
# l1 = SingleLinkList()
# l2 = SingleLinkList()
# l3 = SingleLinkList()
# print(len(l1))
# a = l1.insertFront('new')
# b = l1.insertFront('new2')
# print(a, b)
# print(len(l1))
# print(len(l2))
# print(l1.is_empty())
# c = l2.append('last')
# d = l2.append('last2')
# print(c, d)
# print(len(l2))
# for i in range(7):
# 	l3.append(i)
# print(len(l3))
# # test node class #
# n1 = Node('fyphia')
# print(n1)
# n2 = Node('loves')
# n3 = Node('placido')
# n1.next = n2
# n2.next = n3

# def printNodes(node):
# 	while node:
# 		print('current node is ', node)
# 		node = node.next
# printNodes(n1)
# # test node class #
