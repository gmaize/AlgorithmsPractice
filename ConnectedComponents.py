#Kosaraju's O(V + E) linear time algorithm for partitioning
#the strongly connected components in a graph (V, E)

import Queue

#V = [v, u, ...], E={v:[u, ...], ...}
#V is complete list of vertices in G
#Vertices with no outgoing edges are either not present in E, or have [] as its value
def getStronglyConnectedComponents(V, E):
	reversedEdges = getTranspose(E)
	#get stack of vertices in order of decreasing finishing times in G'(V, E')
	finishedStack = getFinishedStack(V, reversedEdges)
	
	#DFS vertices in G(V, E) in order of decreasing finishing times in G'
	components = []
	alreadyVisited = set()
	while 0 < len(finishedStack):
		v = finishedStack.pop()
		if v in alreadyVisited:
			continue
		#at this point, non-visited reachable nodes from v are in the same scc
		curSCC = getReachableVerticesBFS(E, v, alreadyVisited, [])
		components.append(curSCC)
	return components

#Reverse edges in E
def getTranspose(E):
	reversedEdges = {}
	for v in E:
		if v not in E:
			continue
		for u in E[v]:
			if u not in reversedEdges:
				reversedEdges[u] = set()
			reversedEdges[u].add(v)
	return reversedEdges

#Returns stack of vertices in V, in order of decreasing finishing times,
#with the last finished vertex on top
def getFinishedStack(V, E, finishedStack=[], alreadyVisited = set()):
	for v in V:
		__getFinishedStack(v, E, finishedStack, alreadyVisited)
	return finishedStack

def __getFinishedStack(v, E, finishedStack, alreadyVisited):
	if v in alreadyVisited:
		return
	alreadyVisited.add(v)
	if v in E:
		for u in E[v]:
			__getFinishedStack(u, E, finishedStack, alreadyVisited)
	finishedStack.append(v)

#Returns True iff there exists a path from source to dest
def pathExists(E, source, dest):
	visited = set()
	queue = Queue.Queue(maxsize=-1)
	queue.put(source)
	while not queue.empty():
		v = queue.get()
		visited.add(v)
		if v not in E:
			continue
		for u in E[v]:
			if u == dest:
				return True
			if u in visited:
				continue
			queue.put(u)
	return False

#Returns set of vertices in E that are reachable from vertex v
def getReachableVerticesDFS(E, source, alreadyVisited, reachable):
	if source in alreadyVisited:
		return reachable
	alreadyVisited.add(source)
	reachable.append(source)
	for u in E[source]:
		getReachableVerticesDFS(E, u, alreadyVisited, reachable)
	return reachable

#Returns set of vertices in E that are reachable from source vertex
def getReachableVerticesBFS(E, source, alreadyVisited, reachable):
	queue = Queue.Queue(maxsize=-1)
	queue.put(source)
	while not queue.empty():
		v = queue.get()
		alreadyVisited.add(v)
		reachable.append(v)
		if v not in E:
			continue
		for u in E[v]:
			if u not in alreadyVisited:
				queue.put(u)
	return reachable

