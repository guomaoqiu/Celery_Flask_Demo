from multiprocessing.dummy import Pool as ThreadPool

def movie_links(url):
    print url

    import os
    print os.system('cd /data/movie/ && axel -n 10  %s' % str(url))

if __name__ == "__main__":
    page = []
    with open('vers2.txt', "r") as f:
        for each_line in f.readlines():
            print each_line
            #newpage = each_line
            page.append(each_line)
        pool = ThreadPool(50)
        results = pool.map(movie_links,page)




    #print f.readlines()
