import networkx as nx
import matplotlib.pyplot as plt


def getOptions(train, map):
	options=list()
	points=map.edges()
	lines={v:k for k, v in nx.get_edge_attributes(map, "idx").items()}
	length=nx.get_edge_attributes(map, "weight")
	if train["position"]!=0 and train["position"]!=length[train["line_idx"]]:
		options=lines[train["line_idx"]]
	elif train["position"]==0:
		for i in points:
			if lines[train["line_idx"]][0]==i[0]:
				options.append(i[1])
			elif lines[train["line_idx"]][0]==i[1]:
				options.append(i[0])
	else:
		for i in points:
			if lines[train["line_idx"]][1]==i[0]:
				options.append(i[1])
			elif lines[train["line_idx"]][1]==i[1]:
				options.append(i[0])
				
	return options
	
	


def parseMap(jsonData):
	graph=nx.Graph()
	graph.add_nodes_from([i['idx'] for i in jsonData['points']])
	graph.add_weighted_edges_from([(i['points'][0], i['points'][1], i['length']) for i in jsonData['lines']])
	valList=dict()
	for i in jsonData["lines"]:
		valList[tuple(i["points"])]=i["idx"]
	nx.set_edge_attributes(graph, valList, "idx")
	pos=nx.spring_layout(graph)
	pos=nx.kamada_kawai_layout(graph, pos=pos)
	valList=dict()
	for i in jsonData["points"]:
		valList[i["idx"]]=pos[i["idx"]]
	nx.set_node_attributes(graph, valList, "pos")
	return graph
	
	
def parseTrains(trains, map):
	graph=nx.Graph()
	lines={v:k for k, v in nx.get_edge_attributes(map, "idx").items()}
	length=nx.get_edge_attributes(map, "weight")
	goodstype={1:"armor", 2:"products", None:"Empty"}
	buttons=list()
	for i in trains:
		string="Index:"+str(i["idx"])+"\nGoods:"+str(goodstype[i["goods_type"]])
		if i["goods_type"]!=None:
			string+=' '+str(i["goods"])
		buttons.append(string)
	print(buttons)
	trains=[x for x in trains if x["position"]!=0 and x["position"]!=length[x["line_idx"]]]
	pos=nx.get_node_attributes(map, "pos")
	if trains:
		vec=[pos[lines[i["line_idx"]][1]]-pos[lines[i["line_idx"]][0]] for i in trains]
		for i in trains:
			trainPos={i["idx"]:[pos[lines[i["line_idx"]][0]]+x/length[tuple(lines[i["line_idx"]])]*i["position"] for x in vec]}
		for i in trains:
			trainPos[i["idx"]]=list(trainPos[i["idx"]][0])
		for i in trains:
			graph.add_node(i["idx"], pos=trainPos[i["idx"]])
		print('buttons')	
		print(buttons)
		return graph, buttons
	else:
		return 0, buttons
	
def drawTrains(trains):
	pos=nx.get_node_attributes(trains, "pos")
	nx.draw(trains, pos, node_color="blue", node_size=100)
	
def drawMap(map):
	pos=nx.get_node_attributes(map, "pos")
	labels = nx.get_edge_attributes(map, 'weight')
	nodeSize = 200
	nx.draw(map, pos, with_labels=True, nodecolor='r', edge_color='b', node_size=nodeSize, font_size=8)
	nx.draw_networkx_edge_labels(map, pos, edge_labels=labels)
	
	