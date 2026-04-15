# alternate to question 2
from collections import defaultdict
from itertools import combinations

A = [3, 5, 6, 3, 3, 5]

val_dict = defaultdict(list)
print("early val dict", val_dict)
for i, v in enumerate(A):
	val_dict[v].append(i)

print("late val dict", val_dict)

combos = []
for k, l in val_dict.items():
	combos.extend( combinations(l, 2))
print("these are combinations", combos)

print(f"valid combinations: {combos}")
print(f"num combinations: {len(combos)}")
