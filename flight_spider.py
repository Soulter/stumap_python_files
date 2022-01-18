# -*-coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import os
print("======SoulterL's Flight Fight======")
# 同程 去哪儿 各大航司：春秋 中联航 大新华
res = requests.get("https://www.ly.com/flights/itinerary/oneway/KWL-PEK?date=2021-08-29&from=%E6%A1%82%E6%9E%97&to=%E5%8C%97%E4%BA%AC")
# print(res.text)
# f = open("texttest_tc", "r+", encoding='utf-8')
# res = f.read()
# f.close()
soup = BeautifulSoup(res.text, 'html.parser')
res1_group_fna = soup.findAll('p', class_='flight-item-name')
res1_group_timeS = soup.findAll('div', class_='f-startTime f-times-con')
res1_group_timeE = soup.findAll('div', class_='f-endTime f-times-con')
res1_group_Fair = soup.findAll('div', class_='head-prices')
count = len(res1_group_fna)

loop = 0
print("--GL-BJ 同程旅游结果--")
fairT = 0
while loop < count:
    if loop == 0:
        fairT = int(res1_group_Fair[loop].contents[0].contents[0].contents[0].replace("¥",""))
    else:
        if fairT > int(res1_group_Fair[loop].contents[0].contents[0].contents[0].replace("¥","")):
            fairT = int(res1_group_Fair[loop].contents[0].contents[0].contents[0].replace("¥",""))
    print(res1_group_fna[loop].contents[0] + " " + res1_group_timeS[loop].contents[0].contents[0] + " " + res1_group_timeE[loop].contents[0].contents[0] + " " + res1_group_Fair[loop].contents[0].contents[0].contents[0])
    loop+=1
print("###最低费用："+str(fairT)+"###")

