import numpy as np
import math
from array import array







def bernstein_basis_poly(n,k,v):
    n_fact = math.factorial(n)
    nminusk_fact = math.factorial(n-k)
    k_fact = math.factorial(k)
    a = n_fact/(nminusk_fact*k_fact)
    b = v**k
    c = (1-v)**(n-k)
    val = a*b*c
    return(val)


def find_1D_bernstein_poly_vector(d,v):
    coeffs = [None] * (d+1)
    for j in range(0,d+1):
        coeffs[j] = bernstein_basis_poly(d,j,v)
    return(coeffs)
        



def bernstein_2D_poly_vector(d,u,v):
    row = []
    for i in range(0,d+1):
        iTerm = bernstein_basis_poly(d,i,u)
        temp = find_1D_bernstein_poly_vector(d,v)
        mul = [iTerm*t for t in temp]
        row = np.hstack((row,mul))
    return (row.astype(float))


def find_2D_bernstein_coeffs(a,b,d): 
    nR = len(a)
    si = (d+1)**2
    M = [None] * si
    for i in range(0,nR):
        temp = bernstein_2D_poly_vector(d,a[i][0],a[i][1])
        temp = np.array(temp)
        M = np.vstack((M,temp))
    M = np.delete(M,0,0)
    coe = np.linalg.lstsq(M,b)
##    inv = np.linalg.inv(b)
##    print(inv)
##    coe = np.dot(inv,M)
    return (coe)










def eval_2D_bernstein_poly(d,coeffs,u,v):
    basis_polys = bernstein_2D_poly_vector(d,u,v)
    val = np.dot(basis_polys,coeffs)
    return (val)

def eval_many_bernstein_polys(d,coeffs,uv):
    nR = len(uv)
    si = (d+1)**2
    values = [[0]*2]
    #print(values)
    for r in range(0,nR):
        val = eval_2D_bernstein_poly(d,coeffs,uv[r][0],uv[r][1])
        values = np.vstack((values,val))
    values = np.delete(values,0,0)
    return(values)


def scale2box (val):
    scaled = [[0]*2]*360
    x_val = [x[0] for x in val]
    min_val_x = min(x_val)
    y_val = [x[1] for x in val]
    min_val_y = min(y_val)
    min_val = [min_val_x,min_val_y]
    
    max_val_x = max(x_val)
    max_val_y = max(y_val)
    max_val = [max_val_x,max_val_y]
    
    nR = len(val)
    

    for i in range(0,nR):
        
        scaled_x = float(val[i][0] - min_val_x)/(max_val_x - min_val_x)
        scaled_y = float(val[i][1] - min_val_y)/(max_val_y - min_val_y)
        scaled[i] = [scaled_x,scaled_y]
    return(max_val,min_val,scaled)
            
    
def dewarp (val,max_val,min_val):
    nR = len(val)
    pt = [[0]*2]*nR
    min_val_x = min_val[0]
    min_val_y = min_val[1]
    max_val_x = max_val[0]
    max_val_y = max_val[1]
    print(max_val_y)
    print(min_val_y)

    for i in range(0,nR):

        x = (val[i][0]*(max_val_x - min_val_x)) + min_val_x
        y = (val[i][1]*(max_val_y - min_val_y)) + min_val_y
        print(val[i][1])
        print(val[i][1]*(max_val_y - min_val_y))
        pt[i] = [x,y]
    return(pt)
    



def get_est(cam,robo,pt):
    [max_val_cam, min_val_cam,scaled_cam] = scale2box(cam)
    [max_val_robo, min_val_robo, scaled_robo] = scale2box(robo)
    print(scaled_robo)
    print(robo)
    
    coef = find_2D_bernstein_coeffs(scaled_cam,robo,3)
    BC4 = coef[0]
    scaled_pt_x = float(pt[0] - min_val_cam[0])/(max_val_cam[0] - min_val_cam[0])
    scaled_pt_y = float(pt[1] - min_val_cam[1])/(max_val_cam[1] - min_val_cam[1])
    scaled_pt = [(scaled_pt_x,scaled_pt_y)]
    estRob = eval_many_bernstein_polys(3,BC4,scaled_pt)
    #cam_points = dewarp(estRob,max_val_robo,min_val_robo)
    #print(cam_points)
    print(estRob)
    return(estRob)




    









    
