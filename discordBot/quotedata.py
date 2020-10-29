import random
import bs4
import requests
import webbrowser

import xlsxwriter

wb = xlsxwriter.Workbook("database_quotes.xlsx")
sheet1 = wb.add_worksheet('Sheet1')

def scrap_quotes():
    print("Downloading Webpage")
    website = 'https://www.goodreads.com'
    url = 'https://www.goodreads.com/quotes/tag/Inspirational'
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text,'html.parser')
    quoteElem = soup.select('.quoteText')
    print(len(quoteElem))
    for x in range(1):
        nextLink = soup.select('a[rel="next"]')[0]
        temp_url = website + nextLink.get('href')
        res_temp = requests.get(temp_url)
        soup_temp = bs4.BeautifulSoup(res_temp.text,'html.parser')
        quoteElem = quoteElem + (soup_temp.select('.quoteText'))
        res = requests.get(temp_url)
        soup = bs4.BeautifulSoup(res.text,'html.parser')
        print(len(quoteElem))

    for x in range(len(quoteElem)):
        quote_text = quoteElem[x].find('br').previousSibling
        quote_author = quoteElem[x].find('span').contents[0]
        sheet1.write(x,0,quote_text)
        sheet1.write(x,1,quote_author)

    number = random.randint(0,len(quoteElem)-1)
    quote_text = quoteElem[number].find('br').previousSibling
    quote_author = quoteElem[number].find('span').contents[0]

    wb.close()

scrap_quotes()
