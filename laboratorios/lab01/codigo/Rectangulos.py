def rectangulos(n):
    if(n <= 3):
        return n
    elif(n > 3):
        return rectangulos(n-1) + rectangulos(n-2)

#print(rectangulos(5))