triplets = []


for a in range(1, 31):
    for b in range(a, 31):
        for c in range(b, 31):
            if a**2 + b**2 == c**2:
                triplets.append((a, b, c))

list2=list(triplets)
print(list2)
