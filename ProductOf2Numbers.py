# Product of 2 numbers using recursion
def product(x,y):
    if y > x:
        return product(y,x)
    
    elif y != 0:
        return (x + product(x,y-1))
    
    else:
        return 0
    

print(product(221,5234))