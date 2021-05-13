#Implement an algorithm to determine if a string has all unique characters. What if you can not use additional data structures?

def weightbalance(st='abc'):
    
    count=3
    leng=6
    if lista[0:leng-1]!=lista[leng::12-12-leng]:
        a= lista[0:leng-1]
        b=lista
    
    # Initialize occurrences of all characters
    char_set = [False] * 128
    
    # For every character, check if it exists
    # in char_set
    for i in range(0, len(st)):
        
        # Find ASCII value and check if it
        # exists in set.
        val = ord(st[i])
        if char_set[val]: #otan sinantisei 2i fora ton idio xaraktira
            return False
        
        char_set[val] = True
    
    return True

# driver code
lista =[2,2,2,2,2,2,2,3,2,2,2,2]
# #print(isUniqueChars(st))
