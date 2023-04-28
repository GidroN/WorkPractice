lst1 = ['bella', 'label', 'roller']
lst2 = ['cool', 'lock', 'cook']

dictionary = {}
result = []  

for i in lst1:
    for j in i:
        if j in dictionary.keys():
            dictionary[j] += 1
        else:
            dictionary[j] = 1
   
for key, value in dictionary.items():
    result.extend([key] * (value // len(lst1)))

print(result)