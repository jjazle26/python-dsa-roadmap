class_a = {"Alice", "Bob", "Charlie"}
class_b = {"Bob", "David", "Eve"}

both = class_a & class_b 

only_a = class_a - class_b

print(f"In both: {both}")
print(f"Only in A: {only_a}")