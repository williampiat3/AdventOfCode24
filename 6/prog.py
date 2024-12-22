import numpy as np
from collections import defaultdict
##1723
def turn_right(trajectory):
	rotation = np.array([[0,1],[-1,0]])
	return rotation@trajectory

def turn_left(trajectory):
	rotation = np.array([[0,-1],[1,0]])
	return rotation@trajectory

def translate_line(line):
	return list(map(int,[(carac=="#") for carac in line.replace("\n","")]))

def outside(position,data):
	return position[0]<0 or position[0]>(data.shape[0]-1) or position[1]< 0 or position[1]>(data.shape[1]-1)

def build_reverse_path(position,trajectory,data,directions):
	while True:
		new_position = position - trajectory
		if outside(new_position,data):
			break
		if data[*(new_position)]==1:
			break
		
		directions[tuple(new_position)].append(trajectory)

		potential_branch_pos = new_position +turn_left(trajectory)
		if outside(potential_branch_pos,data):
			pass
		else:
			if data[*(potential_branch_pos)]==1:
				build_reverse_path(new_position,turn_left(trajectory),data,directions)


		position=new_position

def check_if_loop(start,start_trajectory,data):
	position=np.copy(start)
	trajectory = np.copy(start_trajectory)
	history = []
	history_trajectory = []
	while True:
		history.append(np.copy(position))
		history_trajectory.append(np.copy(trajectory))
		new_position = position + trajectory
		if outside(new_position,data):
			return False
		if data[*new_position]==1:
			position =position
			trajectory=turn_right(trajectory)
		else:
			position = new_position

		for back_position,back_trajectory in zip(history,history_trajectory):
			if all([i==j for i,j in zip(position,back_position)]) and all([i==j for i,j in zip(trajectory,back_trajectory)]):
				return True




if __name__ == "__main__":
	data=[]
	with open("input","r") as file:
		for i,line in enumerate(file):
			data.append(translate_line(line))
			if "^" in line:
				position = [i,line.index("^")]
	data = np.array(data)

	traced_path = np.zeros_like(data)
	possible_blocks = np.zeros_like(data)
	position= np.array(position)
	start = np.copy(position)
	traced_path[*position]=1


	summed_possibilies=0
	trajectory = np.array([-1,0])
	count = 0
	while True:
		new_position = position + trajectory
		if outside(new_position,data):
			break
		if data[*new_position]==1:
			position =position
			trajectory=turn_right(trajectory)
		else:
			local_data = np.copy(data)
			local_data[*new_position]=1
			if traced_path[*new_position]==0:
				if check_if_loop(np.copy(position),np.copy(trajectory),local_data):
					possible_blocks[*new_position]=1
			position = new_position
			traced_path[*new_position]=1
			print(count)
		count +=1
		

		

	print("part 1:",np.sum(traced_path))
	# summed_possibilies=0
	# for point in directions:

	# 	possible_trajectories = directions[point]
	# 	if len(possible_trajectories)==1:
	# 		continue
	# 	for i in range(1,len(possible_trajectories)):
	# 		trajectory = possible_trajectories[i]
	# 		possible_direction = turn_right(trajectory)

	# 		possible_loops= [all(previous_direction==possible_direction) for previous_direction in possible_trajectories[:i]]
	# 		if any(possible_loops):
	# 			if not outside(point+trajectory,data):
	# 				possible_blocks[*(point+trajectory)]=1
	print("part 2:",np.sum(possible_blocks))



