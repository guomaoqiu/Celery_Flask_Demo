#! -*- coding:utf-8 -*-
import requests
from lxml import etree
from multiprocessing.dummy import Pool as ThreadPool
# import commands
import sys
reload(sys)
sys.setdefaultencoding("UTF-8")


head = {'User-Agent':'Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'}

def movie_links(url):
    print url
    html = requests.get(url, headers=head,verify=False)
    #print html.content
    selector = (etree.HTML(html.text))
    #print html.text
    contener = selector.xpath('//div[@class="box movie_list"]/ul/li/a/@href')
    #print contener
    for each_url in contener:
        print each_url
        look_url = "https://www.137vod.com" + each_url
        try:
            result = requests.get(url=look_url, headers=head,verify=False)
        except Exception,e:
            print e
            continue


        with open('/tmp/a.txt',"a+") as f:
            f.write(result.text)




if __name__ == "__main__":
    page = []
    for s in xrange(2,195):
        newpage = "https://www.137vod.com/Html/60/index-" + str(s)  + ".html"
        page.append(newpage)
    pool = ThreadPool(100)

    results = pool.map(movie_links,page)
