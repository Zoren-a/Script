import csv

fields = ['SM', 'MEM', 'Shader_reg', 'Shared_mem', 'DL1', 'DL2']

with open('Colelcted_data.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)