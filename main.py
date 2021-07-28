import Sortingpy as sp
import peakFinder as pf
import numpy as np
''' A=[1,3,4,1,2]
print('Insertion Sort')
print(sp.insertion_sort(A))
print('Selection Sort')
print(sp.selection_sort(A))
#A=[1,3,5,2,4]
#print(sp.merge(A,0,3,5))
print('Merge Sort')
print(sp.merge_sort(A,0,5))'''

'''
problemMatrix = np.array([
	[ 4,  5,  6,  7,  8,  7,  6,  5,  4,  3,  2],
	[ 5,  6,  7,  8,  9,  8,  7,  6,  5,  4,  3],
	[ 6,  7,  8,  9, 10,  9,  8,  7,  6,  5,  4],
	[ 7,  8,  9, 10, 11, 10,  9,  8,  7,  6,  5],
	[ 8,  9, 10, 11, 12, 11, 10,  9,  8,  7,  6],
	[ 7,  8,  9, 10, 11, 10,  9,  8,  7,  6,  5],
	[ 6,  7,  8,  9, 10,  9,  8,  7,  6,  5,  4],
	[ 5,  6,  7,  8,  9,  8,  7,  6,  5,  4,  3],
	[ 4,  5,  6,  7,  8,  7,  6,  5,  4,  3,  2],
	[ 3,  4,  5,  6,  7,  6,  5,  4,  3,  2,  1],
	[ 2,  3,  4,  5,  6,  5,  4,  3,  2,  1,  0]
])
n,m=problemMatrix.shape
print(pf.peakfinder_2D(problemMatrix,0,m))'''
#a=[2,1]
#print(pf.peakfinder_1D(a,0,2))
A=[1,3,4,1,2]
print(sp.bubbleSort(A))