digit = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine',
          10: 'Ten'}
teens ={10:'Ten',11:'Eleven',12:'Twelve',13:'Thirteen',14:'Fourteen',15:'Fifteen',16:'Sixteen',17:'Seventeen',18:'Eighteen',19:'Nineteen'}
dozens={2:'Twenty',3:'Thirty',4:'Forty',5:'Fifty',6:'Sixty',7:'Seventy',8:'Eighty',9:'Ninety'}


def numberToWords( num: int) -> str:

    pos_nums = []
    while num != 0:
        pos_nums.append(num % 10)
        num = num // 10

    pos_nums=pos_nums[::-1]
    print(pos_nums)
    output=''
    if len(pos_nums) > 9 and len(pos_nums) <= 12:
        billions=''
        c=0
        for each in pos_nums[:len(pos_nums)-9]:
            billions += str(each)
            c+=1
        pos_nums = pos_nums[c:]
        if int(billions) != 0:
            output = output+convert(billions) + " Billion "
        #pos_nums = pos_nums[:9]

    if len(pos_nums) > 6 and len(pos_nums) <= 9:
        millions=''
        c=0
        for each in pos_nums[:len(pos_nums)-6]:
            millions += str(each)
            c+=1
        pos_nums = pos_nums[c:]
        if int(millions) != 0:
            output = output + convert(millions) + " Million "
        #pos_nums = pos_nums[:6]

    if len(pos_nums) > 3 and len(pos_nums) <= 6:
        thousands=''
        c=0
        for each in pos_nums[:len(pos_nums)-3]:
            thousands += str(each)
            c+=1
        pos_nums = pos_nums[c:]
        if int(thousands)!=0:
            output = output + convert(thousands) + " Thousand "
        #pos_nums = pos_nums[:3]
    output = output + convert(''.join(str(x) for x in pos_nums))
    print(output)
    return output

def convert(pos_nums):
    output=''
    if len(pos_nums) == 3:
        if int(pos_nums[0])!=0:
            output += digit[int(pos_nums[0])] + " Hundred"
        pos_nums = pos_nums[1:3]
    dekades=int(pos_nums) // 10
    monades=int(pos_nums)%10
    if dekades== 0:
        if monades!=0:
            output += " " + digit[int(pos_nums)]
    elif dekades==1:
        output += ' '+teens[int(pos_nums)] + ' '
    else:
        output +=' '+dozens[int(pos_nums[0])]
        if '0' not in pos_nums:
            output += ' '+digit[int(pos_nums[1])]
    return output


numberToWords(1000000)