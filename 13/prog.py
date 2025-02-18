import numpy as np
import math
import sympy

def euclid(x,y):
    b = max(x,y)
    c = min(x,y)
    if c ==1:
        coef_x,coef_y= [1,1-x]
        if (x*coef_x+y*coef_y)==1:
            return coef_x,coef_y
        else:
            return coef_y,coef_x
    eqs = []
    while True:

        r = b%c
        q= b//c
        eqs.append([b,c,q,r])
        b=c
        c=r
        if r==1:
            break
    x_s=sympy.symbols("x")
    y_s=sympy.symbols("y")
    t_s=sympy.symbols("t")
    eqs.reverse()
    b,c,q,r = eqs[0]
    expr = x_s - q*y_s
    for b,c,q,r in eqs[1:]:
        expr = expr.subs(x_s,t_s)
        expr = expr.subs(y_s,x_s-q*t_s)
        expr = expr.subs(t_s,y_s)
    poly = sympy.Poly(expr,[x_s,y_s])
    coeffs = poly.coeffs()
    coef_x,coef_y=coeffs
    if expr.subs(x_s,x).subs(y_s,y)==1:
        return [coef_x,coef_y]
    elif expr.subs(x_s,y).subs(y_s,x)==1:
        return [coef_y,coef_x]

def solve_equation_bf(equation):
    gcd_x = math.gcd(equation["A"][0],equation["B"][0])
    gcd_y = math.gcd(equation["A"][1],equation["B"][1])
    if equation['Prize'][0]%gcd_x!=0 or equation['Prize'][1]%gcd_y!=0:
        #Problem can't be solved
        return False,0
    equation["A"][0]//=gcd_x
    equation["B"][0]//=gcd_x
    equation["Prize"][0]//=gcd_x

    equation["A"][1]//=gcd_y
    equation["B"][1]//=gcd_y
    equation["Prize"][1]//=gcd_y

    success=[]
    for i in range(0,101):
        for j in range(0,101):
            if ((equation["A"][0]*i +  equation["B"][0]*j )==equation["Prize"][0]) and ((equation["A"][1]*i +  equation["B"][1]*j )==equation["Prize"][1]):
                success.append(3*i+j)
    if success!=[]:
        if len(success)>1:
            print(success)
        return True,min(success)
    else:
        return False,0


def solve_equation(equation):
    gcd_x = math.gcd(equation["A"][0],equation["B"][0])
    gcd_y = math.gcd(equation["A"][1],equation["B"][1])
    if equation['Prize'][0]%gcd_x!=0 or equation['Prize'][1]%gcd_y!=0:
        #Problem can't be solved
        return False,[0,0]
    # tranforming equation in primal numbers
    equation["A"][0]//=gcd_x
    equation["B"][0]//=gcd_x
    equation["Prize"][0]//=gcd_x

    equation["A"][1]//=gcd_y
    equation["B"][1]//=gcd_y
    equation["Prize"][1]//=gcd_y

    sol1 = np.array(euclid(equation["A"][0],equation["B"][0]))* equation["Prize"][0]
    sol2 = np.array(euclid(equation["A"][1],equation["B"][1]))* equation["Prize"][1]
    matrix = np.array([[equation["B"][0],-equation["B"][1]],[-equation["A"][0],equation["A"][1]]])
    det = matrix[0,0]*matrix[1,1] - matrix[1,0]*matrix[0,1]
    k = (sol2[0]-sol1[0])*matrix[1,1] + (sol2[1]-sol1[1])*(-matrix[0,1])
    if k%det==0:
        k//=det
        sol = [k*matrix[0,0]+sol1[0],k*matrix[1,0]+sol1[1]]
        if any([inputs<0 for inputs in sol]):
            return False,sol
        else:
            return True,sol
    else:
        return False,[0,0]

    # second_member=np.array([-sol2[0]+sol1[0],[sol2[1]+sol1[1]]])
    # if np.linalg.det(matrix)==0:
    #     pass







if __name__=="__main__":
    data = []
    sample={}
    with open("input","r") as file:
        for line in file:
            if line=="\n":
                data.append(sample)
                sample={}
            if "Button A:" in line:
                sample["A"]=[int(line.split("+")[1].split(",")[0]),int(line.split("+")[2])]
            if "Button B:" in line:
                sample["B"]=[int(line.split("+")[1].split(",")[0]),int(line.split("+")[2])]
            if "Prize" in line:
                sample["Prize"]=[int(line.split("=")[1].split(",")[0]),int(line.split("=")[2])]
    summed_values = 0
    for equation in data:
        worked,values=solve_equation_bf(equation)
        if worked:
            summed_values+=values
    print("part 1:",summed_values)


    data = []
    sample={}
    with open("input","r") as file:
        for line in file:
            if line=="\n":
                data.append(sample)
                sample={}
            if "Button A:" in line:
                sample["A"]=[int(line.split("+")[1].split(",")[0]),int(line.split("+")[2])]
            if "Button B:" in line:
                sample["B"]=[int(line.split("+")[1].split(",")[0]),int(line.split("+")[2])]
            if "Prize" in line:
                sample["Prize"]=[int(line.split("=")[1].split(",")[0])+10000000000000,int(line.split("=")[2])+10000000000000]
    summed_values = 0
    for equation in data:
        check1,values1=solve_equation(equation)
        if check1:
            summed_values +=values1[0]*3+values1[1]

    print("part 2:",summed_values)





