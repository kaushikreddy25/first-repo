'''
Created on 05-Apr-2019

@author: guruk
'''
import requests

down = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print('Status of download: ', down.status_code) #404 for error, 200 for complete
print('Size of downloaded file is: ', len(down.text))

#Following method will raise an error if download failed
print(down.raise_for_status())

downloadFile = open('RomeoAndJuliet.txt','wb')

for piece in down.iter_content(50000):
    downloadFile.write(piece)

readFile = open('RomeoAndJuliet.txt','r')
'''
for i in readFile:
    print(i)
'''