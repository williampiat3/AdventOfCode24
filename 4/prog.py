from itertools import product

if __name__ == '__main__':
	with open("input","r") as file:
		data = [line for line in file]

	def search_around_point(i,j,data,depth=0):
		targets=["M","A","S"]
		count=0
		for di,dj in product([-1,0,1],repeat=2):
			if (di==0 and dj==0) or (i+di)<0 or (j+dj)<0 or (i+di)>=len(data) or (j+dj)>len(data[j]):
				continue
			if data[di+i][dj+j]==targets[depth]:
				if targets[depth]=="S":
					count += 1
					continue
				else:
					count += search_around_point(i+di,j+dj,data,depth+1)
					continue
		return count

	def search_around_point2(i,j,data):
		targets=["M","A","S"]
		count=0
		for di,dj in product([-1,0,1],repeat=2):
			depth=1
			
			while True:
				if (di==0 and dj==0) or (i+di*depth)<0 or (j+dj*depth)<0 or (i+di*depth)>=len(data) or (j+dj*depth)>len(data[j]):
					break
				if data[di*depth+i][dj*depth+j]==targets[depth-1]:
					if targets[depth-1]=="S":
						count+=1
						break
					else:
						depth+=1
						continue
				else:
					break
		return count
	def search_around_point3(i,j,data):
		available = ['M','S']

		for di,dj in [[1,1],[1,-1]]:
			if (i+di)<0 or (j+dj)<0 or (i+di)>=len(data) or (j+dj)>len(data[j]) or (i-di)<0 or (j-dj)<0 or (i-di)>=len(data) or (j-dj)>len(data[j]):
				return 0
			if not (data[di+i][dj+j] in available and data[-di+i][-dj+j] in available and data[di+i][dj+j] != data[-di+i][-dj+j]):
				return 0
		return 1


			
	summed_values = 0
	results=[]
	for i in range(len(data)):
		for j in range(len(data[0])):
			letter = data[i][j]
			if letter=="X":
				results.append(search_around_point2(i,j,data))
			else:
				results.append(0)
	print("part1:",sum(results))
	results=[]
	for i in range(len(data)):
		for j in range(len(data[0])):
			letter = data[i][j]
			if letter=="A":
				results.append(search_around_point3(i,j,data))
			else:
				results.append(0)
	print("part1:",sum(results))