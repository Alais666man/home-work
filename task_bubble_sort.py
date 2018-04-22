def bubble_sort(lst):
    for j in range (len(lst), 0, -1):
        for i in range(0, len(lst) - 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                return lst
            
                


            
  #a = [1, 8, 3, 5, 7, 4]

#print(a)

#for i in range(len(a), 0, -1): 
    #for k in range(0, len(a) - 1):
        #if a[k] > a[k + 1]:
            #a[k], a[k + 1] = a[k +1], a[k]
#print(a)



#def bubble_sort(lst):
    #n=len(a)
    #m=n-1
    #while m>0:
        #for i in range(m):
            #if (a[i]>a[i+1]):
                #x=a[i]
                #a[i]=a[i+1]
                #a[i+1]=x
                #m=m-1
                #return lst
                      
#a=[1,0,9]
#print (a)
#n=len(a)
#m=n-1
#while m>0:
    #for i in range(m):
        #if (a[i]>a[i+1]):
            #x=a[i]
            #a[i]=a[i+1]
            #a[i+1]=x
            #m=m-1
#print(a)            










