import numpy as np
import random
from itertools import product

def add(x,y):
	return x+y

def mul(x,y):
	return x*y
def cat(x,y):
	return int(str(x)+str(y))

def build_expr(sequence,operations,seed=None):
	if not seed:
		seed = operations[0]+f"({sequence[0]},{sequence[1]})"
		if len(sequence)==2:
			return seed
		else:
			return build_expr(sequence[2:],operations[1:],seed=seed)

	else:
		if len(sequence)==1:
			return operations[0]+f"({seed},{sequence[0]})"
		else:
			return build_expr(sequence[1:],operations[1:],seed=operations[0]+f"({seed},{sequence[0]})")

def pick_all_combs(sequence,operations=["mul","add"]):
	return product(operations,repeat=len(sequence)-1)

	
def pick_random_ops(sequence):
	return [random.choice(["mul","add"]) for _ in sequence[1:]]

def compute_sequence(sequence,operations=["mul","add"]):
	operations = pick_all_combs(sequence,operations=operations)
	arithms = list(map(lambda x: eval(build_expr(sequence,x)),operations))
	return arithms


if __name__ == "__main__":
	sequences = []
	results = []
	with open("input","r")as file:
		for line in file:
			result, seq = line.replace("\n","").split(": ")
			results.append(int(result))
			sequences.append(list(map(int,seq.split(" "))))

	print("step 1:",sum([result for sequence,result in zip(sequences,results) if  result in  compute_sequence(sequence)]))


	print("step 2:",sum([result for sequence,result in zip(sequences,results) if  result in  compute_sequence(sequence,operations=["mul","add","cat"])]))
	



