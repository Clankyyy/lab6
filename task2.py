from functools import reduce

def add(a, b):
    return a + b

my_list = [i for i in range(1, 11)]


list_sum = reduce(add, my_list)

print("list sum is ", list_sum)