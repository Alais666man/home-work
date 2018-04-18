t = int(input())
s = float(input())
while t > 0 and s > 0:
    t = t - 1
    s = s - 0.5
    if t != 0 and s == 0:
        print("Моющее средство закончилось. Осталось %d тарелок"%(t))
    elif t == 0 and s != 0:
        print('Все тарелки вымыты. Осталось %.1f ед. моющего средства'%(s))
    elif t == 0 and s == 0:
        print ('Все тарелки вымыты, моющее средство закончилось')










#for i in range(1):
    #if t > s:
        #s = s * 2
        #i = t - s
        #print("Моющее средство закончилось. Осталось %d тарелок"%(i))
    #elif t < s:
        #s = s * 2
        #i = s - t
        #print('Все тарелки вымыты. Осталось %.1f ед. моющего средства'%(i))
    #elif t == s:
        #i = s 
        #print('Все тарелки вымыты, моющее средство закончилось')

















#print('Тарелки')
#t = [int(input())]
#print (t)
#print('Средство')
#s = [int(input())]
#s[:] = [x * 2 for x in s]
#print(s)
#for i in t:
    #if t > s:
        #i = list(set(t) - set(s))
        #print(i)

#for i in t:
    #if t











#print('Количество тарелок')
#n = int(input())
#tarelka = [i for i in range(1,n + 1)]
#print(tarelka)
#print('Количество средства')
#n = int(input())
#sredstvo = [i for i in range(1,n*2+1)]
#print(sredstvo)
#for i in tarelka:
    #if tarelka > sredstvo:
        
        #print()
    #elif tarelka < sredstvo:
        #print('Все чистые, средство осталось')
    #elif tarelka == sredstvo:
        #print('Всё чистое, средства нет')




#n = int(input())
#a = [i for i in range(n)]
#print(a)
