def is_Prime(n):
    if n < 2:
        return False
    i = 2
    while i*i < n:
        if n % i == 0:
            return False
        i += 1
        
    return True

print(is_Prime(17))
print(is_Prime(14)) 
   
        