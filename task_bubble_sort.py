def bubble_sort(lst):
    for j in range(len(lst) - 1):                               # Проход по каждлму элементу списка
        for i in range(len(lst) - 1):                           # Проход по элемнту в паре
            if lst[i] > lst[i + 1]:                             # Если первый элемент пары больше второго
                lst[i], lst[i + 1] = lst[i + 1], lst[i]         # Меняем элементы пары местами
    return lst

