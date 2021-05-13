import re
#o = open("C:\practice_python\chapter1_arrays_strings\output.txt","w")



# function to get unique values
def unique(list1):
    
    # intilize a null list
    unique_list = []
    count=0
    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
        else:
            count+=1
    return unique_list

def clean_list(my_list, exclusion_list):
    
    new_list = []
    for i in my_list:
        if i in exclusion_list:
            continue
        else:
            new_list.append(i)
    
    return new_list

data = open("C:\practice_python\chapter1_arrays_strings\log_files.txt").read()
logs=data.split('\n')
tests=[]
uniquetests=[]
for each in logs:
    test_no=each[29:33]
    tests.append(test_no)

uniquetests=unique(tests)
sanitytests=['5828','5829','5830','5831','5832','5833','5833','5834','5835','5836','5837','5838','5839','5840','5841','5842','5845','5872', \
             '6297','6846','7143','7144','7301','7302','7311','7391','7408','6301','6302','6303','6304','6305','6306','6307','6308','6309', \
             '6310','6311','6312','6313','6314','6315','6316','6317','6318','6320','6565','6566','6564','7149','7150','7158','7186','7290', \
             '7303','7309','7310','7300','7304','7396','7299','7465','7526','6324','6325','6298','6439','6440','6440','6441','6442','6443', \
             '6444','6445','6446','6447','6448','6449','6450','6451','6452','6461','6462','6463','6326','6327','6328','6329','6330','6331', \
             '6332','6333','6334','6335','6336','6337','6338','6339','6340','6341','6342','6561','6562','6563','7278','7288','7283','7295'\
             '7297','7307','7308','7153','7285','7277','7289','7223','7297','7298', '7185', '7147', '7305', '6830','7243', '5344', '5346', \
             '5362', '6319', '6836','5356', '5357', '5359', '5363', '5364', '5844', '6572', '6721', '6837', '7126', '7130', '7313', '7315',\
             '7316', '7317', '7318', '7319', '7320', '7321', '7322', '7323', '7324', '7325', '7326', '7327', '7328', '7329', '7330', '7331',\
             '7332', '7333','7188', '7189', '7190', '7191','7146','7284', '7225', '7226', '7227', '7228', '7229', '7230', '7231', '7232',\
             '7233', '7234', '7235', '7236','7422','7425','7460','7462','7490', '7491', '7492','6453', '7509', '7516', '7517', '7518', ''\
             ]
regressiontests=clean_list(uniquetests,sanitytests)

print(tests)
print(len(tests))
print(uniquetests)
print(len(uniquetests))
print(regressiontests)
print(len(regressiontests))

