################ Patterns Questions ################


rows = int(input("Enter a number:"))

# converted_integer = int(rows)


######### Pattern 1 #########
for i in range(rows):    
    for x in range(rows):
        print("* ", end="")
    print()


######### Pattern 2 ######### 
for i in range(1,rows + 2):
    for x in range(1,i):
        print("*", end="")
    print()


######### Pattern 3 ######### 
for i in range(1,rows + 2):
    for x in range(1,i):
        print(x, end="")
    print()


######### Pattern 4 ######### 
for i in range(1,rows + 1):
    for x in range(i):
        print(i, end="")
    print()



######### Pattern 5 ######### 
for i in range(rows,0, -1):
    for x in range(i):
        print("*", end="")
    print()



######### Pattern 6 ######### 
for i in range(rows,0, -1):
    for x in range(1,i):
        print(x, end="")
    print()




######### Pattern 7 ######### 
for i in range(1, rows+1):
    for x in range(1,(rows-i)+1):
        print(end="  ")

    for y in range(2*i-1, 0 ,-1):
        print("* ", end="")

    print()




######### Pattern 8 ######### 
for i in range(rows, 0 , -1):
    for x in range(0, rows-i):
        print(end="  ")

    for y in range (2*i-1, 0 ,-1):
        print("* ",end="")

    print()




######### Pattern 9 ######### 
for i in range(1, rows+1):
    for x in range(1,(rows-i)+1):
        print(end="  ")

    for y in range(2*i-1, 0 ,-1):
        print("* ", end="")
    
    print()


for i in range(rows, 0 , -1):
    for x in range(0, rows-i):
        print(end="  ")

    for y in range (2*i-1, 0 ,-1):
        print("* ",end="")

    print()



######### Pattern 10 ######### 
for i in range(1,rows + 2):
    for x in range(1,i):
        print("*", end="")
    print()

for i in range(rows,0, -1):
    for x in range(i):
        print("*", end="")
    print()