print("точка A [x y]")
Ax = int(input())
Ay = int(input())
print(Ax,Ay)
print("Точка B [x y]")
Bx = int(input())
By = int(input())
print(Bx,By)
print('Точка C [x y]')
Cx = int(input())
Cy = int(input())
print(Cx,Cy)
AB = ((Ax - Bx)**2 + (Ay - By)**2)**0.5
BC = ((Bx - Cx)**2 + (By - Cy)**2)**0.5
AC = ((Ax - Cx)**2 + (Ay - Cy)**2)**0.5
print(AB, BC, AC)
for i in range(1):
    if AB == (BC**2 +AC**2)**0.5 or BC == (AC**2 + AB**2)**0.5 or AC == (AB**2 + BC**2)**0.5:
        print('yes')
    else:
        print('no')
