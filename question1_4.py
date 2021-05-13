#Write a method to decide if two strings are anagrams or not.

def isAnagram(st1,st2):
    if len(st1)!=len(st2): return False
    if sorted(st1)==sorted(st2):
        return True
    else:
        return False
    
# driver code
st1 = "ads"
st2='das'
print(isAnagram(st1,st2))
