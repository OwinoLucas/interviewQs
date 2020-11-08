# Question 1

def missingInteger(array_K, N):
    array_K.sort()
    for i in range(0, N + 1):
        if array_K[i + 1] - array_K[i] != 1:
            return array_K[i] + 1
        elif array_K[i + 1] - array_K[i] == 1:
            return array_K[i] - 1
        else:
            i += 1


# test example, you can change the values
print(missingInteger([1, 3, 5, 6, 7, 4], 7))
