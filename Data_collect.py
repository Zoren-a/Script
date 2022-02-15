import re
import sys
import csv 

file_name = sys.argv[1]
a = file_name[:-4].split('_')
print(a)

with open(file_name, mode='r') as in_file:
    # data = in_file.read()
    r1 = re.findall(r"gpu_tot_ipc.*",in_file.read())
    # print(r1)
    x = r1[0].split()

with open('Colelcted_data.csv', 'a') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow((a[1],a[2],a[3],a[4],a[5],a[6],x[-1]))