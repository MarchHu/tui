from bs4 import BeautifulSoup
import requests
import random

proxy_list = [
    'http://124.88.67.54:843',
    'http://120.25.163.76:3128',
    'http://119.88.128.78:80',
    ]
proxy_ip = random.choice(proxy_list)
proxies = {'http': proxy_ip}
def get_url():
    url_list = []
    for x in xrange(2,10):
        url = 'http://www.xiumm.cc/albums/page-{}.html'.format(x)
        url_list.append(url)
    return url_list



header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    'Cookie': '_7cpf_num=3; JXM732324=1; JXD732324=1; _gat=1; __qiqi__view_plan8126=%2C392; __qiqi__view_ads8126=%2C451%2C452; _ga=GA1.2.62828979.1473231814'

    }



def tui_girl_spider(url,header):


    source_code = requests.get(url,headers = header,proxies = proxies)
    soup = BeautifulSoup(source_code.text,'lxml')
    downloadlinks = []

    #
    # for pic_url in soup.find_all('img'):
    #     pic_link = pic_url.get('src')
    #     downloadlinks.append(pic_link)
    #     print pic_link
    for pic_url in soup.select('.pic_box td a img'):
        pic_link = pic_url.get('src')
        downloadlinks.append(pic_link)
        print pic_link

    for i,j in enumerate(downloadlinks):
        # with open('D:/workspaceOfML/learningspider/pic/{0}.jpg'.format(i),'wb') as file:
        with open('D:/workspaceOfML/learningspider/tui/{0}'.format(str(j[-21:])), 'wb') as file:
            file.write(requests.get(j).content)


if __name__ == '__main__':
    url_list = get_url()
    for url in url_list:
        print url
        tui_girl_spider(url,header)

    print 'Done'





