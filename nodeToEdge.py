import csv
import operator

nodeFile = open('nodeid.csv', 'r')
edgeFile = open('edge.csv', 'w')

R = csv.reader(nodeFile)
W = csv.writer(edgeFile)

'''
nodeData = []

for row in R:
    nodeData.append(row)

comfirm = True


while comfirm :
    x,y = input()

    print nodeData[x][y]

    comfirm = input('continue?')
'''

for row in R:
    for i in range(1,20):
        for j in range(i+1, 20):
            if row[i] != '' and row[j] != '':
                if int(row[i]) < int (row[j]):
                    #data = [row[i], row,[j]]
                    data = [row[i], row[j],chr(len(row[i])) + chr(len(row[j])) + row[i] + row[j]]
                    W.writerow(data)
                else:
                    data = [row[j], row[i],chr(len(row[j])) + chr(len(row[i])) + row[j] + row[i]]
                    W.writerow(data)


nodeFile.close()
edgeFile.close()

edgeFile = open('edge.csv', 'r')
edgeFFile = open('edgeFinal.csv', 'w')

R = csv.reader(edgeFile)
W = csv.writer(edgeFFile)

data = ['Source', 'Target', 'Type', 'Id', 'Lable', 'Weight']
W.writerow(data)

sort = sorted(R, key = operator.itemgetter(2))

lastRow = []

nodeData = []

'''
comfirm = True


while comfirm :
    x,y = input()

    print sort[x][y]

    comfirm = input('continue?')
#for row in sort:
print 1 
'''
lastRow = ['', '', '', '', '', '']
i = 0

for row in sort:
    data = [row[0], row[1], 'Undirected', i, '', 1]
    if data[0] == lastRow[0] and data[1] == lastRow[1]:
        lastRow[5] = lastRow[5] + 1
    else:
        W.writerow(lastRow)
        lastRow = data
        i = i+1

edgeFile.close()
edgeFFile.close()
