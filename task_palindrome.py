def is_palindrome(s):
    s = str(s)                         # Преобразуем тип входных данных в строку
    s = s.lower().replace(' ', '')     # Замена всех символов на строчные и удаление пробелов
    if s == s[::-1]:                   
        return True
    else:
        return False
    
    
    
    
    #if isinstance(s,int) == False:
        #s == s[::-1]
        #return True
    #else:
        #return False
    #elif:
        #s = str(s)
        #s == s[::-1]
        #return True
    #else:
        #return False

#is_palindrome(input())
#print(is_palindrome(input)) 

    
    #if isinstance(s,int) == True:
        #s = str(s)
        #s == s[::-1]
        #return True
    #elif s != s[::-1]:
        #return False
    #else:
        #return True
  
  #if s == int:
        #s = str(s)
        #s == s[::-1]
        
        #return True
    #elif s == str:
        #s == s[::-1]
        #return True
    #else:
        #return False
