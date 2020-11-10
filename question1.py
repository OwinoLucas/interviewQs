# Question 1

def missingInteger(array_K):
    array_K.sort()
    N = len(array_K)
    print(N)

    for i in range(0, N):
        while array_K[i + 1] > array_K[i] and array_K[i] >= 1:
            if array_K[i + 1] - array_K[i] != 1:
                return array_K[i] + 1
            if array_K[i + 1] - array_K[0] == 1 and array_K[i] == 2:
                return 1
            # if array_K[i + 1] - array_K[i] == 1 and array_K[i] == 1 and array_K[-1] == N - 1:
            #     return array_K[-1] + 1
            i += 1


# test example
print(missingInteger([3, 1, 5, 4]))
