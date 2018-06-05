def camel_to_snake(name):                                 
    a = list(name)                                        
    for c in range(len(a)):                                    
        if a[c].isupper() and c != 0 and a[c-1] != '_':                  
            a.insert(c, '_')
            c += 1                                        
            return ''.join(a).lower()


def snake_to_camel(name):
    if name.lower():
        name = name.title()
        name = name.replace('_', '')
        return name 
   




#def snake_to_camel(name):
    #a = list(name)
    #for c in range(len(a)):
        #if a[c].islower and c != 0 and a[c-1] == '_':
            #a.title()
            #a.remove('_')
            #c += 1
            #return ''.join(a)
#print (snake_to_camel(name))        



#def snake_to_camel(name):
    #if name.islower() == True:
        #name = name.title().replace("_","")
        #return name 
#print(snake_to_camel(name))




# Начало функции
# Список из строки
# Для 'c' в диапазоне длины списка
# Если элемент 'c' в списке 'a' в верхнем регистре и не нулевого индекса и элемент 'c-1' не равен '_' 
# Вставка разделителя с индексом 'c' 
# Переход по списку
# Сборка строки с пустым разделителем и преобразование в нижний регистр
