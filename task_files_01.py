with open('data.txt') as f:
    a = format(f.readline()).split(' ')
    a = [int(i) for i in a]

with open('out-1.txt', 'w') as f:
    n = input()
    for i in a:
        if i % n == 0:
            i //= n
            f.write(str(i) + ' ')

with open('out-2.txt', 'w') as f:
    p = input()
    for i in a:
        i **= p
        f.write(str(i) + ' ')


