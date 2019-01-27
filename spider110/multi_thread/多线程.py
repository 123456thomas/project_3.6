import requests
import threading
import time
import queue
import sys
from bs4 import BeautifulSoup
import pymysql

base_url = 'https://www.80s.la/movie/list/-----p'

headers = {
    "User_Agnet": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

url_q = queue.Queue()

for i in range(1, 436):
    target_url = base_url + str(i)
    url_q.put(target_url)


def get_url(url_q):
    while True:
        try:
            url = url_q.get_nowait()
            try:
                response = requests.get(url, headers=headers)
                if response.status_code == 200:
                    time.sleep(1)
                    # print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    # print(response.text)
                    html = BeautifulSoup(response.text, 'lxml')
                    sec = html.select('.me1 > li')
                    # print(sec)
                    # print(type(sec))
                    for sec1 in sec:
                        title = (sec1.select('h3 > a')[0].text).strip()
                        link1 = html.select('h3 > a')[0].attrs['href']
                        link = 'https://www.80s.la' + link1
                        try:
                            conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456',
                                                   db='1809_spidder')
                            cursor = conn.cursor()
                            sql = 'insert into 80s(name1, url)values (%s, %s)'
                            sql1 = (title, link)
                            cursor.execute(sql, sql1)
                            conn.commit()

                        except Exception as e:
                            print("错误：")
                            print(e)
                            pass

            except Exception as e:
                print("错误：")
                print(e)
                continue
        except Exception as e:
            print("错误：")
            print(e)
            sys.exit()

    cursor.close()
    conn.close()


if __name__ == "__main__":
    startTime = time.time()
    threads = []
    for i in range(1, 4):
        t = threading.Thread(target=get_url, args=(url_q,))
        threads.append(t)
        print(len(threads))
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    endTime = time.time()
    print('Done, Time cost: %s ' % (endTime - startTime))





