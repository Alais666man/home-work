def get_free_land(a, b):
    if a[0] == 0:
        raise ValueError("Не задана площадь участка")
    elif b[0] == 0 or b[1] == 0:
        raise ValueError("Не задана площадь грядки")
    elif a[0] * 100 < (b[0] * b[1]):
        raise ValueError("Размер грядки больше размера участка")
    else:
        return a[0] * 100 % (b[0] * b[1])


# if __name__ == '__main__':
    # print(get_free_land((100, '1:1'), (15, 25)))
    # print(get_free_land((0, '1:1'), (15, 25)))
    # print(get_free_land((100, '1:1'), (5, 0)))
    # print(get_free_land((6, '3:2'), (40, 28)))
