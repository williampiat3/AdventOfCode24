import numpy as np
from collections import defaultdict



def roll_out_number(number):
	caracters=str(number)
	if len(caracters)%2==0:
		return [int(caracters[:len(caracters)//2]),int(caracters[len(caracters)//2:])]
	elif number ==0:
		return [1]
	else:
		return [2024*number]
def exec_rollouts(numbers,depth,verbose=False):
	local_numbers = numbers
	for _ in range(depth):
		local_numbers = sum(list(map(roll_out_number,local_numbers)),start=[])
		if verbose:
			print(local_numbers)
	return local_numbers

def build_readout_table(value,depth):
	readout_table=[]
	current_numbers =[value]
	readout_table.append(current_numbers)
	for i in range(1,depth+1):
		current_numbers = exec_rollouts(current_numbers,1)
		readout_table.append(current_numbers)
	return readout_table

def roll_out_zero(depth,rollout_table):
	return rollout_table[depth]

def update_time_machine(time_machine):
	new_time_machine=defaultdict(list)
	for i in time_machine:
		if i<=0:
			continue
		else:
			new_time_machine[i-1]=time_machine[i]
	return new_time_machine

def exec_rollouts_skip(numbers,depth,rollout_table):
	local_numbers=numbers
	local_count=0
	time_machine=defaultdict(list)
	for i in range(depth):

		for number in local_numbers:
			if number not in rollout_table:
				rollout_table[number]= build_readout_table(number,min(25,depth-i-1))
		# count_zeros = local_numbers.count(0)
		# local_numbers = sum(list(map(roll_out_number,[number for number in local_numbers if number not in rollout_table])),start=[])
		# # handle 0s
		# # print(depth-i-1)
		new_local_numbers =[]
		for number in local_numbers:
			leap = min(len(rollout_table[number])-2,depth-i-1)
			if leap<0:
				new_local_numbers.extend(roll_out_number(number))
			else:
				time_machine[leap].extend(rollout_table[number][leap+1])
		# print(new_local_numbers)
		new_local_numbers.extend(time_machine[0])
		local_numbers = new_local_numbers
		
		time_machine = update_time_machine(time_machine)
		# print(time_machine)

	return local_numbers



		


if __name__ == "__main__":
	readout_table={}

	with open("input","r") as file:
		for line in file:
			data = list(map(int,line.replace("\n","").split(" ")))
			break
	roll_out_table={}
	roll_out_table[0] = build_readout_table(0,25)
	print("table built")
	# print(roll_out_table)
	print(len(exec_rollouts_skip(data,depth=75,rollout_table=roll_out_table)))
	# print("___REAL____")
	# print(len(exec_rollouts(data,depth=25,verbose=False)))
	# exec_rollouts([0],depth=25)
