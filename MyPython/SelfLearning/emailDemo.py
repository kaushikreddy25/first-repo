'''
Created on 10-Apr-2019

@author: guruk
'''
import smtplib

conn = smtplib.SMTP('smtp.gmail.com', 587)

conn.ehlo()
conn.starttls()

conn.login('gurukaushik92@gmail.com', 'apdjpagfrmawajlr')

conn.sendmail('gurukaushik92@gmail.com', 'guru.kaushik@hotmail.com', 'Subject: Sending mail from Python... \n\n Dear Kaushik, \n I just learnt how to send a n email from Python. Let\'s keep going \n\n-K ')

conn.quit()

