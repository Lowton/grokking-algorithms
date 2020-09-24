graph = {}

graph['start'] = {}
graph['start']['mountain'] = 7
graph['start']['forest'] = 5
graph['start']['road'] = 3

graph['mountain'] = {}
graph['mountain']['bike'] = 2

graph['forest'] = {}
graph['forest']['river'] = 1
graph['forest']['bridge'] = 3

graph['road'] = {}
graph['road']['bridge'] = 1

graph['bridge'] = {}
graph['bridge']['river'] = 1
graph['bridge']['finish'] = 6

graph['river'] = {}
graph['river']['bike'] = 3

graph['bike'] = {}
graph['bike']['finish'] = 2

graph['finish'] = {}

infinity = float('inf')
costs = {}
costs['mountain'] = 7
costs['forest'] = 5
costs['road'] = 2
costs['bike'] = infinity
costs['river'] = infinity
costs['bridge'] = infinity
costs['finish'] = infinity

parent = {}
parent['mountain'] = 'start'
parent['forest'] = 'start'
parent['road'] = 'start'
parent['bike'] = None
parent['river'] = None
parent['bridge'] = None
parent['finish'] = None

processed = []

def findLowestCostNode(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node
            
node = findLowestCostNode(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parent[n] = node
    processed.append(node)
    node = findLowestCostNode(costs)

def shortestRoute(node):
    route = ''
    while node != 'start':
        route = f'-> {node}[{costs[node]}] {route}'
        node = parent[node]
    return f'start {route}'

def printShortestRoute(node):
    print(f'Shortest route to {node} is {shortestRoute(node)}. It takes {costs[node]} hours.')
    
printShortestRoute('finish')
printShortestRoute('river')
printShortestRoute('bike')
