A = [1, 2, 3, 4, 5, 6]
B = [3, 4]  # Indices where the split should happen

# Split A at the indices in B
result = []
start = 0

for index in B:
    result.append(A[start:index])  # Include the element at the split index
    start = index

# Add the remaining part of A, if any
if start <= len(A):
    result.append(A[start:])

weight = 0
for sublist in result:
    weight = weight + len(set(sublist))

print(result)
print("Total weight:", weight)