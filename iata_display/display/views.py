import pandas as pd
from django.shortcuts import render
import csv
# Create your views here.
def getfile(request):
    '''
    #csv_file = request.FILES['D:\Internship/airport_info.csv']
    file_reader = pd.read_csv("D:\Internship/airport_info.csv", encoding='latin1')
    #print(file_reader.head())
    #print(file_reader['iata'].dtypes)
    lines = file_reader.split("\n")
    for line in lines:
        fields = line.split(",")
        print(fields)
    return render(request, 'home.html')
    '''
    csv_file = open('airport_info.csv', 'r')
    csv_reader = csv.reader(csv_file)

    # the loop
    data = []
    for line in csv_reader:
        next(csv_reader)
        #print(line[2])
        row=[]
        for i in range(5):
            row.append(line[i])
        data.append(row)
    return render(request, 'home.html',  {'list': data})