import numpy as np

def outside(i,j,data):
	return (i<0 or j<0 or i>=len(data) or j>=len(data[0]))

def compute_graph(data):
	adjacency= np.zeros((len(data)*len(data[0]),len(data)*len(data[0])))
	for i in range(len(data)):
		for j in range(len(data[0])):
			for (di,dj) in [[0,1],[1,0]]:
				if outside(i+di,j+dj,data):
					continue
				if data[i][j]==data[di+i][dj+j]:
					adjacency[i*len(data[0])+j,(i+di)*len(data[0])+j+dj]=1
					adjacency[(i+di)*len(data[0])+j+dj,i*len(data[0])+j]=1
	return adjacency

def compute_borders_and_areas(k,adjacency,done_node,borders,areas):
	if k in done_node:
		return
	else:
		borders.append(4 - sum(adjacency[k]))
		areas.append(1)
		done_node.append(k)
		for new_k in [index for index,l in enumerate(adjacency[k]) if l==1]:
			compute_borders_and_areas(new_k,adjacency,done_node,borders,areas)
	return sum(areas)*(sum(borders)-sum(areas))


def compute_borders_and_areas2(k,adjacency,done_node,borders,areas,border_points):
	if k in done_node:
		return
	else:
		number_of_borders= 4 - sum(adjacency[k])
		borders.append(number_of_borders)
		areas.append(1)
		done_node.append(k)
		if number_of_borders!=0:
			border_points.append(k)

		for new_k in [index for index,l in enumerate(adjacency[k]) if l==1]:
			compute_borders_and_areas2(new_k,adjacency,done_node,borders,areas,border_points)
	start_point = border_points[0]
	current_point = start_point
	done_points =[]
	current_vector =0
	while True:
		picked_neighbor = [index for index,l in enumerate(adjacency[curent_point]) if l==1 and index in border_points and index not in done_points][0]
		current_vector

	return sum(areas)*sum(borders)


def dikstra(adjacency):
	done_node = []
	total_cost=0
	for k in range(adjacency.shape[0]):
		if k not in done_node:
			local_nodes=[]
			borders = []
			areas =[]
			border_points=[]
			total_cost+= compute_borders_and_areas(k,adjacency,done_node,borders,areas)
	return total_cost



if __name__ == "__main__":
	data=[]
	with open("input","r") as file:
		for line in file:
			data.append(line.replace('\n',''))
	adjacency = compute_graph(data)
	print(dikstra(adjacency))


