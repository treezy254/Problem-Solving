''' Consider a matrix where each cell contains eother a 0 or a 1. Any cell 
containing a 1 is called a filled cell. Two cells are said to be connected if
they are adjacent to each otehr  horizontally, vertically, or diagonally. In the
following grid, all cells marked X are connected to the cell marked Y.

XXX
XYX
XXX

if one or more filled cells are also connected, they form a region. Note that
each cell in a region is connected to zero or more cells in the region but is
not necessarily directly connected to all the other cells in the region.

Given an n X m matrix, find and print the number of cells in the largest
region in the matrix. note that they may be more that one region in the matrix.

Function Description

Complete the connectedCell function in the editor below.

connectedCell has the following parameter(s):
- int matrix[n][m]:  represents the  row of the matrix

Returns
- int: the area of the largest region

''''

matrix = []
rows = 0
cols = 0
def searchNeigbours(i, j):
	if matrix[i][j] == 1:
		matrix[i][j] = -1
		s = 0
		for ii in range(max(0, i-1), min(i+2, rows)):
			for jj in range(max(0, j-1), min(j+2, cols)):
				s += searchNeigbours(ii, jj)

		print(i, j, s)
		return 1 + s
	return 0


def connectedCell(matrix):

	global rows
	global cols
	rows = len(matrix)
	cols = len(matrix[0])
	mx = 0
	for i in range(0, rows):
		for j in range(0, cols):
			mx = max(mx, searchNeigbours(i, j))

	return mx