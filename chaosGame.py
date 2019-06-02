#!/usr/bin/env python3

import random
import matplotlib.pyplot as plt
from math import sqrt


def point_on_triangle(pt1, pt2, pt3):

    s, t = sorted([random.random(), random.random()])
    return (s * pt1[0] + (t-s)*pt2[0] + (1-t)*pt3[0], s * pt1[1] + (t-s)*pt2[1] + (1-t)*pt3[1])


N = int(input("How many dots? "))

if (N < 1):
    print("Greater than 1!")
    quit()

ptB = (2, 0)
ptC = (0, 0)
ptA = (ptB[0]/2, ptB[0]*(sqrt(3)/2))

points = [ptA, ptB, ptC]

points.append(point_on_triangle(ptA, ptB, ptC))

M = []

M.append(((ptA[0] + points[-1][0])/2, (ptA[1] + points[-1][1])/2))

i = 1
while i < N:
    M.append(((M[i-1][0] + ptB[0]) / 2, (M[i-1][1] + ptB[1]) / 2))
    M.append(((M[i][0] + ptC[0]) / 2, (M[i][1] + ptC[1]) / 2))
    M.append(((M[i+1][0] + ptA[0]) / 2, (M[i+1][1] + ptA[1]) / 2))

    points.append(M[i-1])
    points.append(M[i])
    points.append(M[i+1])

    i = i + 2

x, y = zip(*points)
plt.scatter(x, y, s=0.1)
plt.show()
