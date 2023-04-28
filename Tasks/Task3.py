from collections import Counter
# Мое решение
lst1 = ['bella', 'label', 'roller']
lst2 = ['cool', 'lock', 'cook']

def common_letters(lst):
    dictionary = {}
    result = []  

    for i in lst:
        for j in i:
            if j in dictionary.keys():
                dictionary[j] += 1
            else:
                dictionary[j] = 1
    
    for key, value in dictionary.items():
        result.extend([key] * (value // len(lst)))

    return result

# Не мое решение
def common_letters_with_duplicates(lst):
    # Создаем список для общих символов
    common_chars = []

    # Находим общие символы без дубликатов
    unique_common_chars = set.intersection(*map(set, lst))
    
    for char in unique_common_chars:
        # Находим минимальное количество вхождений символа в каждую строку
        min_count = min([Counter(string)[char] for string in lst])
        
        # Добавляем символ в результат с учетом количества вхождений
        common_chars.extend([char] * min_count)

    return common_chars
