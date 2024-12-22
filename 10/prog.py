import numpy as np
import random
from itertools import combinations
from collections import defaultdict

def outside(i,j,data):
	return (i<0 or j<0 or i>=len(data) or j>=len(data[0]))


def search_around_point(i,j,data,map_summit,heigth=0):
	
	count=0
	for di,dj in [[0,1],[0,-1],[1,0],[-1,0]]:
		if outside(i+di,j+dj,data):
			continue
		if data[di+i][dj+j]==(heigth+1):

			if (heigth+1)==9:
				map_summit[di+i,dj+j]=1
				continue
			else:
				search_around_point(i+di,j+dj,data,map_summit,heigth+1)
				continue
	return count


def search_around_point2(i,j,data,heigth=0):
	
	count=0
	for di,dj in [[0,1],[0,-1],[1,0],[-1,0]]:
		if outside(i+di,j+dj,data):
			continue
		if data[di+i][dj+j]==(heigth+1):

			if (heigth+1)==9:
				count+=1
				continue
			else:
				count += search_around_point2(i+di,j+dj,data,heigth+1)
				continue
	return count

if __name__ == "__main__":
	with open("input","r") as file:
		data = [list(map(int,line.replace('\n',''))) for line in file]
	count=np.zeros_like(np.array(data))
	for i in range(len(data)):
		for j in range(len(data[0])):
			if data[i][j]==0:
				map_summit = np.zeros((len(data),len(data[0])))
				search_around_point(i,j,data,map_summit,heigth=0)
				count[i,j]=np.sum(map_summit)

	print("part 1:",np.sum(count))

	count=np.zeros_like(np.array(data))
	for i in range(len(data)):
		for j in range(len(data[0])):
			if data[i][j]==0:
				count[i,j]=search_around_point2(i,j,data)

	print("part 2:",np.sum(count))
