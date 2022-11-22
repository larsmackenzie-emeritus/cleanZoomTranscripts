import os

def clean_data_file(file, newfile):
    f = open(file, "r")
    lines = f.readlines()
    f.close()
    newlines = []
    for l in lines:
        l = l.split()
        l = list(filter(lambda x: '0' not in x, l))
        l = list(filter(lambda x: '-->' not in x, l))
        l = l[2:]
        l = " ".join(l)
        l = l + "\n"
        newlines.append(l)
   
    f = open(newfile, "w")
    f.writelines(newlines)
    f.close()



path = os.getcwd()
raw_folder=path + '\\raw\\'
clean_folder=path+'\\clean\\'
files = os.listdir(raw_folder)
for fname in files:
    file_name =fname[:-4]
    newfile = clean_folder+file_name+'_clean.txt'
    print('new '+ newfile)
    clean_data_file(raw_folder+fname, newfile)


