import numpy as np
from collections import defaultdict



if __name__ == "__main__":
	with open("input","r") as file:
		number1,number2 = zip(*[map(int,line.replace("\n","").split("   ")) for line in file])

	counts=defaultdict(int)
	for i in set(number2):
		counts[i]=number2.count(i)


	print("score 1",np.sum(np.abs(np.array(sorted(number1))-np.array(sorted(number2)))))

	print("score 2",sum([counts[i]*i for i in number1]))


	
