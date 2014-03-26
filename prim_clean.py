class Heap(list):
	def __init__(self, d):
		self.d = d

	def insert(self, node):
		index = len(self)
		self.append(None)
		parentIndex = self.parentIndex(index)
		while index != 0 and node.key < self[parentIndex].key:
			self[index] = self[parentIndex]
			index = parentIndex
			parentIndex = self.parentIndex(index)
		self[index] = node

	def parentIndex(self, i):
		return (i - 1) / self.d

	def childs(self,ind):	
		tmpList = []
		for n in range(0, self.d):
			tmpList.append(ind*self.d+n+1)
		return tmpList

	def heapify(self, i):
		smallest = i
		for j in self.childs(i):
			if j >= len(self): break
			if self[j].key < self[smallest].key:
				smallest = j
		if smallest != i:
			self[i], self[smallest] = self[smallest], self[i]
			self.heapify(smallest)

	def root(self):
		if not self: return
		root = self[0]	#Save first
		last = self[-1]	#Save last
		self[0] = last	#Overwrite first
		super(Heap, self).pop()	#Remove last
		if self:
			self.heapify(0)
		return root

	def decrease(self,vertex):
		index = self.index(vertex)
		while index > 0 and self[self.parentIndex(index)].key > self[index].key:
			self[index], self[self.parentIndex(index)] = self[self.parentIndex(index)], self[index]
			index = self.parentIndex(index)

class Vertex:
	def __init__(self, name):
		self.name = name
		self.key = float('inf')
		self.p = None

	def __repr__(self):
		if self.p:
			p = self.p.name
		else:
			p = 'None'
		return '('+str(self.name)+', ' + str(self.key)+', '+str(p)+')'

class Edge:
	def __init__(self, node1, node2, weight):
		self.u = node1
		self.v = node2
		self.w = weight

def relax(v, edge):
	if v.key == float('inf'):
		v.key = edge.w
		if v == edge.v:
			v.p = edge.u
		else:
			v.p = edge.v
		q.insert(v)
	elif v.key > edge.w and v not in tree:
		v.key = edge.w
		if v == edge.v:
			v.p = edge.u
		else:
			v.p = edge.v
		q.decrease(v)

def prims():
	while len(q) > 0:
		u = q.root()
		tree.append(u)
		for edge in edges:
			if edge.u == u:
				relax(edge.v, edge)
			elif edge.v == u:
				relax(edge.u, edge)

verticies= []
edges= []
q = Heap(3)
tree = []

#Verticies and edges from example of prims algoeithm in the book
for l in 'abcdefghi':
	verticies.append(Vertex(l))

edges.append(Edge(verticies[0],verticies[1],4))
edges.append(Edge(verticies[0],verticies[7],8))
edges.append(Edge(verticies[1],verticies[2],8))
edges.append(Edge(verticies[1],verticies[7],11))
edges.append(Edge(verticies[2],verticies[3],7))
edges.append(Edge(verticies[2],verticies[5],4))
edges.append(Edge(verticies[2],verticies[8],2))
edges.append(Edge(verticies[3],verticies[4],9))
edges.append(Edge(verticies[3],verticies[5],14))
edges.append(Edge(verticies[4],verticies[5],10))
edges.append(Edge(verticies[5],verticies[6],2))
edges.append(Edge(verticies[6],verticies[7],1))
edges.append(Edge(verticies[6],verticies[8],6))
edges.append(Edge(verticies[7],verticies[8],7))


#Add one vertex to the queue
q.append(verticies[0])
verticies[0].key = 0

#Run prims algorithm
prims()
print tree
print str(tree) == '[(a, 0, None), (b, 4, a), (h, 8, a), (g, 1, h), (f, 2, g), (c, 4, f), (i, 2, c), (d, 7, c), (e, 9, d)]'
