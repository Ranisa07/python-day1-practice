# Nested Loop(Means Loop inside another Loop)
# Programs: Pattern-1(Square)                        * * * * *
for i in range(5):                                 # * * * * *
    for j in range(5):                             # * * * * *
        print("*",end=" ")                         # * * * * *
    print()                                        # * * * * *

# Pattern-2(Right angle triangle)                  *
for i in range(5):                               # * *
    for j in range(i):                           # * * *
        print("*",end=" ")                       # * * * *
    print()                                      # * * * * *
                                                 # * * * * * *


# Pattern-3(reverse right angle triangle)
n=4
for i in range(n):                               # * * * *     
    for j in range(i):                           # * * *
        print("*",end=" ")                       # * *
    print()                                      # *

# Pattern-4                                     
n = 5                                           #         *
star = 1                                        #       * *
space = n-1                                     #     * * *
for i in range(n):                              #   * * * *
    for j in range(space):                      # * * * * *
        print(" ",end=" ")
    for j in range(star):
        print("*",end=" ")
    print()
    space -= 1
    star += 1

# Pattern-5:
n = 4
star = n
space = 0
for i in range(n):
    for j in range(space):
        print(" ",end=" ")
    for j in range(star):
        print("*",end=" ")
    print()
    star -= 1
    space += 1 

# Pattern-6:
n = 5
space = n//2
star = 1
for i in range(n):
    for j in range(space):
        print(" ",end=" ")
    for j in range(star):
        print("*",end=" ")
    if i < n//2:
        space -= 1
        star += 2
    else:
        space += 1
        star -= 2
    print()
                         
# Pattern-7:
n = 5                               # * * *   * * * 
star = n//2 + 1                     # * *       * *           
space = 1                           # *           *            
for i in range(n):                  # * *       * *                       
    for j in range(star):           # * * *   * * *                             
        print("*",end=" ")                                    
    for j in range(space):                                        
        print(" ",end=" ")                                         
    for j in range(star):                                                  
        print("*",end=" ")                                                 
    if i < n//2 :                                                  
        star -= 1
        space += 2
    else:
        star += 1
        space -= 2
    print()
                          
# Pattern-8:
n = 5
for i in range(n):
    for j in range(n):
        if i == j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# Pattern-9:
n = 5
for i in range(1,n+1):
    for j in range(1,n+1):
        if i + j == n + 1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# Pattern-10:
n = 5                                                   # *       * 
for i in range(1,n+1):                                  #   *   *   
    for j in range(1,n+1):                              #     *     
        if i == j or i + j == n + 1:                    #   *   *   
            print("*",end=" ")                          # *       *
        else:
            print(" ",end=" ")
    print()

    

