size_of_array = int(input().strip())
array = list(map(int, input().strip().split()))
reversed_array = array[::-1]
print(" ".join(map(str, reversed_array)))
