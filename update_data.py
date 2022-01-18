import json
import time
import requests
import pymysql
f = open("school.txt", "r+", encoding='utf-8')
school_str = f.read()
json1 = json.loads(school_str)
i = 0
j = 0
db = pymysql.connect(host='39.100.5.139', port=3306, user='stumap', passwd='000112000112', db='stumap', charset='utf8')
cursor = db.cursor()
print(json1.get("data"))
for dic in json1.get("data"):
    str_prov = dic.get("province")
    print(str_prov)
    i+=1
    idsc = str(i)
    sql = "UPDATE nsc SET area='"+str_prov+"' WHERE id="+idsc+";"
    cursor.execute(sql)
    print(idsc+"/"+"2901")

print(i)
db.commit()
cursor.close()
db.close()
