def mins(a, i, res):
    n = len(a) - 1
    left = 2 * i + 1
    right = 2 * i + 2
    if not (i >= n // 2 and i <= n):
        if (a[i] > a[left] or a[i] > a[right]):

            if a[left] < a[right]:
                res.append([i, left])
                a[i], a[left] = a[left], a[i]
                mins(a, left, res)

            else:
                res.append([i, right])
                a[i], a[right] = a[right], a[i]
                mins(a, right, res)
def heapify(a, res):
    n = len(a)
    for i in range(n // 2, -1, -1):
        mins(a, i, res)
    return res
print("Before Swapping:")
a = [7, 6, 5, 4, 3, 2]
print(a)
res = heapify(a, [])
print("\nAfter Swapping:")
print(a)
print(res)