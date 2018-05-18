import glob
filelist = (glob.glob('C:\\Users\\p.mykhailyk\\Seafile\\p4ne_training\\config_files\\*.txt'))
#print(filelist)
Total_list = []
for ff in filelist:
    fw = open(ff)
    lines = list(fw)
    for string in lines:
        pos = string.find('ip address')
        if pos > 0:
            small_1 = string[int(pos):]
            small_2 = small_1.replace('ip address', '')
            small_3 = small_2.strip()
            Total_list = Total_list + [small_3]

for ipa in Total_list:
    print(ipa)