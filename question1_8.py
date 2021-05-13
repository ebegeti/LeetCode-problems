#Assume you have a method isSubstring which checks if one word is a substring of another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring (i.e., “waterbottle” is a rotation of “erbottlewat”).
def isSubstring(big,small):
    if big.find(small)>=0:
        return True
    else:
        return False
    
def isRotation(s1,s2):
    leng=len(s1)
    if leng==len(s2) and leng>0:
        s1s1=s1+s1
        return isSubstring(s1s1,s2)
    return False

# driver code
if __name__ == "__main__":
    pairs=dict()
    pairs={"apple": "pleap", "waterbottle": "erbottlewat", "camera": "macera"}
    for id,val in pairs.items():
        word1=id
        word2=val
        print(isRotation(word1,word2))
    
        