magical_matrix = [[2, 7, 6],
                  [9, 5, 1],
                  [4, 3, 8]]


not_magical_matrix = [[2, 2],
                      [2, 2]]

def print_matrix(m):
    for row in m:
        print(row)

def is_unique(m):
    tmp = []
    for row in m:
        for element in row:
            if element not in tmp:
                tmp.append(element)
            else:
                return False
    return True

def is_magic(m):
    size = len(m)
    target_summ = column_sum(m, 0)


    if not is_unique(m):
        return False

    #columns
    if not columns_sum_equal(m, target_summ):
        return False
    #rows 
    if not rows_sum_equal(m, target_summ):
            return False

    #diagonals
    if not diagonals_sum_equal(m, target_summ):
        return False
    
    return True

def diagonals_sum_equal(m, target):
    tmp = 0
    size = len(m)
    for i in range(size):
        tmp += m[i][i]
    
    if tmp != target:
        return False
    
    tmp = 0 
    i, j = 0,  size -  1
    while (i != size - 1):
        tmp += m[i][j]
        i += 1
        j -= 1
    else:
        tmp += m[i][j]

    if tmp != target:
        return False
    
    return True


def rows_sum_equal(m, target: int) -> bool:
    size = len(m)
    for i in range(size):
        if sum(m[i]) != target:
            return False
    return True
    
def columns_sum_equal(m, target: int) -> bool:
    size = len(m)

    for i in range(1, size):
        if column_sum(m, i) != target:
            return False
        
    return True

def column_sum(m, col) -> int:
    size = len(m[0])
    summ = m[0][col]
    for j in range(1, size):
        summ += m[j][col]

    return summ

print_matrix(not_magical_matrix)
print("Is this matrix magical?", is_magic(not_magical_matrix))

print_matrix(magical_matrix)
print("Is this matrix magical?", is_magic(magical_matrix))