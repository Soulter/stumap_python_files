# -*-coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import pymysql
import threading
import os

# def data_save(stu_id,stu_name,scid,stu_class):
def main_loop():
    if os.path.isfile("uploaded.txt"):
        f=open("uploaded.txt", "r+", encoding='utf-8')
        # data_id_list = []
        data_id_list = f.read().split(" ")
        f.close()
    else:
        data_id_list = []
    print(data_id_list)
    f=open("uploaded.txt", "a", encoding='utf-8')
    db = pymysql.connect(host='39.100.5.139', port=3306, user='stumap', passwd='000112000112', db='stumap', charset='utf8')
    cursor = db.cursor()
    res = requests.get("https://glzx.net/plus/view.php?aid=9321")
    print(res.text)
    # res.decoding = 'gb2312'
    # res.decode("gb2312").encode('utf-8')
    soup = BeautifulSoup(res.text, 'html.parser')
    i = 2
    tag = 0
    while i < len(soup.tbody.contents):
        try:
            list_fi = soup.findAll("tbody")[1].contents[i].contents
            stu_id = list_fi[1].contents[0].replace("\n","").replace("\r","").replace("\t","")
            stu_name = list_fi[3].contents[0].replace("\n","").replace("\r","").replace("\t","")
            scid = list_fi[7].contents[0].replace("\n","").replace("\r","").replace("\t","")
            stu_class = list_fi[5].contents[0].replace("\n","").replace("\r","").replace("\t","")
            if data_id_list.count(stu_id) == 0:
                sql = "INSERT IGNORE INTO students (id,class,name,scname) VALUES ('" + stu_id + "','" + stu_class + "','" + stu_name + "','" + scid + "');"
                # cursor.execute(sql)
                data_id_list.append(stu_id)
                print("新增 "+stu_id + stu_name + scid + stu_class)
                f.write(stu_id+" ")
                tag = 1
                # print(soup.tbody.contents[i].contents)
        except AttributeError:
            i = i+1
        else:
            i = i+1
    if tag==0:
        print("没有任何更新.")
    # db.commit()
    # cursor.close()
    # db.close()
    f.close()

def time_handler():
    main_loop()
    global timer
    timer = threading.Timer(600,time_handler)
    timer.start()
    print("定时器启动...600秒后执行任务")


if __name__ == '__main__':
    time_handler()







