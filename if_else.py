n = int(input())

if n % 2 == 1: #* if n is odd
    print("Weird") #* print weird

elif n % 2 == 0 and 2 <= n <= 5: #* if n is even and greater than 2 or less than 5
    print("Not Weird") #* print not weird

elif n % 2 == 0 and 6 <= n <= 20: #* if n is even and greater than 6 or less than 20
    print("Weird") #* print weird

else:
    print("Not Weird") #* else just print wierd