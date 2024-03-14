def pyth_triplets(num):
    store = []
    for a in range(1, num + 1):
        for b in range(a, num + 1):
            c = (a**2 + b**2)**0.5
            if c.is_integer() and c <= num:
                store.append((a, b, int(c)))
    return store

for i in pyth_triplets(30):
    print(i)
