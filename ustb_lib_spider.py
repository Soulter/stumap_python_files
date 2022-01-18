import requests
import time
import json
import datetime
import win10toast

def reserveSeat(check_time, opening_time_list):
    year = datetime.datetime.now().strftime("%Y")
    month = datetime.datetime.now().strftime("%m")
    day = datetime.datetime.now().strftime("%d")
    print(year+month+day)
    close_time = opening_time_list[1][:2]+opening_time_list[1][-2:]
    print("get close time:"+close_time)


    login_url = "http://libzw.ustb.edu.cn/ClientWeb/pro/ajax/login.aspx?act=login&id=U202141035&pwd=ustb000000&role=512&aliuserid=&schoolcode=&wxuserid=&_nocache=1637235626380"
    reserve_url = "http://libzw.ustb.edu.cn/ClientWeb/pro/ajax/reserve.aspx?dialogid=&dev_id={}&lab_id=&kind_id=&room_id=&type=dev&prop=&test_id=&term=&Vnumber=&classkind=&test_name=&start={}-{}-{}+{}%3A{}&end={}-{}-{}+{}%3A{}&start_time={}&end_time={}&up_file=&memo=&act=set_resv"\
        .format(not_occupied_seats_id_list[0], year, month, day, check_time[:2], check_time[-2:], year, month, day,close_time[:2], close_time[-2:], check_time, close_time)
    print("test: reserveURL:"+reserve_url)
    response_log = requests.get(login_url,
        headers=headers)
    response = requests.get(reserve_url,
                            headers=headers)
    print("reserve_res:"+response.text)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Edg/94.0.992.38',
    'Cookie': 'Hm_lvt_13b40e489bb711d52e8face65ffaa168=1632546221,1634714912,1634718416,1635051809; ASP.NET_SessionId=uktih5aj0jz5yc55vgk2wy55; _d_id=8ea70ae28b27fbfee509e1a2ec8580',
    'Accept': '*/*',
    'Connection': 'keep-alive',
    'Referer': 'http://libzw.ustb.edu.cn/ClientWeb/m/ic2/Default.aspx'
}
#查座选座

#直接登录
#http://libzw.ustb.edu.cn/ClientWeb/pro/ajax/login.aspx?act=login&id=U202141035&pwd=ustb000000&role=512&aliuserid=&schoolcode=&wxuserid=&_nocache=1637235626380
#以下链接为图书馆房间信息列表
#http://libzw.ustb.edu.cn/ClientWeb/pro/ajax/room.aspx?classkind=8&date=2021-11-10&start=16:10&end=17:10&act=get_rm_sta&_nocache=1636531335107
#以下链接可以不用headers就可以get
#http://libzw.ustb.edu.cn/ClientWeb/pro/ajax/device.aspx?byType=devcls&classkind=8&display=fp&md=d&room_id=102057443&purpose=&selectOpenAty=&cld_name=default&date=2021-11-10&fr_start=15%3A30&fr_end=16%3A30&act=get_rsv_sta&_=1636529360022
lib_room_id_list = [100540999,100543976,100544640,100544829,100545037,100545208,100545387,100545390,100545650,102057443,100545791]
lib_room_name_list = ["图西楼一楼南区","图西楼一楼北区","图西楼二楼南区","图西楼二楼北区","图西楼三楼南区","图西楼三楼北区","图西楼三楼中厅","图西楼三楼301","图西楼四楼南区","图西楼四楼北区","图西楼四楼中厅",]
names_tar = ["赖潘豪","廖玮珑","张福升","张浩伦","蒋振楠","李小千","许佳伟","赵予","于睿迪","文博欣","韩天祥","丁晨","杨明勋","夏琳","李响","沈书祺","李霄洋","周亚","陈燃","范思哲","陈天乐"]
near_window_list = []
tar_in_occupied = False
lib_room_name_list_1 = ["图西楼一楼南区"]
lib_room_id_list_1 = [100540999]
not_occupied_seats_list = []
not_occupied_seats_id_list = []


stu_count = 0
#
i=75
while i<=135:
    near_window_list.append("F1A0"+str(i))
    near_window_list.append("F1A0" + str(i+1))
    i = i+4
i=0
while i<=57:
    near_window_list.append("F1B0"+str(i))
    near_window_list.append("F1B0" + str(i+1))
    i = i+4
i=111
while i<=152:
    near_window_list.append("F2A"+str(i))
    near_window_list.append("F1A" + str(i+1))
    i = i+4
i=123
while i<=176:
    near_window_list.append("F2B"+str(i))
    near_window_list.append("F2B" + str(i+1))
    i = i+4
i=107
while i<=156:
    near_window_list.append("F3A"+str(i))
    near_window_list.append("F3A" + str(i+1))
    i = i+4
# i="059"
# while i<=176:
#     near_window_list.append("F3B"+str(i))
#     near_window_list.append("F3B" + str(i+1))
#     i = i+4
i=123
while i<=176:
    near_window_list.append("F4A"+str(i))
    near_window_list.append("F4A" + str(i+1))
    i = i+4
toaster = win10toast.ToastNotifier()
hhstr = ""
for lib_room_name, lib_room_id in zip(lib_room_name_list_1, lib_room_id_list_1):
        # print("Starting spider. POWERED BY SOULTER")
        room_url = 'http://libzw.ustb.edu.cn/ClientWeb/pro/ajax/device.aspx?right=detail&fr_all_day=false&room_id'+str(lib_room_id)+'&name='+lib_room_name+'&open_start=700&open_end=2200&classkind=8&date=2022-01-04&start=13:30&end=22:00&act=get_rsv_sta&fr_start=15:40&fr_end=22:00'
        print("room_url:"+room_url)
        response = requests.get(room_url,
            headers=headers)
        # print(response.status_code)  # 打印状态码
        # print(response.url)  # 打印请求url
        # print(response.headers)  # 打印头信息
        # print(response.cookies)  # 打印cookie信息
        res = response.text
        # print(res)
        json_res = json.loads(res)
        seats_list = json_res.get("data")
        while True:
            hhstr = ""
            stu_count = 0
            # name_tar = str(input("Input what you want to search for..."))
            not_occupied_seats_list.clear()
            for seat_info in seats_list:
                try:
                    got_name = seat_info.get("ts")[0]["owner"]
                    stu_count += 1
                    # print(seat_info.get("ts")[0]["owner"])
                    if got_name in names_tar:
                        tar_in_occupied = True
                        # hhstr = hhstr + got_name +" "
                        print(got_name+" is in library "+ str(seat_info['title']) +" now."+" Duration: "+str(seat_info.get("ts")[0]['start'])+"-"+str(seat_info.get("ts")[0]['end']))
                        # break
                except Exception:
                    not_occupied_seats_list.append(str(seat_info['title']))
                    not_occupied_seats_id_list.append(str(seat_info["devId"]))
            # toaster.show_toast("WARNING", hhstr +" are in library now.")
            print("OnPeople: " + str(stu_count))
            print("[Not be occupied seats]: " + str(not_occupied_seats_list)+"\n"+"[Device Id] "+str(not_occupied_seats_id_list))
            print("[Total]: " + str(len(not_occupied_seats_list)))
            print("[Warning]: today's open time: "+str(seat_info['open']))
            # is_confirm_check = input("Check a seat which is near the wall? (time format like 0900) or 0: ")
            # if is_confirm_check != "0":
            #     reserveSeat(is_confirm_check, seat_info['open'])
            # break
        # if tar_in_occupied:
        #     break
        # print(res)  # 以文本形式打印网页源码
            time.sleep(300)

