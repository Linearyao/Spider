from multiprocessing import Pool,Manager
import requests
import time

link_list = []
with open("spider.txt",'r') as file:
    link_list = file.readlines()
    for eachone in link_list:
        link = eachone.split('\t')[0]
        link = link.replace('\n','')
        link_list.append(link)

start = time.time()
def crawler(q,index):
    Process_id = 'Process-' + str(index)
    while not q.empty():
        url = q.get(timeout=2)
        try:
            r = requests.get(url,timeout = 20)
            print(Process_id,q.qsize(),r.status_code,url)
        except Exception as e:
            print(Process_id,q.qsize(),url,'Error:',e)

if __name__ == '__main__':
    manager = Manager()
    workQueue = manager.Queue(1000)

    for url in link_list:
        workQueue.put(url)

    pool = Pool(processes=3)
    for i in range(4):
        pool.apply_async(crawler,args=(workQueue,i))

    print("Started processes")
    pool.close()
    pool.join()

    end = time.time()
    print('Pool + Queue多进程爬虫的总时间为:',end - start)
    print('Main process Ended')
