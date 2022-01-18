# -*-coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import pymysql
import threading
import os

# db = pymysql.connect(host='39.100.5.139', port=3306, user='stumap', passwd='000112000112', db='stumap', charset='utf8')
# db = pymysql.connect(host='470b0527.nat123.net', port=38249, user='stumap', passwd='000112000112', db='stumap', charset='utf8')
cursor = db.cursor()


# res = requests.get("https://glzx.net/plus/view.php?aid=9321")
# soup = BeautifulSoup(res.text, 'html.parser')
# i = 2
# while i < len(soup.tbody.contents):
#     try:
#         list_fi = soup.tbody.contents[i].contents
#         print(list_fi)
#         stu_id = list_fi[1].contents[0].replace("\n", "").replace("\r", "").replace("\t", "")
#         stu_name = list_fi[3].contents[0].replace("\n", "").replace("\r", "").replace("\t", "")
#         scid = list_fi[7].contents[0].replace("\n", "").replace("\r", "").replace("\t", "")
#         stu_class = list_fi[5].contents[0].replace("\n", "").replace("\r", "").replace("\t", "")
#         # if data_id_list.count(stu_id) == 0:
#         #     sql = "INSERT IGNORE INTO students (id,class,name,scname) VALUES ('" + stu_id + "','" + stu_class + "','" + stu_name + "','" + scid + "');"
#         #     cursor.execute(sql)
#         #     print("新增 " + stu_id + stu_name + scid + stu_class)
#         #     f.write(stu_id + " ")
#         # else:
#         #     print("不需要更新:" + stu_id)
#         # # print(soup.tbody.contents[i].contents)
#         str1 = "https://restapi.amap.com/v3/geocode/geo?address=" + scid + "&output=json&key=75ebc6cfad423b5cf711e8200619b8a9"
#         res = requests.get(str1)
#         print(res.json())
#         idsc = str(i)
#         try:
#             lonlat = res.json().get("geocodes")[0].get("location").split(",")
#             sql = "INSERT IGNORE INTO nsc (id,scname,level,area,lon,lat) VALUES ('" + idsc + "','" + str_sc + "','" + "null" + "','" + "null" + "','" + \
#                   lonlat[0] + "','" + lonlat[1] + "');"
#             cursor.execute(sql)
#         except IndexError:
#             sql = "INSERT IGNORE INTO nsc (id,scname,level,area,lon,lat) VALUES ('" + idsc + "','" + str_sc + "','" + "null" + "','" + "null" + "','" + "0" + "','" + "0" + "');"
#             cursor.execute(sql)
#     except AttributeError:
#         i = i + 1
#     else:
#         i = i + 1
