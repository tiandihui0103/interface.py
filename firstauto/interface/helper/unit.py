import csv,sys
def makeCsvData(dataPath):
    data=[];
    for value in csv.reader(open(dataPath,"r",encoding='UTF-8')):
        data.append(value);
    return data;