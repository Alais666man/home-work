def get_quadrant_number(x, y):
        if x > 0 and y > 0:
            n = 1
            return n
        elif x < 0 < y:
            n = 2
            return n
        elif x < 0 and y < 0:
            n = 3
            return n
        elif y < 0 < x:
            n = 4
            return n
        elif x == 0 and y == 0:
            raise ValueError

#
#
# def get_quadrant_number(x, y):
#     n = 1 if x > 0 and y > 0 else None
#     n = 3 if x < 0 and y < 0 else None
#     n = 4 if y < 0 < x else None
#     n = 2 if x < 0 < y else None
#     raise ValueError if x ==0 and y == 0 else None







