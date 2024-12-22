import numpy as np
import random
from itertools import combinations
from collections import defaultdict


if __name__ == "__main__":
	data = []
	nodes=defaultdict(list)
	with open("test","r")as file:
		for line in file:
			data = list(map(int,line.replace("\n","")))

	## Part 1
	memory = np.array(sum([size*[index//2] if index%2==0 else size*[-1] for index,size in enumerate(data) ],start=[]))
	free_space_mask =(memory==-1)
	size_empty_mem = np.sum(free_space_mask.astype(int))
	accumulated_place=np.cumsum(free_space_mask.astype(int))
	accumulated_data=np.cumsum((~free_space_mask).astype(int))
	memory_data = memory[~free_space_mask]
	size_data = len(memory_data)

	data_to_be_replaced = accumulated_place[size_data]

	memory_data = memory[~free_space_mask][range(-1,-data_to_be_replaced-1,-1)]
	memory[free_space_mask*(accumulated_place<=data_to_be_replaced)]= memory_data
	memory[size_data:]=0
	print("part 1:",np.sum(memory*np.arange(0,memory.shape[0])))

	## Part 2
	free_spaces_sizes = data[1::2]
	data_sizes = np.array(data[0::2])
	data_indexes = np.arange(0,len(data_sizes))
	index_done = np.ones_like(data_sizes).astype(int)
	transport_map =defaultdict(list)
	limit=0
	for index_free,free_space in enumerate(free_spaces_sizes):
		remaining_space=free_space
		for index,size in zip(data_indexes[index_done*(data_sizes<limit)],data_sizes[index_done*(data_sizes<limit)]):
			if size <= remaining_space:
				remaining_space -= size
				transport_map[index_free].append(index)
				index_done[index]=0
			if remaining_space==0:
				break
		free_spaces_sizes[index_free]=remaining_space
		if remaining_space!=0:
			limit=remaining_space


	memory=[]
	for index,size in enumerate(data):
		if index%2==0:
			if index_done[index//2]==0:
				memory.extend([-1]*size)
			else:
				memory.extend(size*[index//2])
		else:
			if (index//2) in transport_map:
				for transported in transport_map[index//2]:
					memory.extend(data_sizes[transported]*[transported])
				if free_spaces_sizes[index//2]!=0:
					memory.extend([-1]*free_spaces_sizes[index//2])

			else:
				memory.extend([-1]*size)
	memory = np.array(memory)
	memory[memory==-1]=0
	print("part 2:",np.sum(memory*np.arange(0,memory.shape[0])))















