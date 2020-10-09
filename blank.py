cs35_notepad

Beej  1:39 PM
hash.py 
table = [None] * 8
​
class HashEntry:
	def __init__(self, key, value):
		self.key = key
Click to expand inline (51 lines)


:+1::skin-tone-3:
2
:+1::skin-tone-5:
1


Cody Morley  2:02 PM
https://developer.apple.com/documentation/swift/hashable
https://developer.apple.com/documentation/swift/hasher
https://medium.com/journey-of-one-thousand-apps/building-a-hash-data-structure-in-swift-e9b2733d9e20
I'll leave this here so the iOS students have a refresher on how to Hashable the everything. (edited) 
MediumMedium
Building A Hash Data Structure In Swift
Adventures In Data Structures
Reading time
9 min read
Jan 23rd, 2018 (194 kB)
https://miro.medium.com/max/838/1*h-2lpI8XEgxn_iCPULxJbg.png

1 reply
8 days agoView thread

Beej  2:03 PM
Slightly updated with bonus information
hash.py 
table = [None] * 8
​
class HashEntry:
	def __init__(self, key, value):
		self.key = key
Click to expand inline (58 lines)


:nice-text:
4



2 replies
Last reply 8 days agoView thread

leslie-rodriguez  3:11 PM
was added to #cs35_notepad by Leana.

Justin Andrade:lambda-staff-refresh:  3:13 PM
@channel Here is today's lecture recording! :arrow_right: https://youtu.be/4TXTLaQqu6s
YouTubeYouTube | Lambda School
CS35 - Hash Tables I w/ Beej Jorgensen 

:+1:
1
:ultrafastparrot:
1


Beej  2:05 PM
Pseudocode for GET, PUT, DELETE with chaining 
Slot
Index Chain (linked list)
----- -------------------------------
 0    -> HashEntry("qux",10) -> None
 1    -> HashEntry("plugh",20) -> HashEntry("foo",1) -> None
Click to expand inline (37 lines)


:thankyou7:
2
:+1:
1

2:06
Linked list example
llist.py 
class Node:
	def __init__(self, value):
		self.value = value
		self.next = None
Click to expand inline (97 lines)


2:06
Hash table load and rehash notes 
Hash table loading
------------------
load_factor = number_of_items_in_the_table / number_of_slots_in_array
Click to expand inline (62 lines)



Justin Andrade:lambda-staff-refresh:  3:36 PM
@channel Here is today's lecture recording :arrow_right: https://youtu.be/JFT8op8tvog
YouTubeYouTube | Lambda School
CS35 - Hash Tables II w/ Beej Jorgensen 

:a-team:
1
:thankyoukindly:
2


David Gansen  7:40 PM
was added to #cs35_notepad by Nick Flannery.

Beej  2:08 PM
Hash table application notes 
What Hash Table Solve
---------------------
* We need to look up some data quickly
    * Some data that was slow to generate or obtain
Click to expand inline (20 lines)


2:09
fib.py 
# 0 1 1 2 3 5 8 13 21 34 55 ...
#
# fib(0): 0
# fib(1): 1
# fib(n): fib(n-1) + fib(n-2)
Click to expand inline (26 lines)


2:09
sorter.py 
d = {
    "foo": 12,
    "bar": 17,
    "qux": 2
}
Click to expand inline (36 lines)


2:10
collisions.py 
import hashlib
import random
​
def hash_function(key):
    return int(hashlib.md5(str(key).encode()).hexdigest()[-8:], 16) & 0xffffffff
Click to expand inline (27 lines)


2:10
podcast.py 
def pod(total, podcasts):
    podcast_len = {}
​
    for p in podcasts:
        podcast_len[p] = True
Click to expand inline (30 lines)



Justin Andrade:lambda-staff-refresh:  3:37 PM
@channel Here is today's lecture recording! :arrow_right: https://youtu.be/FrCD85CrjxE
YouTubeYouTube | Lambda School
CS35 - Hash Tables III w/ Beej Jorgensen 

:fire:
2


Antonio MB  5:12 PM
@Beej could you please upload the file where we did the char count :thankyou7:


2 replies
Last reply 6 days agoView thread

Beej  5:16 PM
count.py 
def letter_count(s):
    d = {}
​
    for c in s:
        if not c.isalpha():
Click to expand inline (22 lines)



Gabe  3:59 PM
was added to #cs35_notepad by Patrick Gordon.

Justin Andrade:lambda-staff-refresh:  4:17 PM
@channel Here is today's lecture recording! :arrow_right: https://youtu.be/2O_DIQTiGok
YouTubeYouTube | Lambda School
CS35 - Hash Tables IV w/ Beej Jorgensen 

:fireball:
4


Beej  2:13 PM
Graphs notes 
Graphs
------
Nodes (also called "verts", "vertexes", "vertices") are connected by edges
Edges _may_ have numeric weights associated with them
* If not shown, assume all weights are 1 ("unweighted graph")
Edges can be directed (one way) or undirected (two way)
* If there are _only_ undirected edges, we call it an "undirected graph"
* Else we call it a "directed graph"
Cycle: we can traverse and get back to the starting node somehow
* If a graph has any cycles in it, we call it a "cyclic graph".
* Else it's an "acyclic graph".
Representation of graphs
------------------------
Which nodes are adjacent ("directly connected") to a particular node.
Adjacency matrix
* Big grid that has true/false values showing which nodes are adjacent
  * Or edge weights
Adjacency list (what we'll use)
A: {B, D}
B: {D, C}
C: {C, B}
D: {}
BFT
---
Init:
    Add the starting vert to the queue
While the queue is not empty:
    Pop current vert off queue
    If not visited:
        "Visit" the node
        Track it as visited
        Add all its neighbors (adjacent nodes) to the queue
Collapse



2:13
graph.py 
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
​
