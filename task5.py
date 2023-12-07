def greatest_devisor(a, b):
    minim = min(a, b)

    for i in range(minim, 0, -1):
        if (a % i == 0) and (b % i == 0):
            return i
    return 1

if __name__ == "__main__":
    print("Greates devisor for {0} and {1} is".format(25, 100), greatest_devisor(25, 100))