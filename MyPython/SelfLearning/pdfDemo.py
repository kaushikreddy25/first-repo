'''
Created on 10-Apr-2019

@author: guruk
'''
#! python3

#Lesson 44

import os
import PyPDF2


os.chdir('W:\\Python\\Programs')
pdfFile = open('Assignment.pdf','rb')

reader = PyPDF2.PdfFileReader(pdfFile)

print(reader.numPages)

page = reader.getPage(0)

print(page.extractText())

for PageNum in range(reader.numPages):
    print('--------->>>>>>>>Page Number is<<<<<<<<----------', PageNum+1)
    print(reader.getPage(PageNum).extractText())


#for editing pdfs at Page level see the lesson video.