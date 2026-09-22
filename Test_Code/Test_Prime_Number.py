from Code.Prime_Number import is_Prime

assert is_Prime(15) == False  
print("Test case 1 pass")

assert is_Prime(11) == True
print("Test case 2 pass ")


assert is_Prime(11) != False  
print("Test case 3 pass")

assert is_Prime(12) == False
print("Test case 4 pass ")