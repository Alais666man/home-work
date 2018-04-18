ax = int(input())
ay = int(input())
bx = int(input())
by = int(input())
cx = int(input())
cy = int(input())
x1 = bx - ax
y1 = by - ay
x2 = cx - bx
y2 = cy - by
x3 = cx - ax
y3 = cy - ay
for i in range(1):
    if x1 * x2 + y1 * y2 == 0 or x2 * x3 + y2 * y3 == 0 or x1 * x3 + y1 * y3 == 0:
        print('yes')
    else:
        print('no')
