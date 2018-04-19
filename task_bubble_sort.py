

def bubble_sort(spisok):
    n = 1
    while n < len(spisok):
        
        for i in range(len(spisok) - n):
            if spisok[i] > spisok[i + 1]:
                spisok[i], spisok[i + 1] = spisok[i + 1], spisok[i]
                n = n + 1
                
spisok = [14, 8, 3, 1, 89, 2, 45]            
bubble_sort(spisok) 
print(spisok)
                
            
    

        
        
