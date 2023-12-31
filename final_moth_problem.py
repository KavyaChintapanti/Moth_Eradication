# -*- coding: utf-8 -*-
"""final_moth_problem.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zFv2pKThZwoZEs7YvAglmQreNWsWqTSi
"""

class Location: 
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 

def problem_input(no_of_traps) :
    point_list = []
    x_list=[]
    y_list=[]
    for i in range(no_of_traps):
        x, y = [float(i) for i in input().split()]
        x_list.append(x)
        y_list.append(y)
        point_list.append(Location(x,y))
    polygon_vertices = convex_hull(point_list,len(point_list))
    return polygon_vertices,x_list,y_list

import math
def total_perimeter(point_list) ->str:
    perimeter = 0
    for i in range(0,len(point_list)):
        p1 = point_list[i]
        if i == len(point_list) - 1 :
            break
        else :
            p2 = point_list[i+1]
        perimeter += math.sqrt(((p2[0]-p1[0])**2)+((p2[1]-p1[1])**2))
    return round(perimeter,2)

def convex_hull(point_list,no_of_traps):
    if no_of_traps < 3: 
        return
    bottomleft_point = finding_initial_P(point_list) 
    hull = [] 
    fp = bottomleft_point
    sp= 0
    while(True): 
        hull.append(fp) 
        sp = (fp+1) % no_of_traps
        for i in range(no_of_traps): 
            if orientation(point_list[fp],point_list[i], point_list[sp]) == 2: 
                sp = i 
        fp = sp 
        if(fp == bottomleft_point): 
            break
    vertices = []
    begin_vertex = []
    for trap in hull:
        vertices.append([point_list[trap].x,point_list[trap].y])
    begin_vertex.append(vertices[0])
    vertices.extend(begin_vertex)
    return vertices[::-1]

def finding_initial_P(point_list) :
    min = 0
    for i in range(1,len(point_list)): 
        if point_list[i].y < point_list[min].y: 
            min= i 
        elif point_list[i].y == point_list[min].y: 
            if point_list[i].x < point_list[min].x : 
                min = i 
    return min
def orientation(fp, sp, tp) :
    value = ((sp.y - fp.y) * (tp.x - sp.x)) - ((sp.x - fp.x) * (tp.y - sp.y))
    if value == 0:   
        return 0  # collinear
    elif value > 0: 
        return 1  # Clockwise
    else: 
        return 2  # Counterclockwise
  
def problem_output(point_list) ->str:
    list1 =[]
    list2= []
    for i in (tuple(x) for x in point_list):
        list1.append(i)
    new_tuple= tuple(list1)
    for i in new_tuple:
        s=str(i)
        list2.append(s)
        poly_edges="-".join(list2)
    print(poly_edges)

    
import matplotlib.pyplot as plt
def problem_plot(x,y,point_list) :
    plt.scatter(x,y,color = 'blue')
    plt.xlabel("X - axis")
    plt.ylabel("Y - axis")
    x_points = []
    y_points = []
    points = [z for y in point_list for z in y]
    x_points = points[::2]
    y_points = points[1::2]
    plt.plot(x_points,y_points,color='green')
    plt.legend(["Edge of Polygon", "Moth Trap"], loc ="upper left")
    plt.show()

no_of_traps=1
while(no_of_traps!=0):
  for area in range(1,1000):
    no_of_traps=int(input())
    if no_of_traps==0:
      break
    polygon_vertices,x_points,y_points= problem_input(no_of_traps)
    print(_)
    print("Region #",area,":")
    problem_output(polygon_vertices)
    print("Perimeter length = ",total_perimeter(polygon_vertices))
    problem_plot(x_points,y_points,polygon_vertices)