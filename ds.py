#! -*- coding:utf-8 -*-
import requests
from lxml import etree
from multiprocessing.dummy import Pool as ThreadPool
import commands

head = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64)'}

def movie_links(url):
    #print url
    html = requests.get(url, headers=head,verify=False)
    print html
    selector=etree.HTML(html.content)
    print selector
    contener = selector.xpath('/html/body/div[1]/video/source/@src')

    data = []
    for each in contener:

        look_url = requests.get(url=each,headers=head,verify=False)
        print look_url
        selector_2 = etree.HTML(look_url.text)

        for s in selector_2:
            try:
                down =  s.xpath('//*[@id="videocont"]/div[2]/iframe/@src')[0].split("id=")[1].split('?')[0]
                if  len(down) != 0: 
                    data.append(down)
            except Exception:
                pass

    ids = list(set(data))
    import time
    #d = time.strftime('%Y-%m-%d-%H:%M:%S')
    #commands.getoutput('mkdir/tmp/%s' % str(d))
    for i in ids:
        print i
        print commands.getoutput("cd /tmp/ && axel -n 10 %s" % (i.replace('https','http')))

if __name__ == "__main__":
    page = []
    for s in xrange(1,2):
        newpage = "https://cherry-porn.com/page/" + str(s)
        page.append(newpage)
    pool = ThreadPool(10)
    results = pool.map(movie_links,page)
