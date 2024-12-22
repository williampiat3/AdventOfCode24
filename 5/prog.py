from collections import defaultdict

def check_if_not_valid(index,sequence):
	carac = sequence[index]
	return(index!=0 and any([(bfr in forbidden_before[carac]) for bfr in print_sequence[:index]])) or (index!=(len(print_sequence)-1) and any([(aft in forbidden_after[carac]) for aft in print_sequence[index:]]) )

def check_compatibility(index,sequence):
	carac = sequence[index]
	compatibility =[]
	for index2,carac2 in enumerate(sequence):
		if index == index2:
			compatibility.append(1)
		if index2 < index:
			compatibility.append(int(not (carac2 in forbidden_before[carac])))
		if index2> index:
			compatibility.append(int(not (carac2 in forbidden_after[carac])))
	return compatibility

def pivot(sentence):
	new_sentence=sentence
	for index in range(len(new_sentence)):
		running_index = index
		compatibility = check_compatibility(running_index,new_sentence)
		if 0 not in compatibility:
			continue
		while True:
			compatibility = check_compatibility(running_index,new_sentence)
			if 0 in compatibility:
				index_of_zero=compatibility.index(0)
				tampon = new_sentence[index_of_zero]
				new_sentence[index_of_zero]=new_sentence[running_index]
				new_sentence[running_index] = tampon
			else:
				break
	return new_sentence



if __name__ == "__main__":
	forbidden_before = defaultdict(list)
	forbidden_after = defaultdict(list)
	data = []
	with open("input","r") as file:
		for line in file:
			if "|" in line:
				before, after = map(int,line.replace("\n","").split("|"))
				forbidden_before[before].append(after)
				forbidden_after[after].append(before)
			if "," in line:
				data.append(list(map(int,line.replace("\n","").split(","))))

	invalid_sentences=[]
	summed = 0
	for i in range(len(data)):
		print_sequence=data[i]
		
		validity_sequence= [(0 in check_compatibility(j,print_sequence)) for j in range(len(print_sequence))]
		if any(validity_sequence):
			invalid_sentences.append(print_sequence)
			continue
		else:
			summed += print_sequence[len(print_sequence)//2]
	print("part 1", summed)
	summed = 0
	for invalid_sentence in invalid_sentences:
		
		pivoted = pivot(invalid_sentence)
		print(any([(0 in check_compatibility(j,pivoted)) for j in range(len(pivoted))]))
		summed += pivoted[len(invalid_sentence)//2]
	print("part 2:",summed)


