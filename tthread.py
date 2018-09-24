#encoding=utf-8

import threading
import urllib2
import requests

class FetchUrls(threading.Thread):
    def __init__(self, urls, output, lock):
        threading.Thread.__init__(self)
        self.urls = urls
        self.output = output
        self.lock = lock

    def run(self):
        while self.urls:
            self.lock.acquire()
            print 'lock ac by {}'.format(self.name)
            url = self.urls.pop()
            text = requests.get(url).text
            text = text.encode('utf-8')
            self.output.write(text)
            self.output.write(url.center(40, '*'))
            # print url.center(80, '&')
            # print text
            print 'write done by {} from {}'.format(self.name, url)
            print 'lock re by {}'.format(self.name)
            self.lock.release()

def main():
    lock = threading.Lock()
    urls1 = ['https://www.baidu.com', 'https://www.douban.com']
    urls2 = ['https://www.zhihu.com', 'https://www.liaoxuefeng.com']
    f = open('output', 'w+')
    t1 = FetchUrls(urls1, f, lock)
    t2 = FetchUrls(urls2, f, lock)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    f.close()

if __name__ == '__main__':
    main()



