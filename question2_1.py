#Implement an algorithm to determine if a string has all unique characters. What if you can not use additional data structures?

def isUniqueChars(st='abc'):
    
    # String length cannot be more than
    # 256.
    if len(st) > 256:
        return False
    
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
#st = "abcd"
#print(isUniqueChars(st))
