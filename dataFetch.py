import requests
from bs4 import BeautifulSoup

def lastTradedPrice(ticker):
    page = requests.get("https://in.finance.yahoo.com/quote/"+ticker)
    soup = BeautifulSoup(page.content, 'html.parser')
    val = soup.findAll("span", {"class": "Trsdu(0.3s) Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(b)"})
    if len(val) >=1 :
        return val[0].get_text()
    else:
        return "Invalid Request"

def marketCap(ticker):
    page = requests.get("https://in.finance.yahoo.com/quote/"+ticker)
    soup = BeautifulSoup(page.content, 'html.parser')
    val = soup.findAll("td", {"class": "Ta(end) Fw(600) Lh(14px)"})
    if len(val) >=1 :
        return val[8].get_text()
    else:
        return "Invalid Request"

def previousClose(ticker):
    page = requests.get("https://in.finance.yahoo.com/quote/"+ticker)
    soup = BeautifulSoup(page.content, 'html.parser')
    val = soup.findAll("td", {"class": "Ta(end) Fw(600) Lh(14px)"})
    if len(val) >=1 :
        return val[0].get_text()
    else:
        return "Invalid Request"

def openPrice(ticker):
    page = requests.get("https://in.finance.yahoo.com/quote/"+ticker)
    soup = BeautifulSoup(page.content, 'html.parser')
    val = soup.findAll("td", {"class": "Ta(end) Fw(600) Lh(14px)"})
    if len(val) >=1 :
        return val[1].get_text()
    else:
        return "Invalid Request"

def daysRange(ticker):
    page = requests.get("https://in.finance.yahoo.com/quote/"+ticker)
    soup = BeautifulSoup(page.content, 'html.parser')
    val = soup.findAll("td", {"class": "Ta(end) Fw(600) Lh(14px)"})
    if len(val) >=1 :
        return val[4].get_text()
    else:
        return "Invalid Request"

def fiftyTwoRange(ticker):
    page = requests.get("https://in.finance.yahoo.com/quote/"+ticker)
    soup = BeautifulSoup(page.content, 'html.parser')
    val = soup.findAll("td", {"class": "Ta(end) Fw(600) Lh(14px)"})
    if len(val) >=1 :
        return val[5].get_text()
    else:
        return "Invalid Request"

def volume(ticker):
    page = requests.get("https://in.finance.yahoo.com/quote/"+ticker)
    soup = BeautifulSoup(page.content, 'html.parser')
    val = soup.findAll("td", {"class": "Ta(end) Fw(600) Lh(14px)"})
    if len(val) >=1 :
        return val[6].get_text()
    else:
        return "Invalid Request"

def peRatio(ticker):
    page = requests.get("https://in.finance.yahoo.com/quote/"+ticker)
    soup = BeautifulSoup(page.content, 'html.parser')
    val = soup.findAll("td", {"class": "Ta(end) Fw(600) Lh(14px)"})
    if len(val) >=1 :
        return val[10].get_text()
    else:
        return "Invalid Request"

def dividend(ticker):
    page = requests.get("https://in.finance.yahoo.com/quote/"+ticker)
    soup = BeautifulSoup(page.content, 'html.parser')
    val = soup.findAll("td", {"class": "Ta(end) Fw(600) Lh(14px)"})
    if len(val) >=1 :
        return val[13].get_text()
    else:
        return "Invalid Request"

def change(ticker):
    page = requests.get("https://in.finance.yahoo.com/quote/"+ticker)
    soup = BeautifulSoup(page.content, 'html.parser')
    val = soup.findAll("div", {"D(ib) Va(t) W(48%) BdEnd Bdc($seperatorColor) Pend(6px)"})
    if len(val) >=1 :
        return val[0].get_text()
    else:
        return "Invalid Request"

def summary(ticker):
    message = 'LTP => ' + lastTradedPrice(ticker) + '\nChange => ' + change(ticker) + '\nOpen => ' + openPrice(ticker)  +'\nPrev. Close => ' + previousClose(ticker) + '\nVolume => ' + volume(ticker) + '\nRange(Today) => ' + daysRange(ticker) + '\nRange(52 wk.) => ' + fiftyTwoRange(ticker) + '\nMarket Cap. => ' + marketCap(ticker) + '\nP/E => ' + peRatio(ticker) + '\nDividend => ' + dividend(ticker)
    return message
