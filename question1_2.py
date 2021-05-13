#Write code to reverse a C-Style String. (C-String means that “abcd” is represented as five characters, including the null character.)

def reverseCstring(st='abc'):
    
    original=st[:-1]
    reversed=original[::-1]
    print(reversed)

#driver code
st = "abcd\0"
print(reverseCstring(st))
