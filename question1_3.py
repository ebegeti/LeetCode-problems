#Design an algorithm and write code to remove the duplicate characters in a string without using any additional buffer. NOTE: One or two additional variables are fine. An extra copy of the array is not.
#FOLLOW UP
#Write the test cases for this method.

def removeDuplicates(st='abc'):
    
    # String length cannot be more than
    # 256.
    if len(st) > 256:
        return False
    
    # Initialize occurrences of all characters
    char_set = [False] * 128
    lista=[]
    for i in range(0,len(st)):
        lista.append(st[i])
    
    # For every character, check if it exists
    # in char_set
    for i in range(0, len(st)-1):
        # Find ASCII value and check if it
        # exists in set.
        val = ord(st[i])
        if char_set[val]: #otan sinantisei 2i fora ton idio xaraktira
            lista.remove(lista[i])
        
        char_set[val] = True
    
    return ''.join(lista)

# driver code
st = "abcdabdeff"
print(removeDuplicates(st))
