'''
Created on 08-Apr-2019

@author: guruk
'''
from selenium import webdriver
import bs4, requests
from time import sleep

browser = webdriver.Firefox(executable_path=r'C:\Users\guruk\Downloads\Compressed\geckodriver.exe')
browser.get('https://www.amazon.in/')

searchelem = browser.find_element_by_css_selector('#twotabsearchtextbox')
searchelem.send_keys('Calcutta by Nemai Ghosh')
searchelem.submit()

sleep(5)
curr_url = str(browser.current_url)


def getAmazonPrice(URL):
    
    res = requests.get(URL, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36"})
    res.raise_for_status()
    
    soup = bs4.BeautifulSoup(res.text,'html.parser')
    elem = soup.select('div.s-result-item:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > a:nth-child(1) > span:nth-child(1) > span:nth-child(2) > span:nth-child(2)')
    return elem[0].text.split()

price = getAmazonPrice(curr_url)
print('The price of the product on Amazon.in is: ', price[0]) 
