#Write a method to replace all spaces in a string with ‘%20’.

def replaceSpaces(st):
    st=st.replace(" ","%20")
    return st


# driver code
st = "abc dabd eff"
print(replaceSpaces(st))
