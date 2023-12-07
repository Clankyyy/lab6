import random


def is_prime(num):
    random_num = random.randint(1, num - 1)
    random_num = 3

    if(random_num ** (num - 1) % num != 1):
        return False
    
    return True

user_input = int(input())
test_result = is_prime(user_input)
if test_result:
    print(user_input, "more likely is prime")
else:
    print(user_input, "more likely is not prime")
