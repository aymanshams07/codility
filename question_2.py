A = [3, 5, 6, 3, 3, 5]
print(A)
count = 0
max_count = 10 ** 9
print(max_count)
for i in range(len(A)):
    for j in range(i + 1, len(A)):
        if A[i] == A[j]:
            count += 1
            if count > max_count:
                count = max_count

print(count)
