import random
import ConnectedComponents

def test(V, E):
	#for each component check to see that every node contains a path to every other node
	#for each component check to see that there is no path to and from every other component
	components = ConnectedComponents.getStronglyConnectedComponents(V, E)
	first = None
	second = None
	for component in components:
		print(component)
		if first is None:
			first = component[0]
		elif second is None:
			second = component[0]
		for i in xrange(0, len(component)-1):
			member1 = component[i]
			member2 = component[i+1]
			isPath = ConnectedComponents.pathExists(E, member1, member2)
			print("Path from " + str(member1) + " to " + str(member2) + ": " + str(isPath))
		if len(component) > 1:
			member1 = component[0]
			member2 = component[len(component)-1]
			isPath = ConnectedComponents.pathExists(E, member2, member1)
			print("Path from " + str(member2) + " to " + str(member1) + ": " + str(isPath))

			isPath1 = ConnectedComponents.pathExists(E, first, second)
			isPath2 = ConnectedComponents.pathExists(E, second, first)
			connected = isPath1 and isPath2
			print("Path from " + str(first) + " to " + str(second) + " and back?: " + str(connected))
			print("")
			first = None
			second = None
	for v in E:
		print(str(v) + ": "+str(E[v]))


if __name__ == '__main__':
	#random graph
	V = list(range(0, 10))
	items = [(v, float('inf')) for v in V]
	E = {}
	for v in V:
		E[v] = []
		potentialDests = [dest for dest in V if dest != v]
		numEdges = int(random.random()*len(V)//4)
			#for i in xrange(0, numEdges):
			#j = int(random.random() * len(potentialDests))
			#u = potentialDests.pop(j)
			#E[v].append(u)
	magic = 4
	for i in xrange(0, len(V) - 1):
		remainder = (i + 1) % magic
		dest = None
		if remainder == 3:
			E[i] = [i - magic + 2, i + 1]
		else:
			E[i] = [i + 1]
	test(V, E)
