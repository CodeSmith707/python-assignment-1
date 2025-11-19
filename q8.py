# 8.	Output dictionary which contains only the odd numbers that are present 
# in the input list as keys and their cubes as values using List Comprehension


nums = list(map(int, input("Enter numbers separated by space: ").split()))

result = {n: n**3 for n in nums if n % 2 != 0}

print(result)
