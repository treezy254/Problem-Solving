def diagonalDifference(arr):
    temp = 0
    emp = 0
    for i in range(0, len(arr)):
        temp += arr[i][i]

    for j in range(0, len(arr)):
        emp += arr[j][len(arr)-1-j]

    return abs(temp - emp)