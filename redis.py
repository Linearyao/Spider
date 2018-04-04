import requests
from bs4 import BeautifulSoup
import re
import time
from redis import Redis

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}


def push_redis_list():
    r = Redis(host='IP', port=6379)
    print(r.keys('*'))

    link_list = []
    with open('websit.txt', 'r') as file:
        file_list = file.readlines()
        for eachone in file_list:
            link = eachone.split('\t')[1]
            link = link.replace('\n', '')
            link_list.append(link)
            if len(link_list) == 100:
                break

    for url in link_list:
        response = requests.get(url, headers=headers, timeout=20)
        soup = BeautifulSoup(response.text, 'lxml')
        img_list = soup.find_all('img')
        for img in img_list:
            img_url = img['src']
            if img_url != '':
                print("加入的图片url: ", img_url)
                r.lpush('img_url', img_url)
        print('现在图片链接的个数为', r.llen('img_url'))
    return


def get_img():
    r = Redis(host='IP', port=6379)
    while True:
        try:
            url = r.lpop('img_url')
            url = url.decode('ascii')
            try:
                response = requests.get(url, headers=headers, timeout=20)
                name = int(time.time())
                f = open(str(name) + url[-4:], 'wb')
                f.write(response.content)
                f.close()
                print('已经获取图片', url)
            except Exception as e:
                print('爬取图片过程出问题', e)
            time.sleep(3)
        except Exception as e:
            print(e)
            time.sleep(10)
            break
    return


if __name__ == '__main__':
    this_machine = 'master'
    print('开始分布式爬虫')
    if this_machine == 'master':
        push_redis_list()
    else:
        get_img()
        




为什么会产生这样的报错？怎么解决（我的redis6379端口已经开放）
/home/dowhat/PycharmProjects/untitled/venv/bin/python /home/dowhat/PycharmProjects/untitled/createQueue.py
Traceback (most recent call last):
  File "/home/dowhat/PycharmProjects/untitled/venv/lib/python3.5/site-packages/redis/connection.py", line 484, in connect
    sock = self._connect()
  File "/home/dowhat/PycharmProjects/untitled/venv/lib/python3.5/site-packages/redis/connection.py", line 541, in _connect
    raise err
  File "/home/dowhat/PycharmProjects/untitled/venv/lib/python3.5/site-packages/redis/connection.py", line 529, in _connect
    sock.connect(socket_address)
ConnectionRefusedError: [Errno 111] Connection refused

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/dowhat/PycharmProjects/untitled/venv/lib/python3.5/site-packages/redis/client.py", line 667, in execute_command
    connection.send_command(*args)
  File "/home/dowhat/PycharmProjects/untitled/venv/lib/python3.5/site-packages/redis/connection.py", line 610, in send_command
    self.send_packed_command(self.pack_command(*args))
  File "/home/dowhat/PycharmProjects/untitled/venv/lib/python3.5/site-packages/redis/connection.py", line 585, in send_packed_command
    self.connect()
  File "/home/dowhat/PycharmProjects/untitled/venv/lib/python3.5/site-packages/redis/connection.py", line 489, in connect
    raise ConnectionError(self._error_message(e))
redis.exceptions.ConnectionError: Error 111 connecting to 172.16.14.25:6379. Connection refused.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/dowhat/PycharmProjects/untitled/venv/lib/python3.5/site-packages/redis/connection.py", line 484, in connect
    sock = self._connect()
  File "/home/dowhat/PycharmProjects/untitled/venv/lib/python3.5/site-packages/redis/connection.py", line 541, in _connect
    raise err
  File "/home/dowhat/PycharmProjects/untitled/venv/lib/python3.5/site-packages/redis/connection.py", line 529, in _connect
    sock.connect(socket_address)
ConnectionRefusedError: [Errno 111] Connection refused

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/dowhat/PycharmProjects/untitled/createQueue.py", line 65, in <module>
    push_redis_list()
  File "/home/dowhat/PycharmProjects/untitled/createQueue.py", line 13, in push_redis_list
    print(r.keys('*'))
  File "/home/dowhat/PycharmProjects/untitled/venv/lib/python3.5/site-packages/redis/client.py", line 1032, in keys
    return self.execute_command('KEYS', pattern)
  File "/home/dowhat/PycharmProjects/untitled/venv/lib/python3.5/site-packages/redis/client.py", line 673, in execute_command
开始分布式爬虫
    connection.send_command(*args)
  File "/home/dowhat/PycharmProjects/untitled/venv/lib/python3.5/site-packages/redis/connection.py", line 610, in send_command
    self.send_packed_command(self.pack_command(*args))
  File "/home/dowhat/PycharmProjects/untitled/venv/lib/python3.5/site-packages/redis/connection.py", line 585, in send_packed_command
    self.connect()
  File "/home/dowhat/PycharmProjects/untitled/venv/lib/python3.5/site-packages/redis/connection.py", line 489, in connect
    raise ConnectionError(self._error_message(e))
redis.exceptions.ConnectionError: Error 111 connecting to IP:6379. Connection refused.

Process finished with exit code 1
