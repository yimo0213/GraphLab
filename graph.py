import random
from tqdm import tqdm
from collections import deque
import matplotlib.pyplot as plot
from matplotlib import pyplot as plt

#Undirected graph using an adjacency list
class Graph:

    def __init__(self, n):
        self.adj = {}
        self.len = n
        for i in range(n):
            self.adj[i] = []

    def are_connected(self, node1, node2):
        return node2 in self.adj[node1]

    def adjacent_nodes(self, node):
        return self.adj[node]

    def add_node(self):
        self.adj[len(self.adj)] = []
        self.len += 1

    def add_edge(self, node1, node2):
        if node1 not in self.adj[node2]:
            self.adj[node1].append(node2)
            self.adj[node2].append(node1)

    def number_of_nodes(self):
        return self.len



#Breadth First Search
def BFS(G, node1, node2):
    Q = deque([node1])
    marked = {node1 : True}
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if node == node2:
                return True
            if not marked[node]:
                Q.append(node)
                marked[node] = True
    return False

#BFS return a list
def BFS2(g, node1, node2):
    q = deque([node1])
    marked = {node1:True}
    track_dict = {}
    for node in g.adj:
        if node != node1:
            marked[node] = False
    while len(q) != 0:
        current_node = q.popleft()
        for node in g.adj[current_node]:
            if not marked[node]:
                track_dict[node] = current_node
            if node == node2:
                result = []
                rstNode = node2
                while rstNode != node1:
                    result.append(track_dict[rstNode])
                    rstNode = track_dict[rstNode]

                return (result[::-1] + [node2])
            if not marked[node]:
                q.append(node)
                marked[node] = True
    return []

def BFS3(g, node1):
    q = deque([node1])
    marked = {node1:True}
    track_dict = {}
    for node in g.adj:
        if node != node1:
            marked[node] = False
    while len(q) != 0:
        current_node = q.popleft()
        for node in g.adj[current_node]:
            if not marked[node]:
                track_dict[node] = current_node
                q.append(node)
                marked[node] = True
    return track_dict






#Depth First Search
def DFS(G, node1, node2):
    S = [node1]
    marked = {}
    for node in G.adj:
        marked[node] = False
    while len(S) != 0:
        current_node = S.pop()
        if not marked[current_node]:
            marked[current_node] = True
            for node in G.adj[current_node]:
                if node == node2:
                    return True
                S.append(node)
    return False


#DFS which returns a list
def DFS2(g, node1, node2):
    s = [node1]
    result = []
    marked = {}
    for node in g.adj:
        marked[node] = False
    count = 0
    while len(s) != 0:
        current_node = s.pop()
        result.append(current_node)
        if not marked[current_node]:
            marked[current_node] = True
            for node in g.adj[current_node]:
                if node == node2:
                    result.append(node)
                    return result
                s.append(node)
            count += 1
        else:
            result = result[0:len(result) - count]
            count = len(result) - count
    return []




def DFS3(g, node1):
    s = [node1]
    result = {}
    marked = {}
    for node in g.adj:
        marked[node] = False
    while len(s) != 0:
        current_node = s.pop()
        if not marked[current_node] or current_node == node1:
            marked[current_node] = True
            for node in g.adj[current_node]:
                s.append(node)
            print(str(node) + ":" + str(current_node) )
            if not marked[node] or current_node == node1:
                result[node] = current_node
    return result


def has_cycle(g):
    nodes = list(g.adj)
    marked = []
    while(nodes != []):
        ls = list(BFS3(g,nodes[0])).append(nodes[0]) #each connected component
        sum = 0
        for key in g.adj.keys:
            if key in ls:
                for l in g.adj[key]:
                    if l in ls:
                        sum += 1





#Use the methods below to determine minimum vertex covers


def add_to_each(sets, element):
    copy = sets.copy()
    for set in copy:
        set.append(element)
    return copy


def power_set(set):
    if set == []:
        return [[]]
    return power_set(set[1:]) + add_to_each(power_set(set[1:]), set[0])


def is_vertex_cover(G, C):
    for start in G.adj:
        for end in G.adj[start]:
            if not(start in C or end in C):
                return False
    return True


def MVC(G):
    nodes = [i for i in range(G.get_size())]
    subsets = power_set(nodes)
    min_cover = nodes
    for subset in subsets:
        if is_vertex_cover(G, subset):
            if len(subset) < len(min_cover):
                min_cover = subset
    return min_cover



def randGraph(node, edge):
    g = Graph(node)
    if(edge > node * (node-1)/2):
        edge = int(node * (node -1) /2)
        print("out of range, take the maximum")
    for i in range(edge):
        rStart = random.randint(0, node-1)
        rEnd = random.randint(0, node-1)
        while(rStart == rEnd or g.are_connected(rStart,rEnd)):
            rStart = random.randint(0, node - 1)
            rEnd = random.randint(0, node - 1)
        g.add_edge(rStart,rEnd)
    return g

def is_connected(g):
    nodes = list(g.adj.keys())
    return len(list(BFS3(g,0).keys())) == len(nodes)-1



def experiment2(node,edge):
    pconnect = []
    k = 1000
    for i in range(node,edge):
        connect = 0
        for m in range(k):
            g = randGraph(node,i)
            if is_connected(g):
                connect += 1
        pconnect.append(connect/k)
    plot.plot(range(node,edge),pconnect)
    plot.show()
