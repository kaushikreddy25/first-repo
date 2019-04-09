'''
Created on 08-Apr-2019

@author: guruk
'''
import bs4, requests


def getAmazonPrice(URL):
    
    res = requests.get(URL, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36"})
    res.raise_for_status()
    
    soup = bs4.BeautifulSoup(res.text,'html.parser')
    elem = soup.select('#soldByThirdParty > span.a-size-medium.a-color-price.inlineBlock-display.offer-price.a-text-normal.price3P')
    return elem[0].text.split()

price = getAmazonPrice('https://www.amazon.in/gp/product/9350296063/ref=ox_sc_saved_title_1?smid=APLYOO3IHSCW0&psc=1')
print('The price of the product on Amazon.in is: ', price[0]) 