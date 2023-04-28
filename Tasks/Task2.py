a = [1, 4, 6]
b = [11, 33, 22]

def sort_by(a, b):
    return sorted(a, key=lambda x: b[a.index(x)])

print(sort_by(a, b))