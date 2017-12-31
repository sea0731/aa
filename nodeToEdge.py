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
                    data = [row[i], row[j]]
                    W.writerow(data)
                else:
                    data = [row[j], row[i]]
                    W.writerow(data)


nodeFile.close()
edgeFile.close()

edgeFile = open('edge.csv', 'r')
edgeFFile = open('edgeFinal.csv', 'w')

R = csv.reader(edgeFile)
W = csv.writer(edgeFFile)

sort = sorted(R, key = operator.itemgetter(0))

lastRow = []

nodeData = []

for row in sort:
    nodeData.append(row)

comfirm = True


while comfirm :
    x,y = input()

    print sort[x][y]

    comfirm = input('continue?')
#for row in sort:
    

edgeFile.close()
edgeFFile.close()
