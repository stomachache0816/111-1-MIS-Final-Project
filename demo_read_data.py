import pymysql
import numpy as np

db = pymysql.connect(host="localhost", user="root", password="willyliao920816", database="new_schema")
cursor = db.cursor()
cursor.execute("SELECT * FROM new_schema.f01l_patent")

L = []

raw = cursor.fetchone()

while raw is not None:
    if raw[22] != '' and raw[1] != '':
        L.append([raw[22], raw[1]])
    raw = cursor.fetchone()

db.close()

print(np.array(L))

for data in L:
    data[0] = data[0][:5]
    data[1] = data[1][:str(data[1]).index(' ')].lower()

print(np.array(L))

X_dictionary = {}
Y_dictionary = {}
X_count = 0
Y_count = 0

for data in L:
    if data[0] not in X_dictionary:
        X_dictionary[data[0]] = X_count
        X_count += 1
    if data[1] not in Y_dictionary:
        Y_dictionary[data[1]] = Y_count
        Y_count += 1

print(X_dictionary)
print(Y_dictionary)

for data in L:
    data[0] = X_dictionary[data[0]]
    data[1] = Y_dictionary[data[1]]

print(np.array(L))

file = open('coordinates_data.txt', 'w')
for data in L:
    file.write(str(data[0]))
    file.write(' ')
    file.write(str(data[1]))
    file.write('\n')
print('Output completed.')
file.close()
