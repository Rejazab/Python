from collections import deque

def getDistanceNodes(starterNode, endingNode, path=[]):
	nodes_path = {starterNode: [starterNode]}
	queue = deque()
	queue.append(starterNode)
	while len(queue):
	    node = queue.popleft()
	    for next_node in graph_nodes[node]:
	        if next_node not in nodes_path and next_node not in path:
	            nodes_path[next_node] = [nodes_path[node],next_node]
	            queue.append(next_node)

	tmp_list = nodes_path.get(endingNode) if nodes_path.get(endingNode) != None else []
    size = len(tmp_list)
    node = tmp_list[1] if len(tmp_list) > 1 else ''
    distance = 1
    return_i = 1
    while size == 2:
        next_list = tmp_list[0]
        return_i += 1
        #print('next_list %s'%next_list,file=sys.stderr)
        if type(next_list[0]) != str:
            if len(next_list[0]) != 2 :
                node = next_list[1]
                distance = return_i
        size = len(next_list[0]) if len(next_list) > 1 else len(next_list)
        tmp_list = next_list
    #print('node %s dist %s'%(node,distance),file=sys.stderr)
    return node, distance
