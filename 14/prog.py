import numpy as np
from itertools import product

def outside(i,j,width,height):
    return  i<0 or j<0 or i>=width or j>height
def count_length(k,positions,done_nodes,width,height,map_trace):
    if k in done_nodes:
        return
    else:
        i,j = positions[k]
        for di,dj in product([-1,0,1],repeat=2):
            if outside(i+di,j+dj,width,height) or (di==0 and dj==0):
                continue
            else:
                not_done_positions = positions[[i for i in range(positions.shape[0])if i not in done_nodes]]
                for l in range(not_done_positions.shape[0]):
                    if not_done_positions[l][0]==(i+di) and not_done_positions[l][1]==(j+dj):
                        map_trace[i+di,j+dj]=1
                        done_nodes.append(l)
                        count_length(l,positions,done_nodes,width,height,map_trace)






if __name__ == "__main__":
    data_p= []
    data_v =[]
    with open("input","r") as file:
        for line in file:
            p,v = line.replace("\n","").split()
            data_p.append(list(map(int,p.split("=")[1].split(","))))
            data_v.append(list(map(int,v.split("=")[1].split(","))))
    data_p = np.array(data_p)
    data_v = np.array(data_v)
    width=101
    height=103
    data_p = data_p + 100*data_v

    data_p[:,0]%=width
    data_p[:,1]%=height


    first_quadrant=np.sum(((data_p[:,0]<width//2)*(data_p[:,1]<height//2)).astype(int))
    second_quadrant=np.sum(((data_p[:,0]>width//2)*(data_p[:,1]<height//2)).astype(int))
    third_quadrant=np.sum(((data_p[:,0]<width//2)*(data_p[:,1]>height//2)).astype(int))
    fourth_quadrant=np.sum(((data_p[:,0]>width//2)*(data_p[:,1]>height//2)).astype(int))
    print(first_quadrant*second_quadrant*third_quadrant*fourth_quadrant)

    data_p= []
    data_v =[]
    with open("input","r") as file:
        for line in file:
            p,v = line.replace("\n","").split()
            data_p.append(list(map(int,p.split("=")[1].split(","))))
            data_v.append(list(map(int,v.split("=")[1].split(","))))
    print(len(data_p))
    data_p = np.array(data_p)
    data_v = np.array(data_v)
    i=1
    max_length = 0
    max_lengthes=0
    while True:
        current_pos = data_p + i*data_v
        current_pos[:,0]%=width
        current_pos[:,1]%=height
        first_quadrant=np.sum(((current_pos[:,0]<width//2)*(current_pos[:,1]<height//2)).astype(int))
        second_quadrant=np.sum(((current_pos[:,0]>width//2)*(current_pos[:,1]<height//2)).astype(int))
        third_quadrant=np.sum(((current_pos[:,0]<width//2)*(current_pos[:,1]>height//2)).astype(int))
        fourth_quadrant=np.sum(((current_pos[:,0]>width//2)*(current_pos[:,1]>height//2)).astype(int))
        if first_quadrant==second_quadrant and third_quadrant == fourth_quadrant:
            print(i)

        # done_nodes = [0]
        # lengthes = []

        # for k in range(current_pos.shape[0]):
        #     map_trace = np.zeros((width,height),int)
        #     map_trace[*current_pos[k]]=1
        #     count_length(k,current_pos,done_nodes,width,height,map_trace)
        #     length = np.sum(map_trace)
        #     lengthes.append(length)
        # if max(lengthes)>max_length:
        #     print(i,max(lengthes))
        #     max_length = max(lengthes)

        # first_line=np.sum((current_pos[:,1]==102).astype(int))
        # second_line=np.sum((current_pos[:,1]==101).astype(int))
        # third_line=np.sum((current_pos[:,1]==100).astype(int))
        # fourth_line=np.sum((current_pos[:,1]==99).astype(int))
        # # if first_line==second_line and second_line==third_line and fourth_line==third_line and first_line==2:
        # #     print(i)
        # #     break
        # # highest_points = current_pos[current_pos[:,1]==np.min(current_pos[:,1])]
        # # if highest_points.shape[0]==1 and highest_points[0,0]==width//2 and first_line==2 and second_line==2:
        # #     print(i)
        # symmetric_pos = np.copy(current_pos)
        # symmetric_pos[:,0]= width//2 - (symmetric_pos[:,0] - width//2)
        # canvas = np.zeros((width,height),int)
        # canvas[current_pos[:,0],current_pos[:,1]]+=1
        # proj_y = np.sum(canvas,axis=0)
        # proj_x = np.sum(canvas,axis=1)

        # lengthes_y=[]
        # length_y=0
        # for m in range(proj_y.shape[0]):
        #     if proj_y[m]!=0:
        #         length_y+=1
        #     else:
        #         lengthes_y.append(length_y)
        #         length_y=0
        # lengthes_y.append(length_y)
        # lengthes_x=[]
        # length_x=0
        # for m in range(proj_x.shape[0]):
        #     if proj_x[m]!=0:
        #         length_x+=1
        #     else:
        #         lengthes_x.append(length_x)
        #         length_x=0
        # lengthes_x.append(length_x)
        # proj_length = min((max(lengthes_x),max(lengthes_y)))
        # if proj_length> max_lengthes:
        #     print(i,proj_length)
        #     max_lengthes = proj_length





        # canvas_sym = np.zeros((width,height),int)
        # canvas_sym[symmetric_pos[:,0],symmetric_pos[:,1]]+=1
        # if np.sum((canvas==canvas_sym).astype(int))==(width*height):
        #     print(i)
        i+=1


