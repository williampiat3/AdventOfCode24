import numpy as np
import random
from itertools import combinations
from collections import defaultdict

def outside(position,data):
	return position[0]<0 or position[0]>(len(data)-1) or position[1]< 0 or position[1]>(len(data[0])-1)

if __name__ == "__main__":
	data = []
	nodes=defaultdict(list)
	with open("input","r")as file:

		for i,line in enumerate(file):
			real_line = line.replace("\n","")
			data.append(real_line)
			for j in range(len(real_line)):
				if real_line[j]!=".":
					nodes[real_line[j]].append(np.array([i,j]))


	antinodes_map = np.zeros((len(data),len(data[0])))
	for node in nodes:
		positions_list = nodes[node]
		if len(positions_list)==1:
			continue
		else:
			for pos1,pos2 in combinations(positions_list,2):
				vector = pos1-pos2
				antinode_pos = pos1 + vector
				if not outside(antinode_pos,data):
					antinodes_map[*antinode_pos]=1
				antinode_pos = pos2 - vector
				if not outside(antinode_pos,data):
					antinodes_map[*antinode_pos]=1
	print("part1:",np.sum(antinodes_map))


	antinodes_map = np.zeros((len(data),len(data[0])))
	for node in nodes:
		positions_list = nodes[node]
		if len(positions_list)==1:
			continue
		else:
			for pos1,pos2 in combinations(positions_list,2):
				vector = pos1-pos2
				harmonic =0
				while True:
					antinode_pos = pos1 + harmonic*vector
					if not outside(antinode_pos,data):
						antinodes_map[*antinode_pos]=1
						harmonic +=1
					else:
						break
				harmonic =0
				while True:
					antinode_pos = pos2 - harmonic*vector
					if not outside(antinode_pos,data):
						antinodes_map[*antinode_pos]=1
						harmonic +=1
					else:
						break
	print("part2:",np.sum(antinodes_map))