import numpy as np

import re

def mul(x,y):

    return x*y

def filter_string(sentence):

    p1 = re.compile(r'don\'t\(\)')

    p2 = re.compile(r'do\(\)')

   

    while p1.search(sentence):

        search_object = p1.search(sentence)

        search_object2 = p2.search(sentence[search_object.end():])

        if search_object2:

            sentence = sentence[:search_object.start()]+sentence[search_object.end():][search_object2.end():]

        else:

            sentence = sentence[:search_object.start()]

    return sentence

 

def filter_via_mask(sentence):

    state=True

    extracted_sentence = []

    local_sentence=sentence

    skip=0

    for i,char in enumerate(sentence):

        if skip >0:

            skip-=1

            continue

        if char=='d':

            if sentence[i:i+7]=="don't()":

                skip=6

                state=False

                continue

            if sentence[i:i+4]=="do()":

                skip=3

                state=True

                continue

        else:

            if state:

                extracted_sentence.append(char)

    return ''.join(extracted_sentence)

   

    

    

def filter_string2(sentence):

    local_sentence = sentence

    p = re.compile(r'mul\(\d+,\d+\)')

    p1 = re.compile(r'don\'t\(\)')

    p2 = re.compile(r'do\(\)')

    state=True

    operations=[]

    while local_sentence!="":

        if state:

            if p1.search(local_sentence):

                search_object = p1.search(local_sentence)

                operations +=list(map(eval,p.findall(local_sentence[:search_object.start()])))

                local_sentence = local_sentence[search_object.end():]

                state=False

            else:

                break

       

        else:

            if p2.search(local_sentence):

                search_object = p2.search(local_sentence)

                local_sentence = local_sentence[search_object.end():]

                state=True

            else:

                break

    if state:

        operations +=list(map(eval,p.findall(local_sentence)))

    return sum(operations)

           

        

    

    

    

p1 = re.compile(r'don\'t\(\)')

p2 = re.compile(r'(do\(\)|\n)')

p = re.compile(r'mul\(\d+,\d+\)')

 

with open("input.txt","r") as file:

    data = sum(list(map(eval,p.findall("".join([line for line in file])))))

 

print("part 1:",data)   

 

 

with open("input.txt","r") as file:

   

        

    data=sum(list(map(eval,p.findall(filter_string("".join([line for line in file]))))))

           

       

print("part 2:",data)   