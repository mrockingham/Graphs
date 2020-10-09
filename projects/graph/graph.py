"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:
	def __init__(self):
		self.vertices = {}    # keys are all verts in the graph, values are sets of adj verts
​
	def add_vertex(self, vertex):
		"""Add a new unconnected vert"""
		self.vertices[vertex] = set()
​
	def add_edge(self, v_from, v_to):
		if v_from in self.vertices and v_to in self.vertices:
			self.vertices[v_from].add(v_to)
		else:
			raise IndexError("nonexistent vertex")
​
	def is_connected(self, v_from, v_to):
		if v_from in self.vertices and v_to in self.vertices:
			return v_to in self.vertices[v_from]
		else:
			raise IndexError("nonexistent vertex")
​
	def get_neighbors(self, v):
		return self.vertices[v]
​
	def bft(self, starting_vertex_id):
		q = Queue()
		visited = set()
​
		# Init:
		q.enqueue(starting_vertex_id)
​
		# While queue isn't empty
		while q.size() > 0:
​
			v = q.dequeue()
​
			if v not in visited:
				print(v)   # "Visit" the node
​
				visited.add(v)
​
				for neighbor in self.get_neighbors(v):
					q.enqueue(neighbor)
​
	def dft(self, starting_vertex_id):
		q = Stack()
		visited = set()
​
		# Init:
		q.push(starting_vertex_id)
​
		# While queue isn't empty
		while q.size() > 0:
​
			v = q.pop()
​
			if v not in visited:
				print(v)   # "Visit" the node
​
				visited.add(v)
​
				for neighbor in self.get_neighbors(v):
					q.push(neighbor)
​
	def bfs(self, starting_vertex_id, target_vertex_id):
		# Create an empty queue and enqueue A PATH TO the starting vertex ID
		# Create a Set to store visited vertices
		# While the queue is not empty...
			# Dequeue the first PATH
			# Grab the last vertex from the PATH
			# If that vertex has not been visited...
				# CHECK IF IT'S THE TARGET
				  # IF SO, RETURN PATH
				# Mark it as visited...
				# Then add A PATH TO its neighbors to the back of the queue
				  # COPY THE PATH
				  # APPEND THE NEIGHOR TO THE BACK
​
​
​
g = Graph()
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
​
g.add_edge(2, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
​
print(g.vertices)
​
g.bft(3)
Collapse




Justin Andrade:lambda-staff-refresh:  3:21 PM
@channel Here is today's lecture recording! :arrow_right:  https://youtu.be/hST_X7eFWSQ
YouTubeYouTube | Lambda School
CS35 - Graphs I w/ Beej Jorgensen 


Beej  12:55 PM
graph.py with DFS recursive 
# Stack and Queue are in util.py
​
class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)
​
class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)
​
class Graph:
	def __init__(self):
		self.vertices = {}    # keys are all verts in the graph, values are sets of adj verts
​
	def add_vertex(self, vertex):
		"""Add a new unconnected vert"""
		self.vertices[vertex] = set()
​
	def add_edge(self, v_from, v_to):
		if v_from in self.vertices and v_to in self.vertices:
			self.vertices[v_from].add(v_to)
		else:
			raise IndexError("nonexistent vertex")
​
	def is_connected(self, v_from, v_to):
		if v_from in self.vertices and v_to in self.vertices:
			return v_to in self.vertices[v_from]
		else:
			raise IndexError("nonexistent vertex")
​
	def get_neighbors(self, v):
		return self.vertices[v]
​
	def bft(self, starting_vertex_id):
		q = Queue()
		visited = set()
​
		# Init:
		q.enqueue(starting_vertex_id)
​
		# While queue isn't empty
		while q.size() > 0:
​
			v = q.dequeue()
​
			if v not in visited:
				print(v)   # "Visit" the node
​
				visited.add(v)
​
				for neighbor in self.get_neighbors(v):
					q.enqueue(neighbor)
​
	def dft(self, starting_vertex_id):
		q = Stack()
		visited = set()
​
		# Init:
		q.push(starting_vertex_id)
​
		# While queue isn't empty
		while q.size() > 0:
​
			v = q.pop()
​
			if v not in visited:
				print(v)   # "Visit" the node
​
				visited.add(v)
​
				for neighbor in self.get_neighbors(v):
					q.push(neighbor)
​
	def bfs(self, starting_vertex_id, target_vertex_id):
		q = Queue()
		visited = set()
​
		# Init:
		q.enqueue([starting_vertex_id])
​
		# While the queue isn't empty
		while q.size() > 0:
​
			path = q.dequeue()
​
			#end_of_path_node = path[-1]
			v = path[-1]
​
			if v not in visited:
​
				if v == target_vertex_id:
					return path  # Found it!
​
				visited.add(v)
​
				for neighbor in self.get_neighbors(v):
					new_path = path + [neighbor]
					q.enqueue(new_path)
​
		return None
​
	def dft_recursive(self, starting_vertex, visited=None):
​
		if visited is None:
			visited = set()
​
		print(starting_vertex)
		visited.add(starting_vertex)
​
		for neighbor in self.get_neighbors(starting_vertex):
			if neighbor not in visited:
				self.dft_recursive(neighbor, visited)
​
​
	def dfs_recursive(self, starting_vertex, target_vertex, visited=None, path=None):
​
		if visited is None:
			visited = set()
​
		if path is None:
			path = [starting_vertex]
​
		print(starting_vertex)
		visited.add(starting_vertex)
​
		for neighbor in self.get_neighbors(starting_vertex):
			if neighbor not in visited:
​
				new_path = path + [neighbor]
				if neighbor == target_vertex:
					return new_path
​
				dfs_path = self.dfs_recursive(neighbor, target_vertex, visited, new_path)
				if dfs_path is not None:
					return dfs_path
​
		return None
​
g = Graph()
g.add_vertex('A')
g.add_vertex('y')
g.add_vertex('x')
g.add_vertex('z')
​
g.add_edge('A', 'x')
g.add_edge('x', 'A')
g.add_edge('A', 'y')
g.add_edge('y', 'z')
g.add_edge('z', 'x')
​
print(g.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
