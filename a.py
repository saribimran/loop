#input the value of term
n = int (input("Enter the number of terms: "))

sum = 0 #initialise
i = 1 #initialise
while i <= n: #loop willrun from 1 to n
    sum = sum + i 
    i = i + 1 

print("\nsum is:", sum)