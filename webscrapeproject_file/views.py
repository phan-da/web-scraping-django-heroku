from django.shortcuts import render
from bs4 import BeautifulSoup
from urllib.request import urlopen

# Create your views here.
def home(request):
    return render(request,'home.html')
def itjob(request):
    temp_position_name = list()
    temp_location = list()
    html = urlopen('https://itviec.com/it-jobs/python-django/ho-chi-minh-hcm')
    soup = BeautifulSoup(html, 'html.parser')
    postings = soup.find_all("div", class_="details")
    for p in postings:
        title = p.find('a').text
        temp_position_name.append(title)
    return render(request, 'itjob.html', context={'context1': temp_position_name, 'context2': temp_location})

def hotwheels(request):
    temp_product_desire_ebay = list()
    html = urlopen('https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw=hot+wheel+redline&_sacat=0&LH_TitleDesc=0&_osacat=0&_odkw=hot+wheel+%2767+camaro')
    soup = BeautifulSoup(html, 'html.parser')
    products = soup.find_all('li', class_='s-item s-item--watch-at-corner')
    for p in products:
        name = p.find('a', class_='s-item__link').text
        price = p.find('span', class_='s-item__price').text
        name_and_price = name + " - "+price
        temp_product_desire_ebay.append(name_and_price)
    return render(request, 'hotwheels.html', context={'product': temp_product_desire_ebay})

def goldprice(request):
    temp_gold_kitco = list()
    html = urlopen('https://www.kitco.com/charts/livegold.html')
    soup = BeautifulSoup(html, 'html.parser')
    data = soup.find_all('div', class_='data-blk chg arrow_up_tsp')
    for d in data:
        value = d.find('span', id="sp-chg-value").text
        percent = d.find('span', id="sp-chg-percent").text
        value_and_percent = "Value:"+value+", percent:"+percent
        temp_gold_kitco.append(value_and_percent)

    data = soup.find_all('div', class_='data-blk chg arrow_down_tsp')
    for d in data:
        value = d.find('span', id="sp-chg-value").text
        percent = d.find('span', id="sp-chg-percent").text
        value_and_percent = "Value:" + value + ", percent:" + percent
        temp_gold_kitco.append(value_and_percent)
    return render(request, 'goldprice.html', context={'goldprice': temp_gold_kitco})