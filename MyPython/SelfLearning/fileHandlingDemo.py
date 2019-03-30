f = open('myData.txt','r')
import os
print(os.getcwd())


print(f.read())
print(f.readlines())

f1 = open('copiedData.txt','w')


f1.write("This is the new file to copy old file into ")
f1.write('\n')

f = open('myData.txt','r')

for i in f:
    f1.write(i)  

f2 = open('Barca.jpg','rb')

#for j in f2:
    #print(j)
    
f2 = open('Barca.jpg','rb')
f3 = open('copiedPic.jpg','wb')

for k in f2:
    f3.write(k)

import shelve

sf = shelve.open('shelvefile')
sf['Football Clubs'] = ['Barcelona','Arsenal','Girona', 'Sevilla']

sf = shelve.open('shelvefile')
print(sf['Football Clubs'])
sf = shelve.open('shelvefile')
print('Keys are----')
print(list(sf.keys()))
sf = shelve.open('shelvefile')

print('Values are---')
print(list(sf.values()))
sf.close()

#https://1drv.ms/u/s!Amv7MQc0Jhpisl7CDBRf8InwMfDY

'''
    r = read mode
    a = append mode
    w = write mode
    rb/wb = read/write in binary mode
'''