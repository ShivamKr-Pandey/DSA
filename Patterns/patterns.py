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



######### Pattern 11 ######### 
for i in range(rows+1):
    if(i%2==0):
        num = 1
    else:
        num = 0
    
    for x in range(i):
        print(num, end="")
        num = 1-num
    
    print()



######### Pattern 12 #########
for i in range(1,rows):
    for x in range(1,i+1):
        print(x, end="")
    
    for y in range(2*(rows-i), 2, -2):
        print(end="  ")
    
    for z in range(i, 0, -1):
        print(z, end="")

    print()




######### Pattern 13 #########
k = 1
for i in range(1,rows+1):
    for x in range(i):
        print(str(k)+" ", end="")
        k = 1 + k
    print()




######### Pattern 14 #########
for i in range(rows + 1):
    for x in range(i):
        print(chr(65 + x), end=" ")
    print()




######### Pattern 15 #########
for i in range(rows, 0 ,-1):
    for x in range(i):
        print(chr(65 + x), end=" ")
    print()




######### Pattern 16 #########
num = 64

for i in range(0,rows + 1):
    for x in range(i):
        print(chr(num), end=" ")
    num = num + 1;
    print()



######### Pattern 17 #########
num = 65

for i in range(0,rows + 1):
    for x in range(rows -i):
        print(end="  ")

    for y in range(i):
        print(chr(num+y), end=" ")

    for y in range(i-2,-1,-1):
        print(chr(num+y), end=" ")
    print()




######### Pattern 18 #########
num = 65

for i in range(0,rows+1):
    sl = num + rows - i
    for x in range(sl,num+rows):
        print(chr(x), end=" ")
    print()



######### Pattern 19 #########
start = 0
for i in range(rows):
    for x in range(rows - i):
        print("*", end="")
    
    for x in range(start):
        print(" ", end="")
    
    for x in range(rows - i):
        print("*", end="")
    
    start += 2
    print()

start = 2 * rows - 2
for i in range(1, rows + 1):
    for x in range(i):
        print("*", end="")
    
    for x in range(start):
        print(" ", end="")
    
    for x in range(i):
        print("*", end="")

    start -= 2
    print()


######### Pattern 20 #########
start = 2 * rows - 2
for i in range(1, rows):
    for x in range(i):
        print("*", end="")
    
    for x in range(start):
        print(" ", end="")
    
    for x in range(i):
        print("*", end="")

    start -= 2
    print()

start = 0
for i in range(rows):
    for x in range(rows - i):
        print("*", end="")
    
    for x in range(start):
        print(" ", end="")
    
    for x in range(rows - i):
        print("*", end="")
    
    start += 2
    print()



######### Pattern 21 #########
for i in range(rows):
    if (i == 0 or i == rows-1):
        print("*" * rows)
    else:
        print("*" + " " * (rows-2) + "*")
