from multiprocessing import Process,Queue
import time

import crawler as crawler
import requests

link_list = []
with open('list.txt','r') as file:
    file_list = file.readlines()
    for eachone in file_list:
        link = eachone.split('\t')[1]
        link = link.replace('\n','')
        link_list.append(link)

start = time.time()
class MyProcess(Process):
    def __init__(self,q):
        Process.__init__(self)
        self.q = q

    def run(self):
        print("starting",self.pid)
        while not self.q.empty():
            crawler(self.q)
        print("Exiting",self.pid)

    def crawler(q):
        url = q.get(timeout = 2)
        try:
            r = requests.get(url,timeout=20)
            print(q.qsize(),r.status_code,url)
        except Exception as e:
            print(q.qsize(),url,'Error:',e)

        if __name__ == '__main__':
            ProcessNames = ["Process-1","Process-2","Process-3"]
            workQueue = Queue(1000)#创建工作队列

            for url in link_list:
                workQueue.put(url)#将url从队列中提取出来

            for i in range(0,3):
                p = MyProcess(workQueue)
                p.daemon = True
                p.start()
                p.join()

        end = time.time()
        print('Process + Queue多进程爬虫时间为：',end-start)
        print('Main process Ended!')
