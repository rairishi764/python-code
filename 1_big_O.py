#
# omega- bestcase  
# theta - avg case
# macron- worst case (Big 0 scenario)
# https://www.bigocheatsheet.com/

def print_items (n):     
    for i in range(n):   # O(n) - runs n times
        print(i)

    for i in range(n):   # O(n pow 2) - runs n*n times 
        for j in range (n):
            print(i,j)

def print_items_1 (a,b):
    for i in range(a):   # O(a) - runs a times
        print(i)
    for j in range(b):   # O(b) - runs b times
        print(i)         # O(a) +O(b) = O(a+b)  
    
    for i in range(a):   # O(a*b) - runs a*b times 
        for j in range (b):
            print(i,j)

# Big O of lists
# insertion at begining is O(n) as reindexing of allitems has to happen
# insertion at end is O(1) 
# search is O(n)
#
#

print_items(10)   # O(n),
                  # nested loop O(n pow2)                           LOOP WITHIN LOOP
                  # O(1) runs only once                             CONSTANT
                  # O(logn) ex-split the arr list to 2 and then 2   DIVIDE & CONQUER