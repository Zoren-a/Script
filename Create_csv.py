import csv

fields = ['SM', 'MM', 'shader', 'core', 'spunit', 'l1latency', 'dl2', 'IPC']

with open('Colelcted_data.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)