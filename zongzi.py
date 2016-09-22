#-*- coding:utf-8 -*-
#tr:nth-of-type(6) td a
#wrapper > div > table > tbody > tr:nth-of-type(1) > td > div.tail > a
#tr:nth-of-type(1) td a.title
from bs4 import BeautifulSoup
import requests
import random
import time

def get_url_all():
    url_list = []
    for x in xrange(1,12):
        url = 'http://www.btmeet.net/search/大桥未久/{}-1.html'.format(x)
        url_list.append(url)
    return url_list



header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    'Cookie': '__cfduid=d6037f130c36da1e034baf47ebe19afe41473237773; _xz=UxNrR+IhqMzHcdaS6M53WkaDJXli9jap+Sah45g6LGz1Kb8rDLzI1nlVHj7oAp+PRXlmpTqyCeSjFLy44o8TQeC3yH9fIb2ysr5XNevSHE0eWsFKbg2CoSnmt4nPGC4YleqV8MqG6BltHLQanwa9gsM9pxt3SqmFXgDqF4khA4OBQV8QrtY9IZ2sl1RafRxF; locale=CN; sys=1; _ga=GA1.2.934017469.1473237707; Hm_lvt_1722c9813dd5f42628a989c4b0de178f=1473237707,1473238087; Hm_lpvt_1722c9813dd5f42628a989c4b0de178f=1473238748'

    }



def get_url(url,header):


    source_code = requests.get(url,headers = header)
    soup = BeautifulSoup(source_code.text,'lxml')
    souce_url = 'http://www.btmeet.net'
    downloadlinks = []


    for pic_url in soup.select('.item-title h3 a'):
        url_of_page = souce_url + pic_url.get('href')
        downloadlinks.append(url_of_page)
        #print url_of_page
    return downloadlinks

def main():

    url_list = get_url_all()
    all_links = []
    for i in url_list:
        downloadlinks = get_url(str(i),header)
        for item in downloadlinks:
            try:
                all_links.append(item)
                time.sleep(5)
                #print item
                source_code = requests.get(item,headers=header)
                soup = BeautifulSoup(source_code.text, 'lxml')
                print soup.select('.panel-body a')[0].get('href')
                tag = soup.select('.fileDetail div.panel-body p a')[:-1]
                for item in tag:
                    print item.text.strip()
            except (requests.exceptions.ConnectionError,NameError):
                print 'Lost One'
                pass








main()
# source_code = requests.get('http://www.btmeet.net/wiki/579b70d4b75236a34ce63abd826fc70521b95cdd.html', headers=header)
# soup = BeautifulSoup(source_code.text, 'lxml')
# print soup.select('.panel-body a')[0].get('href')
# tag =  soup.select('.fileDetail div.panel-body p a')[:-1]
# for item in tag:
#     print item.text.strip()
##wall > div.fileDetail > div:nth-child(4) > div.panel-body










