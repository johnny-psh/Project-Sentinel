from sklearn import svm
from sklearn.model_selection import train_test_split
import csv
import sys
import numpy as np
import socket
import re

f = open('information.csv','r')
reader = csv.reader(f)
Statement = []

for row in reader:
    wordAscii = ""
    conArray = []
    word = ''.join(row)
    wordArray = list(word)
    
#float64 crashed at 310. Test if it exceeds!
    for count in range(len(wordArray)):
        wordAscii += str(ord(wordArray[count]))
    if (len(wordAscii) < 310):
        conArray.append(wordAscii)
        Statement.append(conArray)
  

labels = []
for num in range(378):
    labels.append(0)
for num in range(70903):
    #1000
    labels.append(1)

X_train, X_test, y_train, y_test = train_test_split(Statement,labels, test_size=0.2, random_state=0)

clf = svm.SVC()
clf = clf.fit(X_train, y_train)

print(clf.score(X_test,y_test))

#create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#bind the socket to a public host,
# and a well-known port
serversocket.bind(("", 8080))
#become a server socket
serversocket.listen(5)

while True:
    connection, address = serversocket.accept()
    test = connection.recv(309)
    testArray = list(test)
    testAscii = ""
    for count in range(len(testArray)):
        testAscii += str(ord(testArray[count]))
    if(len(testAscii) < 310):
            try:
                print(clf.predict(testAscii))
                connection.send(np.array2string(clf.predict(testAscii)))
            except:
                pass
    else:
        connection.send("b")
    