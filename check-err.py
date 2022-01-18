# -*-coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import pymysql
import threading
import os
import json

f = open("stu.txt", "r+", encoding='utf-8')
stu_str = f.read()
json1 = json.loads(stu_str)
f.close()
res = requests.get("https://glzx.net/plus/view.php?aid=9321")
soup = BeautifulSoup(res.text, 'html.parser')
i = 2
db = pymysql.connect(host='39.100.5.139', port=3306, user='stumap', passwd='000112000112', db='stumap', charset='utf8')
cursor = db.cursor()
stu_name_in_file = ""
idsc = 2914

tagT = 0
while i < len(soup.tbody.contents):
    try:
        tag=0
        list_fi = soup.tbody.contents[i].contents
        # print(list_fi)
        stu_name = list_fi[3].contents[0].replace("\n", "").replace("\r", "").replace("\t", "")
        scid = list_fi[7].contents[0].replace("\n", "").replace("\r", "").replace("\t", "")
        stu_id = list_fi[1].contents[0].replace("\n", "").replace("\r", "").replace("\t", "")
        for stu_name_in_file in json1:
            if stu_name == stu_name_in_file.get("na"):
                tag = 1
                break
        if tag == 0:
            print(stu_name + " "+stu_id + " "+scid)
            # str1 = "https://restapi.amap.com/v3/geocode/geo?address=" + str_sc + "&city=" + str_city + "&output=json&key=75ebc6cfad423b5cf711e8200619b8a9"
            # res = requests.get(str1)
            # print(res.json())
            # idsc = str(i)
            str1 = "https://restapi.amap.com/v3/geocode/geo?address=" + scid + "&output=json&key=75ebc6cfad423b5cf711e8200619b8a9"
            res = requests.get(str1)
            print(res.json())
            try:
                lonlat = res.json().get("geocodes")[0].get("location").split(",")
                sql = "INSERT IGNORE INTO nsc (id,scname,area,lon,lat) VALUES ('" + str(idsc) + "','" + scid + "','" + "null" + "','" + lonlat[0] + "','" + lonlat[1] + "');"
                if stu_id == 398:
                    tagT=1
                if tagT == 1:
                    cursor.execute(sql)

            except IndexError:
                sql = "INSERT IGNORE INTO nsc (id,scname,area,lon,lat) VALUES ('" + str(idsc) + "','" + scid + "','" + "null" + "','" + "0" + "','" + "0" + "');"
                if tagT == 1:
                    cursor.execute(sql)
            i=i+1
    except AttributeError:
        i = i + 1
    else:
        i = i + 1
# db.commit()
cursor.close()
db.close()