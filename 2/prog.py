import numpy as np
from collections import defaultdict

def check_if_safe(scene,first=True):
	grads = np.convolve(scene,np.array([1,-1]),mode="valid")
	if (all(np.sign(grads)==1) or all(np.sign(grads)==-1)) and all(np.abs(grads)>0) and all(np.abs(grads)<4):
		return 1
	elif first:
		return int(any(list(map(lambda x: check_if_safe(x,first=False),[np.delete(scene,[i]) for i in range(scene.shape[0])]))))

	else:
		return 0


if __name__ == "__main__":
	with open("input","r") as file:
		data = [np.array(list(map(int,line.replace("\n","").split(" ")))) for line in file]

	valid = list(map(lambda x: check_if_safe(x,first=False),data))
	print("valids part one :",  sum(valid))

	valid = list(map(lambda x: check_if_safe(x,first=True),data))
	print("valids part true :",  sum(valid))


		


