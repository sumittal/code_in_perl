import operator
import csv
import os
import sys


lines = []
line_no = 1
while(line_no <= 7):
    lines.append(sys.stdin.readline())
    line_no += 1

    lst = []
    data = []
    col_names = []

    #########Parsing column names here##########
    temp = lines[0].split(sep=" ")
    lst.append("timestamp")
    lst.append("ORDER")

    for column in temp[2:]:
        try:
            lst.append(column.split(":")[0])
        except:
            lst.append("")
        
    col_names = lst

    #########Parsing rows data here##########
    for line in lines:
        temp = line.split(sep=" ")
        lst = temp[0:2]
        for column in temp[2:]:
            try:
                lst.append(column.split(":")[1])
            except:
                lst.append("")
        data.append(lst)

########Function to write data in CSV##########
def csv_writer(data):
    """
    Write data to a CSV file path
    """
    with open(os.path.join(os.getcwd(),"data.csv"), "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(col_names)
        for line in data:
            writer.writerow(line)

########Function to write data in CSV##########
def csv_sort():
    """
    Write data to a CSV file path
    """
    data = csv.reader(open('data.csv'),delimiter=';')
    sortedlist = sorted(data, key=operator.itemgetter(-1), reverse=True)
    print(sortedlist)
    
csv_writer(data)
csv_sort()
