f = open('myData.txt','r')

print(f.read())

f1 = open('copiedData.txt','w')


f1.write("This is the new file to copy old file into ")
f1.write('\n')

f = open('myData.txt','r')

for i in f:
    f1.write(i)  

f2 = open('Barca.jpg','rb')

for j in f2:
    print(j)
    
f2 = open('Barca.jpg','rb')
f3 = open('copiedPic.jpg','wb')

for k in f2:
    f3.write(k)




'''
    r = read mode
    a = append mode
    w = write mode
    rb/wb = read/write in binary mode
'''