def func(A, B):
    i = 0
    j = 0
    output = []
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            output.append(A[i])
            i += 1
        else:
            output.append(B[j])
            j += 1
    output.extend(A[i:])
    output.extend(B[j:])
    return [output[: len(A)], output[len(A) : len(A) + len(B)]]


A = [1, 3, 5]
B = [2, 4, 6]
print(func(A, B))
